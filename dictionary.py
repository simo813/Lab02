import translator as tr


class Dictionary:
    def __init__(self, dictionary=None):
        # Se non viene passato un dizionario, inizializzalo vuoto
        if dictionary is None:
            dictionary = {}
        self.dictionary = dictionary

    def loaddiz(self, dictionary):
        self.dictionary = dictionary

    def addWord(self, chiave, valore):
        """Aggiunge una parola e la sua traduzione al dizionario."""
        if chiave in self.dictionary:
            if valore not in self.dictionary[chiave]:  # Evita duplicati
                self.dictionary[chiave].append(valore)
        else:
            self.dictionary[chiave] = [valore]

    def __str__(self):
        """Restituisce una stringa leggibile del dizionario."""
        return str(self.dictionary)


    def translate(self, chiave):
        stringa = ", ".join(self.dictionary[chiave])
        print(stringa)

    def translateWordWildCard(self, chiave):
        """Stampa la traduzione di una parola con wildcard"""
        stringa = self.dictionary[chiave]

        # Controlla se il valore è una lista
        if isinstance(stringa, list):
            stringa = ", ".join(stringa)  # Concatena gli elementi in una stringa

        print(stringa)
