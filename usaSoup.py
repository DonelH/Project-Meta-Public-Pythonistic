import requests
from bs4 import BeautifulSoup
import re

URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States'
page = requests.get(URL)
state_list = []

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'mw-content-text')
results_table = results.find('table', class_ = 'wikitable')

state_list = []
state_elems = results_table.find_all('tr')
def scrapeUSA():
    for state_elem in state_elems:
        if (state_elem.find('a') and state_elem.find('a').has_attr('title')
            and not(state_elem.has_attr('style'))):
            if(state_elem !=''):
                state_title = state_elem.find('a').text
                td_list = state_elem.find_all('td')
                state_cases = re.sub('<|t|d|>|/|,', '', str(td_list[0]))
                state_cases = state_cases.rstrip('\n')
                state_deaths = re.sub('<|t|d|>|/|,', '', str(td_list[1]))
                state_deaths = state_deaths.rstrip('\n')
                if(state_title == 'Kansas'):
                    state_cases = str(td_list[0])
                    state_cases = state_cases[4:9]
                    state_cases = re.sub('<|t|d|>|/|,', '', state_cases)
            state_list.append([state_title, int(state_cases),int(state_deaths)])
    print(state_list)
    return state_list

if __name__ == '__main__':
    scrapeUSA()

 

