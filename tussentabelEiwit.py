from dbconnecter import ConnectToDatabase
import re

def main():
    """Aanroep van functies
    """
    seqs, accessie = seq_set_data(bestand="sequenties.txt")
    bestand = "GO_info_ompf (1).txt"
    totaal = eiwit_tussentabel(bestand, accessie)
    connectie = ConnectToDatabase()
    connectie.__verander_grootte__("SET FOREIGN_KEY_CHECKS = 0")
    invullen_tussentabel(totaal, connectie)
    connectie.__sluit_connectie__()


def invullen_tussentabel(totaal, connectie):
    """Vul tussentabel in
    :param totaal: is een lijst die de accessiecodes en functies bevat
    :param connectie: hierdoor is er een connectie met de database en kunnen er waarden worden ingevuld.
    """
    for e in range(len(totaal)):
        acc = totaal[e][0]
        func = totaal[e][2]
        connectie.__set_data__(
            "INSERT INTO tussentabel_eiwit_eiwit_functie(eiwit_functie_functie, ID,eiwitsequentie_accessiecode)"
            "VALUES(%s,%s,%s)", (func, e+197, acc))



def eiwit_tussentabel(bestand, accessie):
    """Er wordt een lege lijst gemaakt. Er wordt over het bestand geïtereerd. 
    Voor elke regel wordt er gekeken of er op de eerste positie de accesiecode overeenkomt met de lijst van de familieaccessiecodes.
    Als het overeenkomt dan wordt het toegevoegd aan een lijst. Vervolgens wordt  de functie toegevoegd en als er nog een functie is
    dan wordt dat ook toegevoegd aan de lijst. De lijst wordt dan toegevoegd aan een andere lijst.
    Hierdoor heb je een lijst met meerdere lijsten die de accesiecode en functies bevat.
    De lijst wordt gereturneerd.
    :param bestand: lees het bestand
    :param accessie: bevat de accessiecodes van de familie
    """
    totaal = [];
    b = open(bestand, 'r')      #open bestand
    for line in b:
        line = line.split('\t')     #regel wordt gesplit op tabs
        acc_en_func = []
        for a in accessie:
            if a ==  line[0]:       #als accessie gelijk is aan de accessiecode op positie 0 in het bestand
                acc_en_func.append(a)       #accessiecode wordt toegevoegd
                acc_en_func.append(line[1])     #functie op positie 1 wordt toegevoegd
                try:        #niet elke regel heeft een tweede functie
                    line[2] = line[2].strip('\n')       #van functie op positie 2 wordt de enter weggehaald
                    acc_en_func.append(line[2])     #functie wordt toegevoegd
                except:
                    print("niet gelukt")
        totaal.append(acc_en_func)      #voeg aan de lijst toe
    return totaal


def seq_set_data(bestand):
    """Het bestand opent een bestand en leest het.
    Het kijkt of de regel leeg is en als dat niet het geval is, kijkt het of het een header is.
    Als het een header is wordt het toegevoegd aan een lijst en anders wordt het ook toegevoegd aan de lijst. 
    Als het een header is wordt er ook gekeken naar de accessiecode door middel van een regular expression.    
    :param bestand: geef bestand mee en lees het
    :return: een lijst met sequenties en accessies
    """
    seqs = []; accessie = []; sequentie = ""; DOORGAAN = True
    bestandlezen = open(bestand, 'r')
    while DOORGAAN:
        regel = bestandlezen.readline()
        regel = regel.strip("\n")
        if regel == "":
            seqs.append(sequentie)
            DOORGAAN = False
        else:
            if regel.startswith('>'):
                if sequentie != "":
                    seqs.append(sequentie)
                    sequentie = ""
                # onderstaande regel overgenomen van stackoverflow:
                # https://stackoverflow.com/questions/8569201/get-the-string-within-brackets-in-python#8569258
                m = re.search(r"\(([A-Za-z0-9_]+)\)", regel)
                accessie.append(m.group(1))
            else:
                sequentie += regel
    return seqs, accessie

main()
