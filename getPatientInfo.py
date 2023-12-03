from re import T
import requests as req
#getPatientInfo function recieves the folowing info:
#-Name
#-Age
#-A list of allergies
#-A list of background diseases

#showPatientInfo function shows all of the information described above from the patientInfo dictionary
def getPatientInfo(patientInfo):
    patientInfo.update({'Name':input("Enter your name: ").capitalize()})
    age="a"
    while age=="a":
        try:
            age = int(input("Enter your age: "))
            patientInfo.update({'Age':age})
        except Exception:
            print("\nENTER ONLY INTEGERS!\n")
    allergy = "a"
    while allergy!="":
        if patientInfo.get('Allergies') == None:
            allergy= input("Enter substances you are allergic to (leave empty to continue): ").lower()
            if allergy !="":
                str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + allergy
                data =req.get(str).json()
                if (len(data['suggestionGroup']['suggestionList']) == 1):
                    allergy = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
                else:
                    print("\nSUBSTANCE NOT FOUND!\n")
                    allergy="N/A"
            if allergy !="" and allergy!="N/A":
                patientInfo.update({'Allergies':[allergy]})
        elif allergy!="":
            allergy= input("Enter substances you are allergic to (leave empty to continue): ").lower()
            if allergy !="":
                str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + allergy
                data =req.get(str).json()
                if (len(data['suggestionGroup']['suggestionList']) != 0):
                        allergy = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
                else:
                        print("\nSUBSTANCE NOT FOUND!\n")
                        allergy="N/A"
                if allergy !="" and allergy!="N/A":
                    if checkForDuplicatePatientInfo("allergy", allergy, patientInfo) == False:
                        patientInfo['Allergies'].append(allergy)
    
    backgroundDisease = "a"
    while backgroundDisease!="":
        if patientInfo.get('Background Dieseases') == None:
            backgroundDisease= input("Enter your background Dieseases (leave empty to continue): ").lower()
            if backgroundDisease!="":
                patientInfo.update({'Background Dieseases':[backgroundDisease]})
        else:
            backgroundDisease= input("Enter your background Dieseases (leave empty to continue): ").lower()
            if backgroundDisease !="":
                if checkForDuplicatePatientInfo("background", backgroundDisease, patientInfo) == False:
                    patientInfo['Background Dieseases'].append(backgroundDisease)

def showPatientInfo(patientInfo):
    if patientInfo.get("Age")!=None:
        print(f"\nThe age of {patientInfo['Name']} is {patientInfo['Age']}")
    if patientInfo.get("Allergies")!=None:
        print(f"{patientInfo['Name']} has alergies to:")
        for allergy in patientInfo['Allergies']:
            print("- "+allergy)
        print("")
    if patientInfo.get("Background Dieseases")!=None:
        print(f"{patientInfo['Name']} has the following background dieseases:")
        for brd in patientInfo['Background Dieseases']:
            print("- "+brd)
        print("")

def checkForDuplicatePatientInfo(mode, item, patientInfo):
    if mode == "allergy":
        for x in patientInfo['Allergies']:
            if x == item:
                return True
    elif mode == "background":
        for x in patientInfo['Background Dieseases']:
            if x == item:
                return True

    return False