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
#def menu():
    #print("\nChoose your preffered option:")
    #print("1. Insert drugs")
    #print("2. Show drug list")
    #print("3. Check for drugs interactions")
    #print("4. Drug info")
    #print("5. Delete a drug")
    #print("6. Patient information")
    #print("7. Relevant allergies information")
    #print("8. Relevant background dieseases information")
    #print("9. Quit\n")
    
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

def showDrugList(druglist):
    if(len(druglist)!=0):
        listWindow = Tk()
        listWindow.configure(bg='white')
        headline=Label(listWindow, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----DRUG LIST-----")
        textbox = Label(listWindow, bg= 'white', font=('Ariel', 14), padx=20, pady=10, justify='left')
        text=""
        count = 1
        for i,j in druglist:
            
            text = text+"\n"+ str(count) + ". " + i+" -- rxcui: "+j
            count+=1
        textbox.configure(text=text)
        headline.pack(anchor='n')
        textbox.pack(anchor='nw')
        listWindow.mainloop()
    else:
        messagebox.showerror(message = "Insert drugs first!", title= "alert")




def clickHistory (): # opens a new window with the history details
    print("showing history")
    
def clickSchedule (): # creates a new schedule for the user
    print("creates new schedule")
    
def clickWarnings (allDrugs): # shows the relevant warnings for the user
    drugInteraction(allDrugs)
    
def clickProfile (patientInfo): # shows the user profile
   reviewProfile(patientInfo) 
    
def clickRecommand (): # recommending on drug to a sick user
    print ("recommending on drugs to a sick user")

def addDrugs(druglist, window, drugsInfoDic, patientInfo):
    
    window.destroy()
    searchDrug(druglist)
    updatedrugsinfodic(drugsInfoDic, druglist)
    mainMenu(druglist, drugsInfoDic, patientInfo)


def mainMenu(druglist, drugsInfoDic, patientInfo):
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
                           command=lambda: addDrugs(druglist, window, drugsInfoDic, patientInfo),
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
                           command=lambda: showDrugList(druglist),
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
                           command=clickHistory,
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
    showProfile.grid(column=2 , row=3, columnspan=2)
    
    # # DB creation
    
    # conn = sqlite3.connect('patient_info.db')
    # # Create table
    # conn.execute('''CREATE TABLE info(
    #                  firstName text,
    #                  lastName text,
    #                  age integer,
    #                  bgilnesses text,
    #                  allergies text
    #                  )''')
    # # Commit Changes
    # conn.commit()
    # # Close connection
    # conn.close()
    
    window.mainloop()
    
        