#checkAllergy function recieves the drugsInfoDic and patientInfo dictionaries and prints the relevent information from drugsInfoDic that contains the allergy name and the word 'allergy'
def checkAllergy(drugsInfoDic, patientInfo):
    lst=[]
    try:
        
        
        for allergy in patientInfo['Allergies']:
            for drug in drugsInfoDic['druginfo']:
                if drug['INDICATION AND USAGE'].find(allergy) != -1 and drug['INDICATION AND USAGE'].find("allergy") != -1:
                    relevant = (drug['INDICATION AND USAGE'])[drug['INDICATION AND USAGE'].find("warnings allergy alert"):]
                    relevant = relevant.split(".")
                    lst.append(f"RELEVANT INDICATION AND USAGE --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{relevant[0]}.{relevant[1]}.\n")
                if drug['WARNINGS'].find(allergy) != -1 and drug['WARNINGS'].find("allergy") != -1:
                    relevant = (drug['WARNINGS'])[drug['WARNINGS'].find("warnings allergy alert"):]
                    relevant = relevant.split(".")
                    lst.append(f"RELEVANT WARNINGS --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{relevant[0]}.{relevant[1]}.\n")
                if drug['DOSAGE AND ADMINISTRATION'].find(allergy) != -1 and drug['DOSAGE AND ADMINISTRATION'].find("allergy") != -1:
                    relevant = (drug['DOSAGE AND ADMINISTRATION'])[drug['DOSAGE AND ADMINISTRATION'].find("warnings allergy alert"):]
                    relevant = relevant.split(".")
                    lst.append(f"RELEVANT DOSAGE AND ADMINISTRATION --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{relevant[0]}.{relevant[1]}.\n")
        if len(lst)!=0:
            print("---ITEMS THAT ARE RELEVANT TO ALLERGIES---\n")
            for item in lst:
                print(item)
    except Exception:
        print("NO ALLERGIES")


        