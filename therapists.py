from bs4 import BeautifulSoup
import requests

def getTherapistProfileLinks(zipcode):

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    page = requests.get('https://www.psychologytoday.com/us/therapists/20001', headers=header)

    soup = BeautifulSoup(page.text, 'html.parser')

    # Full Name, Certifications (listed under the full name on the website)
    # Street, City, State, Zip, Phone Number
    # Additional Address(Street,City, State, Zip, Phone) if applicable
    # Website address, Specialties, Issues, Age focus, Communities, Type of Therapy, Modality, About Summary
    # print(page.text)

    teletherapists = soup.find_all('a', href=True, class_="result-name")

    teletherapyLinks = []

    for teletherapist in teletherapists:
        print(teletherapist['href'])
        teletherapyLinks.append(teletherapist['href'])

    return teletherapyLinks



