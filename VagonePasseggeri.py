from Vagone import Vagone


class VagonePasseggeri(Vagone):
    
    def __init__(self,lunghezza : float,peso_a_vuoto : float,passeggeri : int,capienza : int):
        super().__init__(lunghezza,peso_a_vuoto)
        self._passeggeri = passeggeri
        self._capienza = max(capienza,300) # definisco n massimo di passeggeri (posso metterlo anche com const nell init)


#getter

    def get_passeggeri(self):
        return self._passeggeri
    
    def get_capienza(self):
        return self._capienza

#metodo sale passeggero

    def sale_passeggero(self):
        return self._passeggeri + 1

    def scende_passeggero(self):
        return self._passeggeri - 1


    def __str__(self):
        return super().__str__() + "\nPasseggeri:" + str(self._passeggeri) + "\nCapienza:" + str(self._capienza) 