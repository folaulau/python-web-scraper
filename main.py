from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from therapists import getTherapistProfileLinks, getNextTherapistProfileLinks
import zipcode




# therapistProfileLink = "https://www.psychologytoday.com/us/therapists/20001/428441?sid=603dcd0e85fdf&ref=1&rec_next=1&p=1"



def readProfileData(sheet, therapistProfileLinks, count):

    for therapistProfileLink in therapistProfileLinks:
        print(therapistProfileLink)
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

        heading = soup.find(class_='row profile-name-phone')

        #print(f'nameAndPhone: {nameAndPhone.prettify()}')

        try:
            fullName = heading.find(attrs={"itemprop": "name"});

            # print(f'FullName: {fullName.text.strip()}')

            sheet[f"A{count}"] = fullName.text.strip()
        except:
            print("Something else went wrong")



        try:
            phone = heading.find(attrs={"id": "phone-click-reveal"});

            # print(f'Phone: {phone.text.strip()}')
            sheet[f"G{count}"] = phone.text.strip()
        except:
            print("Something else went wrong phone")


        profileTitles = heading.find(attrs={"class": "profile-title"})

        profiles = heading.find(attrs={"class": "profile-title"})



        try:
            profiles = profileTitles.select(".nowrap")

            certifications = ""

            for profile in profiles:
                glossary = profile.find(attrs={"data-ui-type": "glossary"})
                # print("glossary")
                # print(glossary.text)
                certifications += glossary.text + ","

            # print(f'certifications {certifications}')

            sheet[f"B{count}"] = certifications
        except:
            print("Something else went wrong certifications")

        ########### profile content #############

        profileContent = soup.find(attrs={"id":"profile-content"})

        #print(f'profileContent: {profileContent.prettify()}')

        detailsColumn = profileContent.find(attrs={"class":"col-xs-12 col-sm-12 col-md-7 col-lg-7 details-column"})

        personalStatementList = profileContent.find(attrs={"class":"section profile-personalstatement"})

        # print(f'personalStatementList: {personalStatementList.prettify()}')

        personalStatements = personalStatementList.select(".statementPara")

        personalStatementsStr = "";

        for statement in personalStatements:
            # print("statement")
            # print(statement.text.strip())
            personalStatementsStr += statement.text.strip()

        try:
            sheet[f"S{count}"] = personalStatementsStr
        except:
            print("Something else went wrong personalStatementsStr")

        #print(f'detailsColumn: {detailsColumn.prettify()}')

        specialtiesColumn = profileContent.find(attrs={"class":"col-xs-12 col-sm-12 col-md-5 col-lg-5 specialties-column"})

        # print(f'specialtiesColumn: {specialtiesColumn}')

        try:
            streetAddress = specialtiesColumn.find(attrs={"itemprop":"streetAddress"}).text.strip()

            # print(f'streetAddress: {streetAddress}')

            sheet[f"C{count}"] = streetAddress
        except:
            print("Something else went wrong url"+therapistProfileLink)






        try:
            addressLocality = specialtiesColumn.find(attrs={"itemprop": "addressLocality"}).text.strip()

            # print(f'addressLocality: {addressLocality}')

            sheet[f"D{count}"] = addressLocality
        except:
            print("Something else went wrong url addressLocality "+therapistProfileLink)




        try:
            addressRegion = specialtiesColumn.find(attrs={"itemprop": "addressRegion"}).text.strip()

            sheet[f"E{count}"] = addressRegion

            # print(f'addressRegion: {addressRegion}')
        except:
            print("Something else went wrong url addressRegion "+therapistProfileLink)


        try:
            postalcode = specialtiesColumn.find(attrs={"itemprop": "postalcode"}).text.strip()

            sheet[f"F{count}"] = postalcode

            # print(f'postalcode: {postalcode}')
        except:
            print("Something else went wrong url postalcode "+therapistProfileLink)


        specialityList = specialtiesColumn.find(attrs={"class":"spec-list attributes-top"})
        #print(f'specialityList: {specialityList.prettify()}')

        try:
            specialities = specialityList.select(".highlight")

            specialitiesStr = ""

            # print(f'specialities: {specialities}')
            for speciality in specialities:
                # print("speciality")
                # print(speciality.text.strip())
                specialitiesStr += speciality.text.strip() + ","

            sheet[f"M{count}"] = specialitiesStr
        except:
            print("Something else went wrong url specialitiesStr "+therapistProfileLink)




        try:
            # issues
            issueList = specialtiesColumn.find(attrs={"class": "spec-list attributes-issues"})
            # print(f'issueList: {issueList.prettify()}')
            issues = issueList.select(".attribute-list > li")

            # print(f'issues: {issues}')
            issuesStr = ""

            for issue in issues:
                # print("issue")
                # print(issue.text.strip())
                issuesStr += issue.text.strip() + ","

            sheet[f"N{count}"] = issuesStr
        except:
            print("Something else went wrong url issues "+therapistProfileLink)



        try:
            # Age focus

            ageList = specialtiesColumn.find(attrs={"class": "spec-list attributes-age-focus"})
            # print(f'ageList: {ageList.prettify()}')
            ages = ageList.select(".attribute-list > li")

            # print(f'ages: {ages}')
            agesStr = ""
            for age in ages:
                # print("age")
                # print(age.text.strip())
                agesStr += age.text.strip()

            sheet[f"O{count}"] = agesStr
        except:
            print("Something else went wrong url agesStr "+therapistProfileLink)



        try:
            # Communities - spec-list attributes-categories
            communityList = specialtiesColumn.find(attrs={"class": "spec-list attributes-categories"})
            # print(f'communityList: {communityList.prettify()}')
            communities = communityList.select(".attribute-list > li")

            # print(f'communities: {communities}')
            communitiesStr = ""
            for community in communities:
                # print("community")
                # print(community.text.strip())
                communitiesStr += community.text.strip() + ","

            sheet[f"P{count}"] = communitiesStr
        except:
            print("Something else went wrong url communitiesStr "+therapistProfileLink)



        try:
            # Type of Therapy - spec-list attributes-treatment-orientation

            therapyTypeList = specialtiesColumn.find(attrs={"class": "spec-list attributes-treatment-orientation"})
            # print(f'therapyTypeList: {therapyTypeList.prettify()}')
            therapyTypes = therapyTypeList.select(".attribute-list > li")

            # print(f'therapyTypes: {therapyTypes}')
            therapyTypesStr = ""
            for therapyType in therapyTypes:
                # print("therapyType")
                # print(therapyType.text.strip())
                therapyTypesStr += therapyType.text.strip() + ","

            sheet[f"Q{count}"] = therapyTypesStr
        except:
            print("Something else went wrong url therapyTypesStr " + therapistProfileLink)




        try:
            # Modality
            modalityList = specialtiesColumn.find(attrs={"class": "spec-list attributes-modality"})
            # print(f'modalityList: {modalityList.prettify()}')
            modalities = modalityList.select(".attribute-list > li")

            # print(f'modalities: {modalities}')
            modalitiesStr = ""
            for modality in modalities:
                # print("modality")
                # print(modality.text.strip())
                modalitiesStr += modality.text.strip() + ","

            sheet[f"R{count}"] = modalitiesStr
        except:
            print("Something else went wrong url therapyTypesStr " + therapistProfileLink)

        sheet[f"T{count}"] = therapistProfileLink
        count+=1
    print(f"count: {count}")
    return count

zipcodes = zipcode.getDCZipcodes();

count = 2;

for zipcode in zipcodes:
    workbook = Workbook()
    sheet = workbook.active
    # columns
    sheet["A1"] = "Full Name"
    sheet["B1"] = "Certifications"
    sheet["C1"] = "Street"
    sheet["D1"] = "City"
    sheet["E1"] = "State"
    sheet["F1"] = "Zip"
    sheet["G1"] = "Phone Number"
    sheet["H1"] = "add2 Street"
    sheet["I1"] = "add2 City"
    sheet["J1"] = "add2 State"
    sheet["K1"] = "add2 Zip"
    sheet["L1"] = "add2 PhoneNumber"

    sheet["M1"] = "Specialties"
    sheet["N1"] = "Issues"
    sheet["O1"] = "Age focus"
    sheet["P1"] = "Communities"
    sheet["Q1"] = "Type Of Therapy"
    sheet["R1"] = "Modality"
    sheet["S1"] = "About Summary"
    sheet["T1"] = "Profile Link"

    providerProfileLinks = getTherapistProfileLinks(zipcode)
    therapistProfileLinks = providerProfileLinks[0]
    nextPageLink = providerProfileLinks[1]
    count = readProfileData(sheet, therapistProfileLinks, count)
    print(f"1count: {count}")

    while len(nextPageLink) > 0:
        providerProfileLinks = getNextTherapistProfileLinks(nextPageLink)
        therapistProfileLinks = providerProfileLinks[0]
        nextPageLink = providerProfileLinks[1]
        count = readProfileData(sheet, therapistProfileLinks, count)
        print(f"2count: {count}")

    workbook.save(filename=zipcode + "_providers.xlsx")
    print(zipcode+" done!")
    count = 2

print("data loading done!")


