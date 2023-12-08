from tkinter import *
from tkinter import messagebox
import requests as req
# drugInteraction function recieves the druglist and prints all of the drug interactions
def checkInteractionDup(interactionlist, text):
    for texts in interactionlist:
        if text == texts:
            return True

    return False

def drugInteraction(alldrugs):
    adress = "https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis="
    if len(alldrugs) != 0:
        if len(alldrugs)>0:
            for i in alldrugs:
                adress = adress+i[1]+"+"
        adress = adress[:-1]
        data = req.get(adress).json()


        if (len(data)>1):
            listWindow = Tk()
            listWindow.configure(bg='white')
            headline= Label(listWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG INTERACTIONS-----")
            textbox = Label(listWindow, bg= 'white', font=('Ariel', 14), padx=20, pady=10, justify='left')
            text=""
            finaltext = ""
            count = 1
            interactionlist = []
            for i in data['fullInteractionTypeGroup']:
                for j in i['fullInteractionType'][0]['interactionPair']:
                    text =  ". " + "SEVERITY: " + j['severity']+"\n"+ "    DESCRIPTION: "+ j['description']+"\n"
                    if checkInteractionDup(interactionlist, text) == False:
                        interactionlist.append(text)
                        
                        
            for texts in interactionlist:
                finaltext = finaltext +"\n" + str(count) + texts
                count+=1
            textbox.configure(text=finaltext)
            headline.pack(anchor='n')
            textbox.pack(anchor='nw')
            listWindow.mainloop()
        else:
            messagebox.showerror(title="no interactions found", message="No interactions found!")
    else:
        messagebox.showerror(title="no drugs found", message="Insert drugs first!")
