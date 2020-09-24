import bs4
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import json
import re
import lxml.html
import time
import random
from random import randint
import logging
import collections
from time import gmtime, strftime

from selenium.webdriver.firefox.options import Options

import re
from tabulate import tabulate
import os
date=strftime("%Y-%m-%d")


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os


url='https://www.immoweb.be/en/classified/house/for-sale/woluwe-st-pierre/1150/8822695?searchId=5f6c5ef9a8eb3'


opts = Options()
opts.headless=True
driver = webdriver.Firefox(options=opts)

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

driver.close()

# with open('immo.html', 'w') as file:
#     file.write(driver.page_source)

# with open('immo2.html', 'w') as file:
#     file.write(soup.__str__())


