import re

from dictionary import Dictionary  # Importa correttamente la classe Dictionary

class Translator:

    def __init__(self):
        self.dictionary = Dictionary()  # Istanza corretta

    def printMenu(self):
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")

    def loadDictionary(self, nomeFile):
        with open(nomeFile, "r", encoding="utf-8") as file:
            dizionario = {}
            for riga in file:
                campi = riga.rstrip("\n").split(" ")
                if len(campi) >= 2:
                    chiave = campi[0]
                    valori = campi[1]  # Tutto il resto sono le traduzioni
                    dizionario[chiave] = valori
        self.dictionary.loaddiz(dizionario)  # Carichiamo il dizionario

    def stampa(self):
        """Stampa il dizionario caricato"""
        for chiave in self.dictionary.dictionary:
            print(chiave, self.dictionary.dictionary[chiave])

    def handleAdd(self, entry):
        """Aggiunge una nuova parola al dizionario"""
        campi = entry.split(" ")
        if len(campi) < 2:
            print("Formato non valido. Usa: <parola> <traduzione>")
            return

        chiave = campi[0]
        valore = campi[1]
        self.dictionary.addWord(chiave.lower(), valore)  # Usa self.dictionary


    def handleTranslate(self, query):
        traduzione = self.dictionary.translate(query.lower())
        print("la traduzione di ", query, " è: ", traduzione)


    def handleWildCard(self, query):
        """Cerca parole che corrispondono alla query con wildcard (?)"""
        regex_pattern = query.replace("?", ".")  # Sostituisce ? con . (qualsiasi carattere)
        regex_pattern = f"^{regex_pattern}$"  # Assicura che tutta la parola corrisponda

        for chiave in self.dictionary.dictionary:
            if re.match(regex_pattern, chiave):  # Controlla se la chiave corrisponde
                self.dictionary.translateWordWildCard(chiave)
