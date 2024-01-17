import tensorflow as tf
from tensorflow.keras import layers

class GPTModel(tf.keras.Model):
    def __init__(self, vocab_size, max_len=512, num_heads=8, ff_dim=32, num_transformer_blocks=6, embedding_dim=32):
        super(GPTModel, self).__init__()

        # Layer di embedding per convertire gli indici delle parole in vettori di embedding
        self.embedding = layers.Embedding(vocab_size, embedding_dim)

        # Blocchi trasformatore multi-testa
        self.transformer_blocks = [TransformerBlock(embedding_dim, num_heads, ff_dim) for _ in range(num_transformer_blocks)]

        # Aggiunta di pesi per la codifica posizionale
        self.positional_encoding = self.add_weight("position_embeddings", shape=(max_len, embedding_dim))

        # Normalizzazione dei livelli
        self.layer_normalization = layers.LayerNormalization(epsilon=1e-6)

        # Appiattimento dei tensori
        self.flatten = layers.Flatten()

        # Layer densamente connesso alla fine per la generazione di output
        self.dense = layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Passaggio attraverso il layer di embedding
        x = self.embedding(inputs)

        # Aggiunta della codifica posizionale
        x += self.positional_encoding

        # Passaggio attraverso i blocchi trasformatore multi-testa
        for transformer_block in self.transformer_blocks:
            x = transformer_block(x)

        # Normalizzazione del livello
        x = self.layer_normalization(x)

        # Appiattimento del tensore
        x = self.flatten(x)

        # Passaggio attraverso il layer densamente connesso per generare l'output
        output = self.dense(x)

        return output

class TransformerBlock(tf.keras.layers.Layer):
    def __init__(self, embedding_dim, num_heads, ff_dim, rate=0.1):
        super(TransformerBlock, self).__init__()

        # Attention multi-testa
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embedding_dim)

        # Feedforward network
        self.ffn = tf.keras.Sequential([layers.Dense(ff_dim, activation='relu'), layers.Dense(embedding_dim)])

        # Normalizzazione del livello prima dell'attenzione
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)

        # Normalizzazione del livello dopo l'attenzione
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)

        # Dropout prima e dopo l'attenzione
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs):
        # Passaggio attraverso l'attenzione multi-testa
        attn_output = self.att(inputs, inputs)

        # Applicazione di dropout
        attn_output = self.dropout1(attn_output)

        # Aggiunta della connessione residua e normalizzazione del livello
        out1 = self.layernorm1(inputs + attn_output)

        # Passaggio attraverso la feedforward network
        ffn_output = self.ffn(out1)

        # Applicazione di dropout
        ffn_output = self.dropout2(ffn_output)

        # Aggiunta della connessione residua e normalizzazione del livello
        return self.layernorm2(out1 + ffn_output)

# Definisci il tuo vocabolario e la lunghezza massima della sequenza
vocab_size = 10000  # Sostituisci con la dimensione del tuo vocabolario
max_len = 512  # Sostituisci con la tua lunghezza massima di sequenza

# Crea un'istanza del modello
model = GPTModel(vocab_size=vocab_size, max_len=max_len)

# Compila il modello
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
