from dbconnecter import ConnectToDatabase       #importeer zelfgemaakte klas die verbinding maakt met database
from Conserved import Conservatie      #importeer zelfgemaakte klas die opzoek gaat naar motief

def main():
    """Roept functies aan
    """
    #lijst = conservatie(seqs, accessie)
    connectie = ConnectToDatabase()     #hierdoor kan de ConnectToDatabase worden gebruikt
    connectie.__verander_grootte__('SET FOREIGN_KEY_CHECKS = 0')        #hierdoor kan de database worden ingevuld
    #set_conservatie(connectie, lijst)
    #invullen_eiwitfamilie(connectie)
    connectie.__sluit_connectie__()

def conservatie(seqs, accessie):
    """Zoek voor elke sequentie het motief en returned een ljst met daarin een lisjst met accessie en motief.
    """
    totaal = []
    con = Conservatie()     #hierdoor kan de Conservatie klas worden gebruikt
    for i in range(len(accessie)):
        een_product = []
        con.__vind_textarea__(seqs[i])      #vul de sequentie in
        try:
            motief = con.__get_motif__()        #probeer motief te krijgen
        except:     #als het vorige niet lukt ga hier verder
            motief = ""     #zet motief naar een lege string
        een_product.append(accessie[i])     #accessie wordt toegevoegd aan een lijst 1
        een_product.append(motief)      #motief wordt toegevoegd aan een lijst 1
        totaal.append(een_product)      #lijst wordt toegevoegd aan de lijst 2
    return totaal

def set_conservatie(connectie, totaal):
    """De database vullen met het motief, accessiecode en de primary key is een getal.
    """
    for i in range(len(totaal)):
        motief = totaal[i][1]
        acc = totaal[i][0]
        connectie.__set_data__("INSERT INTO geconserveerde_stukken(motif,eiwitsequentie_accessiecode, id) "
                               "VALUES (%s,%s,%s)", (motief, acc, i))

def invullen_eiwitfamilie(connectie):
    """De database wordt gevuld met het domein en de familienaam.
    """
    connectie.__set_data__("INSERT INTO eiwitfamilie(domein, familie_naam) VALUES(%s,%s)",
                           ('Porin_1', 'Gram-negative porin family'))

def set_eiwitfunctie():
    """"De functie bevat de lijst met functies van het eiwit, deze worden gereturned.
    returned de functies
    """
    functies = ["receptor voor bacteriofaag T2", "vormt porie voor passieve difussie"]
    return functies





main()
