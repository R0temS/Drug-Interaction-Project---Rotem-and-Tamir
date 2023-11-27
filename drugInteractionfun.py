import requests as req

def drugInteraction(alldrugs):
    str = "https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis="
    if len(alldrugs)>0:
        for i in alldrugs:
            str = str+i[1]+"+"
    str = str[:-1]
    data = req.get(str).json()


    if (len(data)>1):
        for i in data['fullInteractionTypeGroup']:
            for j in i['fullInteractionType'][0]['interactionPair']:
                print("")
                print("SEVERITY: ", end="")
                print(j['severity'])
                print("DESCRIPTION: ", end="")
                print (j['description'])
            
    else:
        print("No Interactions Found!")
