import requests
#getInfo function:
#mode "p":  prints basic info about a specific drug
#mode "r":  updates the drugsInfoDic dictionary for a specific drug
#
#updatedrugsinfodic function updates the drugsInfoDic for all of the drugs in the druglist
#
#findLocationInDrugsInfoDic function finds if a info item is available for a specific drug and returns the location. if not found returns -1 
def getInfo(drug_rxcui, mode, drugsinfodic, drugName, loc, listWindow):
    endpoint = "https://api.fda.gov/drug/label.json"
    params = {"search": f"openfda.rxcui:{drug_rxcui}"}

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        if mode == "p":
            try:
                print("INDICATION AND USAGE:  ", end="")
                print(data['results'][0]['indications_and_usage'][0]+ "\n")
            except Exception:
                print("N/A")
            try:
                print("WARNINGS:  ", end="")
                print(data['results'][0]['warnings'][0]+ "\n")
            except Exception:
                print("N/A")
            try:
                print("DOSAGE AND ADMINISTRATION:  ", end="")
                print(data['results'][0]['dosage_and_administration'][0]+ "\n")
            except Exception:
                print("N/A")
            # Process the data, extract dosage information, etc.
        elif mode =="r":
            if len(drugsinfodic)==0:
                drugsinfodic.update({"druginfo": []})
            drugsinfodic['druginfo'].append({"rxcui": drug_rxcui})
            drugsinfodic['druginfo'][loc].update({"drugName": drugName})
            try:
                drugsinfodic['druginfo'][loc].update({"INDICATION AND USAGE": data['results'][0]['indications_and_usage'][0].lower()})
            except Exception:
                drugsinfodic['druginfo'][loc].update({"INDICATION AND USAGE": "N/A"})
            try:
                drugsinfodic['druginfo'][loc].update({"WARNINGS": data['results'][0]['warnings'][0].lower()})
            except Exception:
                drugsinfodic['druginfo'][loc].update({"WARNINGS": "N/A"})
            try:
                drugsinfodic['druginfo'][loc].update({"DOSAGE AND ADMINISTRATION": data['results'][0]['dosage_and_administration'][0].lower()})
            except Exception:
                drugsinfodic['druginfo'][loc].update({"DOSAGE AND ADMINISTRATION": "N/A"})
    else:
        if mode=="p":
            print("NO INFO FOUND")
            

def updatedrugsinfodic(drugsinfodic, druglist):
    loc=0
    for drug in druglist:
        getInfo(drug[1],"r",drugsinfodic, drug[0], loc, "")
        loc=len(drugsinfodic['druginfo'])

def findLocationInDrugsInfoDic(druglist, drugsInfoDic, drugfordelete):
    rxcui = druglist[drugfordelete][1]
    loc=0
    for drug in drugsInfoDic['druginfo']:
        if drug['rxcui'] == rxcui:
            return loc
        loc+=1
    return -1



