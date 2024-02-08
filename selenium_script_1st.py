from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium_script_2nd import list_of_today, save_at_once, save_excel_file, show_df
import pandas
import pickle
import bs4
import requests
import request

opt = Options()
opt.add_argument('--disable-notifications')
#useragent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'
#opt.add_argument(useragent)
driver = webdriver.Chrome(chrome_options=opt, executable_path='chromedriver.exe')

longest_sentences = []
shortest_sentences = []

def run_script(key_word):

    s = driver.get('https://www.google.com')

    search_box = driver.find_element(By.NAME, 'q')
    search_query = key_word
    search_box.send_keys(search_query)

    time.sleep(5)

    suggestions = driver.find_elements(By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li')

    sentences = []
    for suggestion in suggestions:
        text = suggestion.text
        first_sentence = text.split('\n')[0]
        words = first_sentence.split()
        sentences.append([len(words), first_sentence])
    if len(sentences) is not 0 or 1:
        sentences = sorted(sentences, key=lambda x: x[0])
        midpoint = len(sentences) // 2
        shortest = sentences[0]
        longest = sentences[-1]

        shortests = sentences[:midpoint]
        longests = sentences[midpoint:]
    elif len(sentences) == 1:
        shortest = sentences[0]
        longest = sentences[0]
    elif len(sentences) == 0:
        shortest = "NULL"
        longest = "NULL"
    longest_sentences.append(longest[1])
    shortest_sentences.append(shortest[1])

for keyWords in list_of_today:
    run_script(keyWords)
save_at_once(longest_sentences, shortest_sentences)
show_df()
save_excel_file()
driver.quit()