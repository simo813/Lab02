import translator as tr
import dictionary as d


def main():

    t = tr.Translator()
    t.loadDictionary("dictionary.txt")
    while True:
        t.printMenu()
        print("inserisci il numero che corrisponde alla richiesta: ")
        txtIn = input()
        if int(txtIn) == 1:
            print("Inserire una nuova parola e la relativa traduzione secondo il seguente pattern: <parola aliena> <traduzione> (separate da uno spazio)")
            entry = input()
            t.handleAdd(entry)
            continue
        if int(txtIn) == 2:
            print("Cercare la traduzione di una parola esistente inserendo <parola aliena>" )
            query = input()
            t.handleTranslate(query)
            continue
        if int(txtIn) == 3:
            print("Cercare la traduzione di una parola esistente con wildcard \n inserendo <parola aliena> con un solo punto interrogativo")
            query = input()
            t.handleWildCard(query)
            continue
        if int(txtIn) == 4:
            break



main()
