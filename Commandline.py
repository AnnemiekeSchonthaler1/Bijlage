import subprocess
import os
import re


def main():
    accessiecodelijst = []
    count = 0
    for i in range(0, 8):
        if count == 0:  # Als er al een msa is gemaakt hoeft het niet opnieuw
            infile = "familie_sequenties"
            outfile = "alignment"
            hmmfile = "hmm_alignment"
            MAFFT(infile, outfile)
            hmmbuild(outfile, hmmfile)
            hmmsearch(outfile, hmmfile, accessiecodelijst)
            hmmbuild(outfile, hmmfile)
            count += 1
        else:
            hmmsearch(outfile, hmmfile, accessiecodelijst)
            hmmbuild(outfile, hmmfile)


def MAFFT(infile, outfile):
    """
    Deze functie voert een msa uit met behulp van MAFFT.
    :param infile: Het bestand met de sequenties waar de msa van wordt gemaakt
    :param outfile: Het bestand waar de msa in wordt gestopt
    """
    if os.path.isfile(outfile):
        pass
    else:
        cmd = '"/usr/bin/mafft"  --retree 2 --reorder {} > {}'.format(infile,
                                                                      outfile)
    e = subprocess.call(cmd, shell=True)


def hmmbuild(outfile, hmmfile):
    """
    Deze functie bouwt een hmm aan de hand van een msa.
    :param outfile: Het bestand waar het hmm in wordt gestopt
    :param hmmfile: Het bestand van het hmm
    """
    cmd = "hmmbuild {} {}".format(hmmfile, outfile)
    e = subprocess.check_call(cmd, shell=True)


def hmmsearch(outfile, hmmfile, accessiecodelijst):
    """
    Deze functie doorzoekt Swissprot met het hmm
    :param outfile: Het bestand waar de msa in wordt gestopt
    :param hmmfile: Het bestand waar de hmm in zit
    :param accessiecodelijst: Een lijst waar alle identieke gevonden
        accessiecodes in worden gestopt
    """
    cmd = "hmmsearch -A {} --tblout {} --acc {} swissprot".format(outfile,
                                                                  outfile + str(
                                                                      "_leesbaar"),
                                                                  hmmfile)
    e = subprocess.check_call(cmd, shell=True)
    fileappender(outfile + str("_leesbaar"), accessiecodelijst)


def fileappender(bestandsnaam_input, accessiecodelijst):
    """
    Deze functie zoekt de accessiecodes van de sequenties die matchte met het msa
    :param bestandsnaam_input: Het bestand met de msa
    :param accessiecodelijst: De lijst waar de identieke accessiecodes in komen
    """
    # In dit bestand worden de accessiecodes gestopt.
    bestand_append = open("alle_matches", "a")
    # Dit bestand heeft de msa.
    bestand_input = open(bestandsnaam_input, "r")
    # Deze regex zoekt op de accessiecodes.
    regex = "([A-Z]+[0-9]{1,5})+([A-Z]{1}[0-9]{1})*[\.]{1}[0-9]{1}"
    for regel in bestand_input.readlines():
        match = re.search(regex, regel)
        if match is None:
            # als er geen match is gevonden maak ik een string die niets
            # oplevert om te voorkomen dat hij met None gaat zoeken
            match = "ditkomtnooitaanhetbeginvoorhihi"
        else:
            match = match.group(1)
        if regel.startswith(match):
            # Ik zorg dat er geen dubbele zijn
            if match not in accessiecodelijst:
                bestand_append.write(match)
                bestand_append.write("\n")
                accessiecodelijst.append(match)


main()
