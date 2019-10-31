from selenium.webdriver.common.keys import Keys     #hierdoor kan je tekst plaatsen op site
from selenium import webdriver  #hierdoor kan je zoeken op sites automatiseren
import time

class Conservatie:
    def __init__(self):
        self.site = webdriver.Chrome(executable_path="C:/Users/noah-/chromedriver.exe")     #heeft een chromedriver nodig, om te zoeken op chrome
      
    def __vind_textarea__(self, seq):
        """De prosite wordt geopend. Er wordt gezocht naar een tekstveld. 
        Er wordt een sequentie in het tekstveld toegevoegd en vervolgens op de submit knop getriggerd.
        De volgende site wordt dan geopend.
        """
        self.site.get("https://prosite.expasy.org/")
        self.site.find_element_by_name("seq").send_keys(seq)
        knop = self.site.find_element_by_name("submit")
        knop.click()

    def __get_motif__(self):
        """Op de pagina wordt er gezocht naar de klas naam: matchseq. En de uitkomst daarvan (het motief) wordt gereturned.
        """
        return (self.site.find_element_by_class_name("matchseq").text)

    def __get_posities__(self):
        """Op de pagina wordt gezocht naar de klasnaam matchpos. Hier staat namelijk de positie van het motief.
        Dit wordt gereturned.
        """
        return (self.site.find_element_by_class_name("matchpos").text)

