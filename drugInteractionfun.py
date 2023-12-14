from tkinter import *
from tkinter import messagebox
import requests as req
# drugInteraction function recieves the druglist and prints all of the drug interactions
def checkInteractionDup(interactionlist, text):
    for texts in interactionlist:
        if text == texts:
            return True

    return False

def drugInteraction(alldrugs, window):
    adress = "https://rxnav.nlm.nih.gov/REST/interaction/list.json?rxcuis="
    if len(alldrugs) != 0:
        if len(alldrugs)>0:
            for i in alldrugs:
                adress = adress+i[1]+"+"
        adress = adress[:-1]
        data = req.get(adress).json()


        if (len(data)>1):
            text=""
            finaltext = ""
            count = 1
            interactionlist = []
            for i in data['fullInteractionTypeGroup']:
                for j in i['fullInteractionType'][0]['interactionPair']:
                    text =  ". " + "SEVERITY: " + j['severity']+"\n"+ "    DESCRIPTION: "+ j['description']+"\n"
                    if checkInteractionDup(interactionlist, text) == False:
                        interactionlist.append(text)
                        
            infoWindow=Tk()
            infoWindow.configure(bg='white')
            headline=Label(infoWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG INTERACTIONS-----")
            headline.grid(row=0, column=0)
            text1=Text(infoWindow, font=('Ariel', 12), width=120, wrap=WORD, padx=20, pady=20)
            for texts in interactionlist:
                finaltext = finaltext +"\n" + str(count) + texts
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
        else:
            messagebox.showerror(title="no interactions found", message="No interactions found!")
    else:
        messagebox.showerror(title="no drugs found", message="Insert drugs first!")
