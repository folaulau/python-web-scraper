from bs4 import BeautifulSoup
import requests
from therapists import getTherapistProfileLinks

zipcode = "20001";
therapistProfileLinks = getTherapistProfileLinks(zipcode)

for therapistProfileLink in therapistProfileLinks:
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    page = requests.get(therapistProfileLink, headers=header)

    soup = BeautifulSoup(page.text, 'html.parser')

    profileContainer = soup.find(id='profileContainer')

    print(f'profileContainer: {profileContainer}')

    tel = soup.find(id='phone-click-reveal')

    print(f'phone: {tel.text}')

    tel = soup.find(itemprop='phone-click-reveal')

    print(f'phone: {tel.text}')


    break

