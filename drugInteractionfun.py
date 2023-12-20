# 17/12 - imported the updateDB module in order to update the warning list after maping the interactions in the drug list.
# also added the pre window when clicking on the warnings button in the GUI window. added submit button and function.
from ast import Try
from asyncio import events
import re
from tkinter import *
from tkinter import messagebox
from token import COMMA
import requests as req
from updateDB import * 
from checkallergyandbrd import *

# drugInteraction function recieves the druglist and prints all of the drug interactions
def checkInteractionDup(interactionlist, text):
    for texts in interactionlist:
        if text == texts:
            return True

    return False

def submit(finalList, chooseDrugsWindow, window, mode, warningList, listbox, event):
    for index in listbox.curselection():
        #finalList.append(re.search("^The.*Spain$", (listbox.get(index)), listbox.get(index)[-7:]))
        finalList.append([re.search(".*!", (listbox.get(index))).group()[:-1], re.search("!.*", (listbox.get(index))).group()[2:]])
  
    chooseDrugsWindow.destroy()
    loading(event)
   
    
    drugInteraction(finalList, window, "print", warningList)
    
   
   
def drugInteraction(alldrugs, window, mode, warningList):
    
    if mode == "choose":

        # new window for the user to pick the relevant drugs for interactions
        chooseDrugsWindow = Tk()
        listbox = Listbox(chooseDrugsWindow,
                            selectmode="multiple",
                            bg='white', 
                            font=('Ariel', 18),
                            width=12
                            )
        listbox.pack()
        count = 1
        finalList = []
        for drug in alldrugs:
            listbox.insert(count, f"{drug[0]}! {drug[1]}") 
            count += 1
        event = threading.Event() # loading
        submitButton = Button(chooseDrugsWindow, text="submit", command=lambda: submit(finalList, chooseDrugsWindow, window, "", warningList, listbox, event))
        submitButton.pack()     
        chooseDrugsWindow.mainloop() 
    if mode == "print":
            try:
                event.set() # loading
            except Exception:
                pass    
            flag = False
            interactionlist = []  
            adress = "https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis="
            if len(alldrugs) >=2:
                   
                    for location1 in range(0, len(alldrugs)-1):
                    
                        for location2 in range(location1+1, len(alldrugs)):
                                    adress = adress+alldrugs[location1][1]+"+"+alldrugs[location2][1]
                                    data = req.get(adress).json()
        
                                    if (len(data)>1):
                                        flag = True
        
                                        finaltext = ""
                                        count = 1
                                        for i in data['fullInteractionTypeGroup']:
                                            for j in i['fullInteractionType'][0]['interactionPair']:
                                                text=f"--- Interaction between: {alldrugs[location1][0]} and {alldrugs[location2][0]} ---\n\n"
                                                text = text + "SEVERITY: " + j['severity']+"\n"+ "DESCRIPTION: "+ j['description']+"\n------------------------------------\n\n"
                                                if checkInteractionDup(interactionlist, text) == False:
                                                    interactionlist.append(text)
                                    
                    if (flag == False):
                      messagebox.showerror(title="no interactions found", message="No interactions found!")             
                    else:
                        #new window for showing interactions
                        
                        infoWindow=Tk()
                        infoWindow.configure(bg='white')
                        headline=Label(infoWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG INTERACTIONS-----")
                        headline.grid(row=0, column=0)
                        text1=Text(infoWindow, font=('Ariel', 12), width=120, wrap=WORD, padx=20, pady=20)
                        for texts in interactionlist:
                            finaltext = finaltext +"\n" + texts
                            count+=1
                        text1.insert(1.0, finaltext)
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
                        window.destroy()
                        infoWindow.mainloop()                   
                                         
            elif (len(alldrugs)==1):
                messagebox.showerror(title="NUMBER OF DRUGS", message="Need a minimun of 2 drugs!")
            else:
                messagebox.showerror(title="no drugs found", message="Insert drugs first!")
                
    elif mode == "update":
            flag = False
            interactionlist = []  
            adress = "https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis="
            if len(alldrugs) >=2:
                   
                    for location1 in range(0, len(alldrugs)-1):
                    
                        for location2 in range(location1+1, len(alldrugs)):
                                    adress = adress+alldrugs[location1][1]+"+"+alldrugs[location2][1]
                                    data = req.get(adress).json()
        
                                    if (len(data)>1):
                                        
                                        count = 1
                                        for i in data['fullInteractionTypeGroup']:
                                            for j in i['fullInteractionType'][0]['interactionPair']:
                                                text =  "SEVERITY: " + j['severity']+"\n"+ "DESCRIPTION: "+ j['description']
                                                if checkInteractionDup(interactionlist, text) == False:
                                                    if(j['severity']!= 'N/A'):
                                                        warningList.append([alldrugs[location1][0], alldrugs[location1][1], alldrugs[location2][0], alldrugs[location2][1]])
                                                    interactionlist.append(text)
                                                   
                    updateDB("", "", "", "", warningList, warningList)   # updating the DB                                     
                         
                                      
                                         
          
