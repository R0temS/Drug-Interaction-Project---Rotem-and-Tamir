import requests

def getInfo(drug_rxcui, mode, drugsinfodic):
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
            drugsinfodic.update({"druginfo": {}})
            drugsinfodic['druginfo'].update({"rxcui": drug_rxcui})
            try:
                drugsinfodic['druginfo'].update({"INDICATION AND USAGE": data['results'][0]['indications_and_usage'][0]})
            except Exception:
                drugsinfodic['druginfo'].update({"INDICATION AND USAGE": "N/A"})
            try:
                drugsinfodic['druginfo'].update({"WARNINGS": data['results'][0]['warnings'][0]})
            except Exception:
                drugsinfodic['druginfo'].update({"WARNINGS": "N/A"})
            try:
                drugsinfodic['druginfo'].update({"DOSAGE AND ADMINISTRATION": data['results'][0]['dosage_and_administration'][0]})
            except Exception:
                drugsinfodic['druginfo'].update({"DOSAGE AND ADMINISTRATION": "N/A"})
    else:
        print(f"Error: {response.status_code}")
