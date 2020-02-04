import requests
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver


def eprint(*args, **kwargs):
    # pass
    print(*args, file=sys.stderr, **kwargs)

def extract_json(url):

    options = webdriver.chrome.options.Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    
    driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), 'chromedriver.exe'), options=options)

    print('friendly')

    time.sleep(3)

    driver.get(url)

    # time.sleep(30)

    print(driver.page_source)

    with open('./debug.txt', mode='w', encoding='utf8') as out:
        out.write(driver.page_source)

    soup = BeautifulSoup(driver.page_source, features="html.parser")


extract_json('https://careers.microsoft.com/i/us/en/job/756760/Software-Engineer')