from bs4 import BeautifulSoup
import requests
import time



med_link = requests.get('https://www.lung.org/lung-health-diseases/lung-disease-lookup/influenza/symptoms-causes-and-risk').text
soup = BeautifulSoup(med_link, 'lxml')
symptoms = soup.find_all('div', class_ = 'fr-view')

def find_sypmtoms(): 
    for symptom in symptoms:
    
        short_sypmtom = symptom.find('p', class_ = None).text
        if len(short_sypmtom) < 150:
            print(short_sypmtom)
            print(" ")
        
