#checkAllergy function recieves the drugsInfoDic and patientInfo dictionaries and prints the relevent information from drugsInfoDic that contains the allergy name and the word 'allergy'
#
#checkBackgroundDiesease function recieves the drugsInfoDic and patientInfo dictionaries and prints the relevent information from drugsInfoDic that contains the diesease name
def checkAllergy(drugsInfoDic, patientInfo):
    lst=[]
        
        
    for allergy in patientInfo['Allergies']:
        for drug in drugsInfoDic['druginfo']:
            try:   
                if drug['INDICATION AND USAGE'].find(allergy) != -1 and drug['INDICATION AND USAGE'].find("allergy") != -1:
                    relevant = (drug['INDICATION AND USAGE'])[drug['INDICATION AND USAGE'].find("warnings allergy alert"):]
                    relevant = relevant.split(".")
                    lst.append(f"RELEVANT INDICATION AND USAGE --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{relevant[0]}.{relevant[1]}.\n")
            except Exception:
                pass
            try:
                if drug['WARNINGS'].find(allergy) != -1 and drug['WARNINGS'].find("allergy") != -1:
                    relevant = (drug['WARNINGS'])[drug['WARNINGS'].find("warnings allergy alert"):]
                    relevant = relevant.split(".")
                    lst.append(f"RELEVANT WARNINGS --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{relevant[0]}.{relevant[1]}.\n")
            except Exception:
                pass
            try:
                if drug['DOSAGE AND ADMINISTRATION'].find(allergy) != -1 and drug['DOSAGE AND ADMINISTRATION'].find("allergy") != -1:
                    relevant = (drug['DOSAGE AND ADMINISTRATION'])[drug['DOSAGE AND ADMINISTRATION'].find("warnings allergy alert"):]
                    relevant = relevant.split(".")
                    lst.append(f"RELEVANT DOSAGE AND ADMINISTRATION --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{relevant[0]}.{relevant[1]}.\n")
            except Exception:
                pass
        if len(lst)!=0:
            print("---ITEMS THAT ARE RELEVANT TO ALLERGIES---\n")
            for item in lst:
                print(item)
        else:
            print("NO INFORMATION THAT IS RELEVANT TO BACKGROUND DIESEASES FOUND")

def checkBackgroundDiesease(drugsInfoDic, patientInfo):
    lst=[]
    
    for diesease in patientInfo['Background Dieseases']:
        for drug in drugsInfoDic['druginfo']:
            try:
                if drug['INDICATION AND USAGE'].find(diesease) != -1:
                     relevant = drug['INDICATION AND USAGE'].split(". ")
                     finalsentence=""
                     for sentence in relevant:
                         if sentence.find(diesease)!=-1:
                             finalsentence = finalsentence + sentence.replace(diesease,"   ***"+diesease.upper()+"***   ")+".\n"
                     lst.append(f"RELEVANT INDICATION AND USAGE --- BETWEEN DRUG - {drug['drugName']} - AND DIESEASE - {diesease}\n\n{relevant}\n")
            except Exception:
                pass
            try:
                if drug['WARNINGS'].find(diesease) != -1:
                    relevant = drug['WARNINGS'].split(". ")
                    finalsentence=""
                    for sentence in relevant:
                        if sentence.find(diesease)!=-1:
                            finalsentence = finalsentence + sentence.replace(diesease,"   ***"+diesease.upper()+"***   ")+".\n"
                    lst.append(f"RELEVANT WARNINGS --- BETWEEN DRUG - {drug['drugName']} - AND DIESEASE - {diesease}\n\n{finalsentence}\n")
            except Exception:
                pass
            try:
                if drug['DOSAGE AND ADMINISTRATION'].find(diesease) != -1:
                     relevant = drug['DOSAGE AND ADMINISTRATION'].split(". ")
                     finalsentence=""
                     for sentence in relevant:
                         if sentence.find(diesease)!=-1:
                             finalsentence = finalsentence + sentence.replace(diesease,"   ***"+diesease.upper()+"***   ")+".\n"
                     lst.append(f"RELEVANT DOSAGE AND ADMINISTRATION --- BETWEEN DRUG - {drug['drugName']} - AND DIESEASE - {diesease}\n\n{relevant}\n")
            except Exception:
                pass
        if len(lst)!=0:
            print("---ITEMS THAT ARE RELEVANT TO BACKGROUND DIESEASES---\n")
            for item in lst:
                print(item)
        else:
            print("NO INFORMATION THAT IS RELEVANT TO BACKGROUND DIESEASES FOUND")

        
        