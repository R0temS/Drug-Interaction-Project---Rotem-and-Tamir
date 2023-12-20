import threading
from tkinter import *
from tkinter import messagebox
import threading
import time

#checkAllergy function recieves the drugsInfoDic and patientInfo dictionaries and prints the relevent information from drugsInfoDic that contains the allergy name and the word 'allergy'
#
#checkBackgroundDiesease function recieves the drugsInfoDic and patientInfo dictionaries and prints the relevent information from drugsInfoDic that contains the diesease name
def checkAllergy(drugsInfoDic, patientInfo, window):
    lst=[]
        
    try:    
        for allergy in patientInfo['Allergies']:
            for drug in drugsInfoDic['druginfo']:
                try:   
                    if drug['INDICATION AND USAGE'].find(allergy) != -1 and drug['INDICATION AND USAGE'].find("allergy") != -1:
                        finalsentence=""
                        if drug['INDICATION AND USAGE'].find("warnings allergy alert") != -1:
                            relevant = (drug['INDICATION AND USAGE'])[drug['INDICATION AND USAGE'].find("warnings allergy alert"):]
                            relevant = relevant.split(".")
                            finalsentence = str(relevant[0])+"."+str(relevant[1])+".\n"
                        else:
                            relevant = drug['INDICATION AND USAGE'].split(". ")
                            for sentence in relevant:
                                if sentence.find(allergy)!=-1:
                                    finalsentence = finalsentence + sentence.replace(allergy,"   ***"+allergy.upper()+"***   ")+".\n"
                        lst.append(f"RELEVANT INDICATION AND USAGE --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{finalsentence}\n")
                except Exception:
                    pass
                try:
                    if drug['WARNINGS'].find(allergy) != -1 and drug['WARNINGS'].find("allergy") != -1:
                        finalsentence=""
                        if drug['WARNINGS'].find("warnings allergy alert") != -1:
                            relevant = (drug['WARNINGS'])[drug['WARNINGS'].find("warnings allergy alert"):]
                            relevant = relevant.split(".")
                            finalsentence = str(relevant[0])+"."+str(relevant[1])+".\n"
                        else:
                            relevant = drug['WARNINGS'].split(". ")
                            for sentence in relevant:
                                if sentence.find(allergy)!=-1:
                                    finalsentence = finalsentence + sentence.replace(allergy,"   ***"+allergy.upper()+"***   ")+".\n"
                        lst.append(f"RELEVANT WARNINGS --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{finalsentence}\n")
                except Exception:
                    pass
                try:
                    if drug['DOSAGE AND ADMINISTRATION'].find(allergy) != -1 and drug['DOSAGE AND ADMINISTRATION'].find("allergy") != -1:
                        finalsentence=""
                        if drug['DOSAGE AND ADMINISTRATION'].find("warnings allergy alert") != -1:
                            relevant = (drug['DOSAGE AND ADMINISTRATION'])[drug['DOSAGE AND ADMINISTRATION'].find("warnings allergy alert"):]
                            relevant = relevant.split(".")
                            finalsentence = str(relevant[0])+"."+str(relevant[1])+".\n"
                        else:
                            relevant = drug['DOSAGE AND ADMINISTRATION'].split(". ")
                            for sentence in relevant:
                                if sentence.find(allergy)!=-1:
                                    finalsentence = finalsentence + sentence.replace(allergy,"   ***"+allergy.upper()+"***   ")+".\n"
                        lst.append(f"RELEVANT DOSAGE AND ADMINISTRATION --- BETWEEN DRUG - {drug['drugName']} - AND SUBSTANCE - {allergy}\n\n{finalsentence}\n")
                except Exception:
                    pass
        if len(lst)!=0:
            infoWindow=Tk()
            infoWindow.configure(bg='white')
            headline=Label(infoWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="---ITEMS THAT ARE RELEVANT TO ALLERGIES---")
            headline.grid(row=0, column=0)
            text1=Text(infoWindow, font=('Ariel', 12), width=120, wrap=WORD, padx=20, pady=20)
            text=""
            for item in lst:
                text = text + item
            
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
            window.destroy()
            infoWindow.mainloop()            
        else:
                messagebox.showinfo(title="Alert",message="NO INFORMATION THAT IS RELEVANT TO ALLERGIES WAS FOUND")
    except Exception:
        messagebox.showinfo(title="Alert",message="NO ALLERGIES IN THE LIST!")

def checkBackgroundDiesease(drugsInfoDic, patientInfo, window):
    lst=[]
    try:
        for diesease in patientInfo['Background Dieseases']:
            for drug in drugsInfoDic['druginfo']:
                try:
                    if drug['INDICATION AND USAGE'].find(diesease) != -1:
                         relevant = drug['INDICATION AND USAGE'].split(". ")
                         finalsentence=""
                         for sentence in relevant:
                             if sentence.find(diesease)!=-1:
                                 finalsentence = finalsentence + sentence.replace(diesease,"   ***"+diesease.upper()+"***   ")+".\n"
                         lst.append(f"RELEVANT INDICATION AND USAGE --- BETWEEN DRUG - {drug['drugName']} - AND DIESEASE - {diesease}\n\n{relevant}\n")
                except Exception:
                    pass
                try:
                    if drug['WARNINGS'].find(diesease) != -1:
                        relevant = drug['WARNINGS'].split(". ")
                        finalsentence=""
                        for sentence in relevant:
                            if sentence.find(diesease)!=-1:
                                finalsentence = finalsentence + sentence.replace(diesease,"   ***"+diesease.upper()+"***   ")+".\n"
                        lst.append(f"RELEVANT WARNINGS --- BETWEEN DRUG - {drug['drugName']} - AND DIESEASE - {diesease}\n\n{finalsentence}\n")
                except Exception:
                    pass
                try:
                    if drug['DOSAGE AND ADMINISTRATION'].find(diesease) != -1:
                         relevant = drug['DOSAGE AND ADMINISTRATION'].split(". ")
                         finalsentence=""
                         for sentence in relevant:
                             if sentence.find(diesease)!=-1:
                                 finalsentence = finalsentence + sentence.replace(diesease,"   ***"+diesease.upper()+"***   ")+".\n"
                         lst.append(f"RELEVANT DOSAGE AND ADMINISTRATION --- BETWEEN DRUG - {drug['drugName']} - AND DIESEASE - {diesease}\n\n{relevant}\n")
                except Exception:
                    pass
        if len(lst)!=0:
            infoWindow=Tk()
            infoWindow.configure(bg='white')
            headline=Label(infoWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="---ITEMS THAT ARE RELEVANT TO BACKGROUND DIESEASES---")
            headline.grid(row=0, column=0)
            text1=Text(infoWindow, font=('Ariel', 12), width=120, wrap=WORD, padx=20, pady=20)
            text=""
            for item in lst:
                text = text + item
            
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
            window.destroy()
            infoWindow.mainloop()            
        else:
                messagebox.showinfo(title="Alert",message="NO INFORMATION THAT IS RELEVANT TO BACKGROUND DIESEASES WAS FOUND")
    except Exception:
        messagebox.showinfo(title="Alert",message="NO BACKGROUND DIESEASES IN THE LIST!")

# Creating a thread of loading window
  
def loading(event):
   
    def timer(event, Text):
        count = 0
        
        while not event.is_set():
            time.sleep(1)
            if count == 0:
                 Text.config(text="LOADING.")
                 count += 1
            elif count == 1:
                 Text.config(text="LOADING..")
                 count += 1
            elif count == 2:
                Text.config(text="LOADING...")
                count = 0
        
        
    
    waitingWindow = Tk()
    Text = Label(waitingWindow, text="LOADING",
                     bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center')
    Text.pack()
    loading_thread = threading.Thread(target= lambda: timer(event, Text), daemon=True) # loading
    loading_thread.start()  # loading
    
    waitingWindow.mainloop() 
    
    
    
        
        
