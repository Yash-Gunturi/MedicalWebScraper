from bs4 import BeautifulSoup
import requests
import time

print('What would you like to learn about today?')
user_req = input('>')
print(f'Searching for {user_req}')

med_link = requests.get('https://www.lung.org/lung-health-diseases/lung-disease-lookup/influenza/symptoms-causes-and-risk').text
soup = BeautifulSoup(med_link, 'lxml')
symptom_info = soup.find_all('div', class_ = 'fr-view')


def find_sypmtoms(): 

    for symptom in symptom_info:
    
        short_sypmtom = symptom.find('p', class_ = None).text
        if len(short_sypmtom) < 150:
            print(short_sypmtom)
            print(" ")

def flu_info():
    
    for info in symptom_info:

        pub = info.get_text()
        if len(pub) > 150:
            print(pub)
            print(" ")

if user_req == "flu":

    print("What about the flu would you like to learn? Please type keywords: general info, symptoms, treatment")
    search_req = input('>')

    match search_req:

        case "general info":

            print(f'{search_req} of the {user_req}: ')
            print(" ")
            flu_info()
            
        case "symptoms":

            print(f'{search_req} of the {user_req}: ')
            print(" ")
            find_sypmtoms()

        case "treatment":

            print(f'{search_req} of the {user_req}: ')
            print(" ")
            flu_info()

        case _:
            print("Sorry we dont have that information right now")
