#11/12 - i added the clickHistory function and tried to add the remove drug button - need to recheck it

#menu function prints the main menu
#showDrugList prints the drugs in druglist
from tkinter import *
from tkinter import messagebox
import os
import requests as req
from getInfofun import *
from searchDrugfun import *
from drugInteractionfun import *
from getPatientInfo import *
from checkallergyandbrd import *
import sqlite3 
from drugInteractionfun import *
from getPatientInfo import *
    
def menu():
  print("\nChoose your preffered option:")
  print("1. Insert drugs")
  print("2. Show drug list")
  print("3. Check for drugs interactions")
  print("4. Drug info")
  print("5. Delete a drug")
  print("6. Patient information")
  print("7. Relevant allergies information")
  print("8. Relevant background dieseases information")
  print("9. Quit\n")
  #window = Tk()
  #window.geometry("420x420")
  #window.config(background="black")
  #window.title("main menu")

  #window.mainloop()


def destroyWindow(Window):
    Window.destroy()
#this function recieves an index of a drug in the drug list and removes it from there
def removeDrug(druglist, index, historyDrugs, listWindow, drugsInfoDic):
    if index.isdigit() == True:
        if (int(index)>0 and int(index)<= len(druglist)):
            historyDrugs.append(druglist[int(index)-1])#the removed drug added to the history list
            drugfordelete1 = findLocationInDrugsInfoDic(druglist, drugsInfoDic, int(index)-1)
            druglist.pop(int(index)-1)
            if drugfordelete1!=-1:
                 drugsInfoDic['druginfo'].pop(drugfordelete1)
            listWindow.destroy()
            messagebox.showinfo(title='Success', message='DRUG REMOVED!')
            updateDB(druglist, "", "", "", "druglist")  # updating the DB
            updateDB("", drugsInfoDic, "", "", "druginfo")
            updateDB("", "", "", historyDrugs, "drughistory")
        else:
            messagebox.showerror(title='Input error', message='CHOICE OUT OF RANGE!')
    else:
        messagebox.showerror(title='Input error', message='ENTER ONLY INTEGERS!')
    
    
    
    print(druglist)
    print(len(druglist))
    print(historyDrugs)    

def showDrugList(druglist, historyDrugs, drugsInfoDic):
    if(len(druglist)!=0):
        listWindow = Tk()
        listWindow.configure(bg='white')
        headline=Label(listWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG LIST-----")
        textbox = Label(listWindow, bg= 'white', font=('Ariel', 14), padx=20, pady=10, justify='left')
        text=""
        count = 1
        for i,j,d,w in druglist:
            
            text = text+"\n"+ str(count) + ". " + i+" -- rxcui: "+j
            count+=1
        textbox.configure(text=text)
        headline.pack(anchor='n')
        textbox.pack(anchor='nw')
        
        entrybox = Entry(listWindow, width=30)
        entrybox.pack()
        # creating button for removing a drug from the list to History section   
        remove = Button(listWindow,
                        text="Remove Drug",
                        command=lambda: removeDrug(druglist, entrybox.get(), historyDrugs, listWindow, drugsInfoDic),
                        font=("Comic Sans", 20),
                        fg="White",
                        background="#20A5C9",
                        activebackground="#20A5C1",
                        activeforeground="White",
                        state=ACTIVE,
                        compound='bottom',
                        padx=10,
                        pady=10, width=25) 
        remove.pack()
        back = Button(listWindow,
                        text="Back to menu",
                        command=lambda: destroyWindow(listWindow),
                        font=("Comic Sans", 20),
                        fg="White",
                        background="#20A5C9",
                        activebackground="#20A5C1",
                        activeforeground="White",
                        state=ACTIVE,
                        compound='bottom',
                        padx=10,
                        pady=10, width=25) 
        back.pack()
        listWindow.mainloop()
    else:
        messagebox.showerror(message = "Insert drugs first!", title= "alert")

def getInfoSubmit(choice, druglist, entrybox, listWindow, drugsInfodic):
    try:
        choice= int(choice)
    except Exception:
        entrybox.delete(0, END)
        messagebox.showerror(title='Input error', message='ENTER ONLY INTEGERS!')
        return
    if (choice<1 or choice>len(druglist)):
        entrybox.delete(0, END)
        messagebox.showerror(title='Input error', message='CHOICE OUT OF RANGE!')
        return
    else:
        choice -=1
        listWindow.destroy()
        getInfo(druglist[choice][1], "p", drugsInfodic, druglist[choice][0], 0, listWindow)


def drugInfo(druglist, drugsInfodic, window):
    if(len(druglist)!=0):
        window.destroy()
        listWindow = Tk()
        listWindow.configure(bg='white')
        headline=Label(listWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG LIST-----")
        textbox = Label(listWindow, bg= 'white', font=('Ariel', 14), padx=20, pady=10, justify='left')
        entrybox = Entry(listWindow, width=30)
        label = Label(listWindow, text = "Which Drug?")
        pick = Button(listWindow, 
                           text="Submit",
                           command=lambda: getInfoSubmit(entrybox.get(), druglist, entrybox, listWindow, drugsInfodic),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C1",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10, width=25)
        text=""
        count = 1
        for i,j,d,w in druglist:
            
            text = text+"\n"+ str(count) + ". " + i+" -- rxcui: "+j
            count+=1
        textbox.configure(text=text)
        headline.grid(row=0, column=0)
        textbox.grid(row=1, column=0)
        label.grid(row=2, column=0)
        entrybox.grid(row=2, column=1)
        pick.grid(row=2, column=2)
       
        listWindow.mainloop()
    else:
        messagebox.showerror(message = "Insert drugs first!", title= "alert")

def clickHistory (historyDrugs): # opens a new window with the history details
    if(len(historyDrugs)!=0):
        historyWindow = Tk()
        historyWindow.configure(bg='white')
        headline=Label(historyWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="----- MEDICINE HISTORY -----")
        textbox = Label(historyWindow, bg= 'white', font=('Ariel', 14), padx=20, pady=10, justify='left')
        text=""
        count = 1
        for i,j,d,w in historyDrugs:
            
            text = text+"\n"+ str(count) + ". " + i+" -- rxcui: "+j
            count+=1
        textbox.configure(text=text)
        headline.grid(row = 0, column =1, rowspan=2)
        textbox.grid(row = 1, column =0, rowspan=4)

        previewsBtn = Button(historyWindow,
                     text="previews",
                     command= lambda: destroyWindow(historyWindow),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
        previewsBtn.grid(row=2, column=0, padx=10, ipadx=50)
        historyWindow.mainloop()
    else:
        messagebox.showerror(message = "No history found!", title= "attention")


    
def clickSchedule (): # creates a new schedule for the user
    print("creates new schedule")
    
def clickWarnings (allDrugs): # shows the relevant warnings for the user
    drugInteraction(allDrugs)
    
def clickProfile (patientInfo): # shows the user profile
   reviewProfile(patientInfo) 
    
def clickRecommand (): # recommending on drug to a sick user
    print ("recommending on drugs to a sick user")

def addDrugs(druglist, window, drugsInfoDic, patientInfo, historyDrugs):
    
    window.destroy()
    searchDrug(druglist)
    updatedrugsinfodic(drugsInfoDic, druglist)
    updateDB(druglist, "", "", "", "druglist")# updating the DB  
    
    mainMenu(historyDrugs, druglist, drugsInfoDic, patientInfo)


def mainMenu(historyDrugs, druglist, drugsInfoDic, patientInfo):
    window = Tk()
    window.title("Drug Management System")
    window.geometry("1000x500")
    #drugLogo = PhotoImage(file='drug logo.png')
    #window.iconphoto(True, drugLogo)
    frame = LabelFrame(window, text="MENU", padx=10, pady=10 )
    frame.pack(padx=10, pady=10, side='bottom')
    
    #creating label
    
    label = Label(window, text="Drugs Coordinator",
                  compound='top',
                  font=("Comic Sans", 20),
                  fg="White",
                  background="#20A5C9",
                  activebackground="#20A5C9",
                  activeforeground="White",
                  padx=10,
                  pady=10,
                  width=25)
                  
    label.pack()
    
                 
     #button for schedule planning
    drugSearch = Button(frame, 
                           text="ADD DRUGS",
                           command=lambda: addDrugs(druglist, window, drugsInfoDic, patientInfo, historyDrugs),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C1",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10, width=25)
    drugSearch.grid(column=0 , row=0, columnspan=2)
    
    showDrugs = Button(frame, 
                           text="DRUG LIST",
                           command=lambda: showDrugList(druglist, historyDrugs, drugsInfoDic),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10, width=25)
    showDrugs.grid(column=2 , row=0, columnspan=2)
    
    #button for schedule planning
    makeSchedule = Button(frame, 
                           text="CREATE SCHEDULE",
                           command=clickSchedule,
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10, width=25)
    makeSchedule.grid(column=0 , row=1, columnspan=2)
    #makeSchedule.pack(side=RIGHT)
    
    #button for showing drug usage history
    showHistory = Button(frame, 
                           text="HISTORY",
                           command= lambda: clickHistory(historyDrugs),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10,
                           width=25)
    showHistory.grid(column=0 , row=2, columnspan=2)
    #showHistory.pack(side=RIGHT)
    
    #button for presenting relebant warnings for the user
    showWarnings = Button(frame, 
                           text="WARNINGS",
                           command= lambda: clickWarnings(druglist),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10,
                           width=25)
    showWarnings.grid(column=0 , row=3, columnspan=2)
    #showWarnings.pack(side=RIGHT)
    
    #button for showing user profile
    showProfile = Button(frame,
                           text="MY PROFILE",
                           command=lambda: clickProfile(patientInfo),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10,
                           width=25)
    showProfile.grid(column=2 , row=1, columnspan=2)
    #showProfile.pack(side=RIGHT)
    
    #button for recommending drugs to a sick user
    drugRecommend= Button(frame, 
                           text="DRUG RECOMMENDATION",
                           command=clickRecommand,
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10,
                           width=25)
    drugRecommend.grid(column=2 , row=2, columnspan=2)
    #drugRecommend.pack(side=RIGHT)
    
    #exit button
    showProfile = Button(frame,
                           text="EXIT",
                           command=exit,
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10,
                           width=25)
    showProfile.grid(column=1 , row=4, columnspan=2)

    druginfo = Button(frame,
                           text="DRUG INFO",
                           command= lambda: drugInfo(druglist, drugsInfoDic, window),
                           font=("Comic Sans", 20),
                           fg="White",
                           background="#20A5C9",
                           activebackground="#20A5C9",
                           activeforeground="White",
                           state=ACTIVE,
                           compound='bottom',
                           padx=10,
                           pady=10,
                           width=25)
    druginfo.grid(column=2 , row=3, columnspan=2)
    
    window.mainloop()
    
        