import requests as req
import os
from tkinter import *
from tkinter import messagebox
from menu import *

#searchDrug function checks if a drug exists in the Api and adds it to the drug list
#checkforduplicate function checks if a specific drug is already exist in the druglist, if so it returns True, else it returns False
def searchDrug(alldrugs):
    def skip():
        drugWindow.destroy()
        menu()
    def drugOptions():
        try:
            optionsWindow.destroy()
        except Exception:
            pass
        def choiceFun(loc):
            if checkforduplicate(i['conceptProperties'][loc]['rxcui'], alldrugs) == False:
                alldrugs.append([i['conceptProperties'][loc]['name'],i['conceptProperties'][loc]['rxcui']])
            optionsWindow.destroy()
            searchDrug(alldrugs)
        drugSearch = entry.get()
        if drugSearch == "":
            messagebox.showerror(title="entry error",message="Insert a drug name first!")
        else:
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
                         messagebox.showinfo(title="Search alert",message="NO DATA FOUND!")
             elif (len(data['drugGroup']) == 2):
                 drugWindow.destroy()
                 optionsWindow=Tk()
                 optionsWindow.title("Drug Options")
                 
                 for i in data['drugGroup']['conceptGroup']:
        
                     if (i['tty'] == 'SBD' and len(i) >1):
                        def on_frame_configure(event):
                            canvas.configure(scrollregion=canvas.bbox("all"))
                        def on_canvas_scroll(event):
                            canvas.yview_scroll(int(-1 * (event.delta / 60)), "units")
                        count = 1
                        headline=Label(optionsWindow, text=f"Options available for {drugSearch}:", font=('Ariel',40,'bold'))
                        headline.pack(side='top')
                        canvas=Canvas(background='white')
                        frame=Frame(canvas, bg='white')
                        canvas.create_window((0,0), window=frame, anchor="n")
                        scrollBar= Scrollbar(frame, orient='vertical', command= canvas.yview)
                        canvas.bind_all("<MouseWheel>", on_canvas_scroll)
                        scrollBar.pack(side=RIGHT, fill="y", anchor='nw')
                        frame.bind("<Configure>", on_frame_configure)
                        canvas.bind("<Configure>", on_frame_configure)
                        canvas.pack(fill="both",anchor="center" ,expand=True)
                        for j in i['conceptProperties']:
                             btn=Button(frame, text=f"{count}. {j['name']}  rxcui - {j['rxcui']}", command=lambda count=count-1: choiceFun(count))
                             btn.pack(padx=20,pady=5)
                             
                             count +=1
                        canvas.configure(yscrollcommand=scrollBar.set)
                 optionsWindow.mainloop()

             else:messagebox.showinfo(title="Search alert",message="NO DATA FOUND!")



    drugWindow = Tk()
    drugWindow.title("drug search")
    drugWindow.config()
    entry = Entry(drugWindow, font=("Ariel", 30))
    entry.pack(side=LEFT)
    skipButton= Button(drugWindow, text="Skip", command=skip)
    skipButton.pack(side=RIGHT)
    searchButton = Button(drugWindow, text="Search", command=drugOptions)
    searchButton.pack(side=RIGHT)
    drugWindow.mainloop()

def checkforduplicate(rxcui, druglist):
    for drug in druglist:
        if rxcui == drug[1]:
            return True
    return False


