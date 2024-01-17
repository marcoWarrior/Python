# Errori Comuni in Python

# 1. SyntaxError
# Descrizione: Errore di sintassi nel codice.
try:
    # Esempio con un errore di sintassi (in questo esempio mancano le parentesi)
    print "Hello, World!"
except SyntaxError as e:
    print(f"SyntaxError: {e}")

# 2. IndentationError
# Descrizione: Errore di indentazione nel codice.
try:
    # Esempio con un errore di indentazione
    for i in range(5):
    print(i)
except IndentationError as e:
    print(f"IndentationError: {e}")

# 3. TypeError
# Descrizione: Tentativo di eseguire un'operazione su un tipo di dato non supportato.
try:
    # Esempio con un TypeError
    result = "5" + 3
except TypeError as e:
    print(f"TypeError: {e}")

# 4. ValueError
# Descrizione: Errore generato quando una funzione riceve un argomento con un tipo corretto, ma un valore inaccettabile.
try:
    # Esempio con un ValueError
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# 5. NameError
# Descrizione: Tentativo di accedere a una variabile o a una funzione che non è stata definita.
try:
    # Esempio con un NameError
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

# 6. FileNotFoundError
# Descrizione: Tentativo di aprire o manipolare un file che non esiste.
try:
    # Esempio con un FileNotFoundError
    with open("file_inesistente.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# 7. ZeroDivisionError
# Descrizione: Tentativo di dividere per zero.
try:
    # Esempio con un ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# 8. KeyError
# Descrizione: Tentativo di accedere a una chiave inesistente in un dizionario.
try:
    # Esempio con un KeyError
    my_dict = {"key1": "value1"}
    value = my_dict["key2"]
except KeyError as e:
    print(f"KeyError: {e}")

# 9. IndexError
# Descrizione: Tentativo di accedere a un indice non valido in una sequenza.
try:
    # Esempio con un IndexError
    my_list = [1, 2, 3]
    element = my_list[5]
except IndexError as e:
    print(f"IndexError: {e}")

# 10. AttributeError
# Descrizione: Tentativo di accedere a un attributo di un oggetto che non esiste.
try:
    # Esempio con un AttributeError
    my_object = {}
    value = my_object.attribute
except AttributeError as e:
    print(f"AttributeError: {e}")

# 11. Exception
# Descrizione: Classe di base per tutti gli errori. Può essere utilizzata per catturare qualsiasi tipo di errore non previsto.
try:
    # Esempio con Exception
    result = 10 / "abc"
except Exception as e:
    print(f"Exception: {e}")

# Blocchi try-except, else e finally
try:
    # Esempio con blocchi try, except, else e finally
    number = int("123")
except ValueError as e:
    print(f"ValueError: {e}")
else:
    print("Conversione riuscita!")
finally:
    print("Eseguito sempre, indipendentemente da ciò che accade.")
