from bs4 import BeautifulSoup
import requests
from therapists import getTherapistProfileLinks

zipcode = "20001";
therapistProfileLinks = getTherapistProfileLinks(zipcode)

#therapistProfileLink = therapistProfileLinks[0]

therapistProfileLink = "https://www.psychologytoday.com/us/therapists/20001/428441?sid=603dcd0e85fdf&ref=1&rec_next=1&p=1"

print(f'therapistProfileLink: {therapistProfileLink}')

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
}

page = requests.get(therapistProfileLink, headers=header)

soup = BeautifulSoup(page.text, 'html.parser')

# Full Name

# Certifications (listed under the full name on the website)

# Street, City, State, Zip, Phone Number

# Additional Address(Street,City, State, Zip, Phone) if applicable

# Website address
# Specialties, Issues, Age focus, Communities, Type of Therapy, Modality, About Summary

########### Fullname, certifications #############

nameAndPhone = soup.find(class_='row profile-name-phone')

#print(f'nameAndPhone: {nameAndPhone.prettify()}')

fullName = nameAndPhone.find(attrs={"itemprop":"name"});

print(f'FullName: {fullName.text.strip()}')

phone = nameAndPhone.find(attrs={"id":"phone-click-reveal"});

print(f'Phone: {phone.text.strip()}')

profileTitles = nameAndPhone.find(attrs={"class":"profile-title"})

profiles = nameAndPhone.find(attrs={"class":"profile-title"})

profiles = profileTitles.select(".nowrap")

certifications=[];

for profile in profiles:
    glossary = profile.find(attrs={"data-ui-type":"glossary"})
    #print("glossary")
    #print(glossary.text)
    certifications.append(glossary.text)

print(f'certifications {certifications}')

########### profile content #############

profileContent = soup.find(attrs={"id":"profile-content"})

#print(f'profileContent: {profileContent.prettify()}')

detailsColumn = profileContent.find(attrs={"class":"col-xs-12 col-sm-12 col-md-7 col-lg-7 details-column"})

#print(f'detailsColumn: {detailsColumn.prettify()}')

specialtiesColumn = profileContent.find(attrs={"class":"col-xs-12 col-sm-12 col-md-5 col-lg-5 specialties-column"})

print(f'specialtiesColumn: {specialtiesColumn}')

streetAddress = specialtiesColumn.find(attrs={"itemprop":"streetAddress"}).text.strip()

print(f'streetAddress: {streetAddress}')

addressLocality = specialtiesColumn.find(attrs={"itemprop":"addressLocality"}).text.strip()

print(f'addressLocality: {addressLocality}')

addressRegion = specialtiesColumn.find(attrs={"itemprop":"addressRegion"}).text.strip()

print(f'addressRegion: {addressRegion}')

postalcode = specialtiesColumn.find(attrs={"itemprop":"postalcode"}).text.strip()

print(f'postalcode: {postalcode}')

specialityList = specialtiesColumn.find(attrs={"class":"spec-list attributes-top"})
#print(f'specialityList: {specialityList.prettify()}')
specialities = specialityList.select(".highlight")
#print(f'specialities: {specialities}')
for speciality in specialities:
    print("speciality")
    print(speciality.text.strip())

# issues
issueList = specialtiesColumn.find(attrs={"class":"spec-list attributes-issues"})
print(f'issueList: {issueList.prettify()}')
issues = issueList.select(".attribute-list > li")

#print(f'issues: {issues}')

for issue in issues:
    print("issue")
    print(issue.text.strip())

#Age focus

ageList = specialtiesColumn.find(attrs={"class":"spec-list attributes-age-focus"})
print(f'ageList: {ageList.prettify()}')
ages = ageList.select(".attribute-list > li")

#print(f'ages: {ages}')

for age in ages:
    print("age")
    print(age.text.strip())

#Communities - spec-list attributes-categories
communityList = specialtiesColumn.find(attrs={"class":"spec-list attributes-categories"})
print(f'communityList: {communityList.prettify()}')
communities = communityList.select(".attribute-list > li")

#print(f'communities: {communities}')

for community in communities:
    print("community")
    print(community.text.strip())



#Type of Therapy - spec-list attributes-treatment-orientation

therapyTypeList = specialtiesColumn.find(attrs={"class":"spec-list attributes-treatment-orientation"})
print(f'therapyTypeList: {therapyTypeList.prettify()}')
therapyTypes = therapyTypeList.select(".attribute-list > li")

#print(f'therapyTypes: {therapyTypes}')

for therapyType in therapyTypes:
    print("therapyType")
    print(therapyType.text.strip())

#Modality
modalityList = specialtiesColumn.find(attrs={"class":"spec-list attributes-modality"})
print(f'modalityList: {modalityList.prettify()}')
modalities = modalityList.select(".attribute-list > li")

#print(f'modalities: {modalities}')

for modality in modalities:
    print("modality")
    print(modality.text.strip())