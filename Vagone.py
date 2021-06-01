

class Vagone():
    def __init__(self,lunghezza : float,peso_a_vuoto : float):
        self._lunghezza = max(lunghezza, 0)
        self._peso_a_vuoto = max(peso_a_vuoto, 0)


#getter

    def get_lunghezza(self):
        return self._lunghezza

    def get_peso_a_vuoto(self):
        return self._peso_a_vuoto

#setter

    def set_lunghezza(self, lunghezza : float):
        if lunghezza <= 0 :
            self._lunghezza = ""
            raise ("la lunghezza non è valida")
        else:
            self._lunghezza = lunghezza        
    
    def peso_a_vuoto(self, peso_a_vuoto : float):
        if peso_a_vuoto <= 0 :
            self._peso_a_vuoto = ""
            raise ("il peso a vuoto non è valido")
        else:
            self._peso_a_vuoto = peso_a_vuoto

#metodo get_peso_totale

    def get_peso_totale(self):
        return self._peso_a_vuoto  

#metodo string

    def __str__(self):
        return "\nLunghezza:" + str(self._lunghezza) + "\nIl peso a vuoto:" + str(self._peso_a_vuoto)