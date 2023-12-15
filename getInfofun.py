import requests
from updateDB import *
from tkinter import *
from tkinter import messagebox
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

    try:
        response = requests.get(endpoint, params=params)
    except Exception:
        messagebox.showerror(title="Search alert",message="COULD NOT CONNECT, CHECK YOUR INTERNET CONNECTION!")
        return
    

    if response.status_code == 200:
        data = response.json()
        if mode == "p":
            
            text="\nINDICATION AND USAGE:  "
            try:
                text= text+ data['results'][0]['indications_and_usage'][0]+ "\n"
            except Exception:
                text= text+ "N/A"
            text= text+ "\nWARNINGS:  "
            try:
                
                text= text+ data['results'][0]['warnings'][0]+ "\n"
            except Exception:
                text= text+ "N/A"
            text= text+ "\nDOSAGE AND ADMINISTRATION:  "
            try:
                
                text= text+ data['results'][0]['dosage_and_administration'][0]+ "\n"
            except Exception:
                text= text+ "N/A"
            # Process the data, extract dosage information, etc.
            infoWindow=Tk()
            infoWindow.configure(bg='white')
            headline=Label(infoWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG INFO-----")
            headline.grid(row=0, column=0)
            text1=Text(infoWindow, font=('Ariel', 12), width=120, wrap=WORD, padx=20, pady=20)
            text1.insert(1.0, text)
            text1.grid(row=1, column=0)
            back = Button(infoWindow,
                        text="Back to menu",
                        command = lambda: infoWindow.destroy(),
                        font=("Comic Sans", 20),
                        fg="White",
                        background="#20A5C9",
                        activebackground="#20A5C1",
                        activeforeground="White",
                        state=ACTIVE,
                        compound='bottom',
                        padx=10,
                        pady=10, width=25) 
            back.grid(row=3, column=0)

            listWindow.destroy()
            infoWindow.mainloop()
            
        
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
            messagebox.showinfo(title='Alert', message="NO INFO FOUND!")
            

def updatedrugsinfodic(drugsinfodic, druglist):
    loc=0
    for drug in druglist:
        getInfo(drug[1],"r",drugsinfodic, drug[0], loc, "")
        loc=len(drugsinfodic['druginfo'])
    ##drugsinfodic updated
    updateDB("", drugsinfodic, "", "", "druginfo")

def findLocationInDrugsInfoDic(druglist, drugsInfoDic, drugfordelete):
    rxcui = druglist[drugfordelete][1]
    loc=0
    for drug in drugsInfoDic['druginfo']:
        if drug['rxcui'] == rxcui:
            return loc
        loc+=1
    return -1
