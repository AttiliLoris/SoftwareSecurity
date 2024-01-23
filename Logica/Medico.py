class Medico(object):
    def __init__(self, nome, cognome, codiceFiscale):
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale

    def salva(self, vettore):
        self.nome = vettore[0]
        self.cognome = vettore[1]
        self.codiceFiscale = vettore[2]
