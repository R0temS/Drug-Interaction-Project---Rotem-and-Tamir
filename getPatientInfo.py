def getPatientInfo(patientInfo):
    patientInfo.update({'Name':input("Enter your name: ")})
    patientInfo.update({'Age':int(input("Enter your age: "))})
    allergy = "a"
    while allergy!="":
        if patientInfo.get('Allergies') == None:
            allergy= input("Enter substances you are allergic to: ").lower()
            if allergy !="":
                patientInfo.update({'Allergies':[allergy]})
        else:
            allergy= input("Enter substances you are allergic to: ").lower()
            if allergy !="":
                patientInfo['Allergies'].append(allergy)
    
    backgroundDisease = "a"
    while backgroundDisease!="":
        if patientInfo.get('Background Dieseases') == None:
            backgroundDisease= input("Enter your background Diseases: ").lower()
            if backgroundDisease!="":
                patientInfo.update({'Background Dieseases':[backgroundDisease]})
        else:
            backgroundDisease= input("Enter your background Diseases: ").lower()
            if backgroundDisease !="":
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
        