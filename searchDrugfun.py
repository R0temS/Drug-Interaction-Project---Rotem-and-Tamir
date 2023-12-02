import requests as req
import os

#searchDrug function checks if a drug exists in the Api and adds it to the drug list
#checkforduplicate function checks if a specific drug is already exist in the druglist, if so it returns True, else it returns False
def searchDrug(alldrugs):
    
    drugSearch = 'a'
    while drugSearch != "":
        
        drugSearch = input("drug to search for (press enter to return to menu)--- ").lower()
        os.system('cls')

        if drugSearch == "":
            break
    
        str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
        data = req.get(str).json()
    
    
        if (len(data['drugGroup']) != 2):
            str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + drugSearch
            data =req.get(str).json()
            if (len(data['suggestionGroup']['suggestionList']) != 0):
                drugSearch = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
                str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
                data = req.get(str).json()
            else:
                str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
                data = req.get(str).json()
                if (len(data['drugGroup']) != 2):
                    print("\nNO DATA FOUND!\n")
        elif (len(data['drugGroup']) == 2):
            for i in data['drugGroup']['conceptGroup']:
        
                 if (i['tty'] == 'SBD' and len(i) >1):
                    count = 1
                    print(f"Options available for {drugSearch}:\n")
                    for j in i['conceptProperties']:
                         print(count ,end="")
                         print(". " ,end="")
                         print(j['name'] ,end="")
                         print("  rxcui - " ,end="")
                         print(j['rxcui'])
                         count +=1
                    
                    try:
                        choice = int(input ("\nWhich of the products: "))-1
                        os.system('cls')
                    except Exception:
                        print("Only a number!")
                        continue
                    if(choice>=0 and choice< count-1):
                        if checkforduplicate(i['conceptProperties'][choice]['rxcui'], alldrugs) == False:
                            alldrugs.append([i['conceptProperties'][choice]['name'],i['conceptProperties'][choice]['rxcui']])
                    else:
                        print("Choice out of range")
                    
        else:    
            print("\nNO DATA FOUND!\n")
    return alldrugs

def checkforduplicate(rxcui, druglist):
    for drug in druglist:
        if rxcui == drug[1]:
            return True
    return False

