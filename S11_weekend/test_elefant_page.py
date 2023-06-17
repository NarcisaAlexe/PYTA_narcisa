"""
1. Intrati pe site-ul https://www.elefant.ro/
"""
import time
import unittest
from selenium import webdriver


class TestElefantPage(unittest.TestCase):
    LINK = "https://www.elefant.ro/"

    def setUp(self):
        # cream driverul
        self.driver = webdriver.Chrome()
        # accesam link-ul www.elefant.ro

        self.driver.get(self.LINK)
        # maximizam fereastra de browser
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self):
        # inchidem browserul
        self.driver.quit()

    def test_page_title(self):
        actual = self.driver.title
        expected = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"
        self.assertEqual(expected, actual)


"""
2. Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
cel putin 10 rezultate ([class="product-title"])
"""


"""
3. Extrageti din lista produsul cu pretul cel mai mic [class="current-price "]
din primele 10 produse gasite
(puteti sa va folositi de find_elements)
"""


"""
4. Extrageti titlul paginii si verificati ca este corect
"""

