import requests as req
import os

def searchDrug(alldrugs):
    drugSearch = 'a'
    while drugSearch != "":
        drugSearch = input("drug to search for (press enter to return to menu)--- ").lower()
    
        if drugSearch == "":
            break
    
        str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
        data = req.get(str).json()
    
    
        if (len(data['drugGroup']) != 2 ):
            str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + drugSearch
            data =req.get(str).json()
            if (len(data['suggestionGroup']['suggestionList']) == 1):
                drugSearch = data['suggestionGroup']['suggestionList']['suggestion'][0]
                str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
                data = req.get(str).json()
            else:
                str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
                data = req.get(str).json()
    
        if (len(data['drugGroup']) == 2):
            for i in data['drugGroup']['conceptGroup']:
        
                 if (i['tty'] == 'SBD' and len(i) >1):
                    count = 1
                    for j in i['conceptProperties']:
                         print(count ,end="")
                         print(". " ,end="")
                         print(j['name'] ,end="")
                         print("  rxcui - " ,end="")
                         print(j['rxcui'])
                         count +=1
                    
                    try:
                        choice = int(input ("Which of the products: "))-1
                    except Exception:
                        print("Only a number!")
                        continue
                    if(choice>=0 and choice<= count-1):
                        if checkforduplicate(i['conceptProperties'][choice]['rxcui'], alldrugs) == False:
                            alldrugs.append([i['conceptProperties'][choice]['name'],i['conceptProperties'][choice]['rxcui']])
                    else:
                        print("Choice out of range")
                    os.system('cls')

        

        else:
            print("NO DATA FOUND!")
    return alldrugs

def checkforduplicate(rxcui, druglist):
    for drug in druglist:
        if rxcui == drug[1]:
            return True
    return False

