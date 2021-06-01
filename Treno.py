from Vagone import Vagone


class Treno():
    def __init__(self,sigla : str,lunghezza_locomotiva : float, peso_locomotiva :float,composizione : list):
        self._sigla = sigla
        self._lunghezza_locomotiva = lunghezza_locomotiva
        self._peso_locomotiva = peso_locomotiva
        self._composizione = []

#metodo aggiungi vagone

    def aggiungi_vagone(self, obj : Vagone):        
        self._composizione.append(obj)
    

    #metodo che restituisce il numero di oggetti lista

    def lunghezza_totale(self)-> int:
        return len(self._composizione)


    def peso_totale(self)-> float:
        return self._peso_locomotiva * len(self._composizione) + 80

    def __str__(self):
        return "\nSigla:" + str(self._sigla) + "\nLunghezza Locomotiva: " + str(self._lunghezza_locomotiva) + "\nPeso Locomotiva: " + str(self._peso_locomotiva) + "\nComposizione: " + str(self._composizione) 
    
