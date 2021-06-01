
from Vagone import Vagone

class VagoneMerci(Vagone):
    def __init__(self,lunghezza : float,peso_a_vuoto : float,peso_caricato : float,peso_trasportabile : float):
        super().__init__(lunghezza, peso_a_vuoto)
        if peso_caricato <= peso_trasportabile:
            self._peso_caricato = max(peso_caricato, 0)
        else:
            self._peso_caricato = "peso caricato non valido"

        self._peso_trasportabile = max(peso_trasportabile, 0)


#getter

    
    def get_peso_caricato(self):
        return self._peso_caricato
    
    def get_peso_trasportabile(self):
        return self._peso_trasportabile


    def __str__(self):
        return super().__str__()+ "\nIl peso caricato:" + str(self._peso_caricato) + "\nIl peso trasportabile:" + str(self._peso_trasportabile)