import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id='ResultsContainer')

job_elements = results.find_all("div", class_="card-content") #This gives back an iterable set of data

# print(results.prettify)

for job_element in job_elements:
    print(job_element, end="\n"*4)

