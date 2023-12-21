from ast import Try
import requests as req
import os
from tkinter import *
from tkinter import messagebox
from updateDB import *

#searchDrug function checks if a drug exists in the Api and adds it to the drug list
#checkforduplicate function checks if a specific drug is already exist in the druglist, if so it returns True, else it returns False
def searchDrug(druglist):
    def skip():
        drugWindow.destroy()
        ## need to add update hisory function
    def drugOptions():
        try:
            optionsWindow.destroy()
        except Exception:
            pass
        def choiceFun(loc, i):
            if checkforduplicate(i['conceptProperties'][loc]['rxcui'], druglist) == False:
                ##function of recieving the perday perweek
                druglist.append([i['conceptProperties'][loc]['name'],i['conceptProperties'][loc]['rxcui'], "perday", "perweek"])
            else:
                messagebox.showinfo(title="Attention",message="Drug already exists!")
            optionsWindow.destroy()
            searchDrug(druglist)
        drugSearch = entry.get().lower()
        if drugSearch == "":
            messagebox.showerror(title="entry error",message="Insert a drug name first!")
        else:
             str = "https://rxnav.nlm.nih.gov/REST/drugs.json?name=" + drugSearch
             try:
                 data = req.get(str).json()
             except Exception:
                 messagebox.showerror(title="Search alert",message="COULD NOT CONNECT, CHECK YOUR INTERNET CONNECTION!")
                 return
             
    
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
        
                     if (len(i) >1):#(i['tty'] == 'SBD' and 
                        def on_frame_configure(event):
                            canvas.configure(scrollregion=canvas.bbox("all"))
                        def on_canvas_scroll(event):
                            canvas.yview_scroll(int(-1 * (event.delta / 60)), "units")
                        count = 1
                        optionsWindow.configure(bg='white')
                        headline=Label(optionsWindow, text=f"Options available for {drugSearch}:", font=('Ariel',40,'bold'), bg='white')
                        headline.grid(row=0, column=0)
                        canvas=Canvas(background='white', width=50)
                        frame=Frame(canvas, bg='white', width=50)
                        canvas.create_window((150,50), window=frame, anchor="n")
                        canvas.bind_all("<MouseWheel>", on_canvas_scroll)
                        frame.bind("<Configure>", on_frame_configure)
                        canvas.bind("<Configure>", on_frame_configure)
                        canvas.grid(row=1, column=0)
                        widthlst=[]
                        for j in i['conceptProperties']:
                             btn=Button(frame,
                                       text=f"{count}. {j['name']}  rxcui - {j['rxcui']}",
                                      command=lambda count=count-1, i=i: choiceFun(count,i), 
                                      anchor='e', font=("Comic Sans", 12),
                                        fg="White",
                                     background="#20A5C9",
                                        activebackground="#20A5C1",
                                     activeforeground="White",)
                             widthlst.append(btn.winfo_reqwidth()+30)
                             btn.grid(padx=20,pady=5, row=count, column=0)
                             count +=1
                     
                 optionsWindow.update_idletasks()
                 canvas.configure(width=max(widthlst))
                 frame.configure(width=max(widthlst))
                 optionsWindow.geometry()
                 optionsWindow.eval('tk::PlaceWindow . center')
                 optionsWindow.mainloop()

             else:messagebox.showinfo(title="Search alert",message="NO DATA FOUND!")



    drugWindow = Tk()
    drugWindow.title("drug search")
    drugWindow.config()
    entry = Entry(drugWindow, font=("Ariel", 30))
    entry.pack(side=LEFT)
    skipButton= Button(drugWindow, text="Continue", command=skip)
    skipButton.pack(side=RIGHT)
    searchButton = Button(drugWindow, text="Search", command=drugOptions)
    searchButton.pack(side=RIGHT)
    drugWindow.eval('tk::PlaceWindow . center')
    drugWindow.mainloop()

def checkforduplicate(rxcui, druglist):
    for drug in druglist:
        if rxcui == drug[1]:
            return True
    return False
