# main.py

from programmi_generici import programmi as pr
from esercitazioni import CalcolatriceDiMedia as cm

def hello_studio():
    print("Benvenuto in Hello Studio!\nAl momento disponiamo di questi programmi: \neq2\ninverti\nMCD\nsomma\nmedia\nvarianza\nordinacongetCollaz\ncontaVocali\n")

if __name__ == "__main__":
    hello_studio()
    print("Desidere visualizzare la sintassi di un programma? (s/n)")
    risposta = input()
    if risposta == "s":
        pr.sintassi()
        pr.


