from veicolo import Veicolo
from autoelettrica import AutoElettrica

def main():
    automobile0 = Veicolo("Fiat", "500L", "Grigio")
    automobile1 = AutoElettrica("Tesla", "Model S", "Nero", 500)

    automobile1.accendi()
    automobile1.statoAuto()
    automobile1.mostraAutonomia()
    automobile1.ferma()
    automobile1.statoAuto()

if __name__ == "__main__":
    main()
