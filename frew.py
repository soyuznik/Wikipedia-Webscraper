from tkinter import Button as Buton
from tkinter import *
from parameterized import parameterized, param
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest
from selenium.webdriver.common.keys import Keys
import os
from nose.tools import assert_equal

import unicodedata

global textelem
global textelem1




class Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Tk()
        chrome_options = webdriver.ChromeOptions()
        h = IntVar()

        def SearchStopper():

            global componentInput
            componentInput = e.get()
            if (h.get() == 1):
                chrome_options.headless = True
                print("itstrue")
            if (h.get() == 2):
                chrome_options.headless = False
                print("itsfalse")
            root.destroy()

        root.title("Webscraper")

        # setting the window

        h.set("1")
        root.geometry("300x70")
        root.title("Webscraper")
        # create
        e = Entry(root, width=25)
        w = Radiobutton(text="headless", value=1, variable=h)
        w1 = Radiobutton(text="normal", value=2, variable=h)
        b = Buton(text="Submit", padx=30, pady=1, command=SearchStopper)

        # insert
        w.grid(column=0, row=1)
        w1.grid(column=0, row=2)
        e.grid(column=0, row=0)
        b.grid(column=1, row=0)

        root.mainloop()




    @parameterized.expand([
        (2, 3, 5),
        (1, 3, 4),
        (3, 3, 6),
        (4, 3, 7),
        (2, 5, 7),
        (2, 8, 10),

    ])

    def testWTFAMIWASTINGMYLIFEON(self, a, b, expected):
        assert_equal(a + b, expected)  # nopepad
        chrome_options = webdriver.ChromeOptions()
        PATH = r"D:\Pycharm\PyCharm Community Edition 2020.2.1\chromedriver.exe"
        self.driver = webdriver.Chrome(
            executable_path=PATH, chrome_options=chrome_options)
        self.driver.get("https://ro.wikipedia.org/wiki/" + componentInput)
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="toc"]')))
        except:
            print('//*[@id="toc"] --- not found')
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]/tbody')))
        except:
            print('//*[@id="mw-content-text"]/div[1]/table[2]/tbody --- not found')

        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        except:
            print("notfound")
            self.driver.quit()

        textelem = self.driver.find_element_by_css_selector('body').text

        def strip_accents(textelem):

            textelem = unicodedata.normalize('NFD', textelem) \
                .encode('ascii', 'ignore') \
                .decode("utf-8")

            return str(textelem)

        yourfile = r"\file" + str(expected)
        location = r"D:\Pycharm\\" + componentInput
        format = r".txt"
        if (expected==5):
            directory = componentInput
            parent_dir = "D:\Pycharm"
            mode = 0o666
            path = os.path.join(parent_dir, directory)
            os.mkdir(path, mode)
            print("Directory '% s' created" % directory)

        finalstring = location + yourfile + format
        print(finalstring)

        file = open(finalstring, 'w+')
        textelem = strip_accents(textelem)
        file.writelines(textelem)

        file.close()




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":  # gotta not be in the unittest class
    unittest.main()
