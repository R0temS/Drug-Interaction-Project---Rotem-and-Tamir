import requests

def getInfo(drug_rxcui):
    endpoint = "https://api.fda.gov/drug/label.json"
    params = {"search": f"openfda.rxcui:{drug_rxcui}"}

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
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
    else:
        print(f"Error: {response.status_code}")
