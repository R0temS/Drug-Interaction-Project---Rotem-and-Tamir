#from re import T
#import requests as req
##getPatientInfo function recieves the folowing info:
##-Name
##-Age
##-A list of allergies
##-A list of background diseases

##showPatientInfo function shows all of the information described above from the patientInfo dictionary
#def getPatientInfo(patientInfo):
#    patientInfo.update({'Name':input("Enter your name: ").capitalize()})
#    age="a"
#    while age=="a":
#        try:
#            age = int(input("Enter your age: "))
#            patientInfo.update({'Age':age})
#        except Exception:
#            print("\nENTER ONLY INTEGERS!\n")
#    allergy = "a"
#    while allergy!="":
#        if patientInfo.get('Allergies') == None:
#            allergy= input("Enter substances you are allergic to (leave empty to continue): ").lower()
#            if allergy !="":
#                str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + allergy
#                data =req.get(str).json()
#                if (len(data['suggestionGroup']['suggestionList']) == 1):
#                    allergy = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
#                else:
#                    print("\nSUBSTANCE NOT FOUND!\n")
#                    allergy="N/A"
#            if allergy !="" and allergy!="N/A":
#                patientInfo.update({'Allergies':[allergy]})
#        elif allergy!="":
#            allergy= input("Enter substances you are allergic to (leave empty to continue): ").lower()
#            if allergy !="":
#                str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + allergy
#                data =req.get(str).json()
#                if (len(data['suggestionGroup']['suggestionList']) != 0):
#                        allergy = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
#                else:
#                        print("\nSUBSTANCE NOT FOUND!\n")
#                        allergy="N/A"
#                if allergy !="" and allergy!="N/A":
#                    if checkForDuplicatePatientInfo("allergy", allergy, patientInfo) == False:
#                        patientInfo['Allergies'].append(allergy)
    
#    backgroundDisease = "a"
#    while backgroundDisease!="":
#        if patientInfo.get('Background Dieseases') == None:
#            backgroundDisease= input("Enter your background Dieseases (leave empty to continue): ").lower()
#            if backgroundDisease!="":
#                patientInfo.update({'Background Dieseases':[backgroundDisease]})
#        else:
#            backgroundDisease= input("Enter your background Dieseases (leave empty to continue): ").lower()
#            if backgroundDisease !="":
#                if checkForDuplicatePatientInfo("background", backgroundDisease, patientInfo) == False:
#                    patientInfo['Background Dieseases'].append(backgroundDisease)

#def showPatientInfo(patientInfo):
#    if patientInfo.get("Age")!=None:
#        print(f"\nThe age of {patientInfo['Name']} is {patientInfo['Age']}")
#    if patientInfo.get("Allergies")!=None:
#        print(f"{patientInfo['Name']} has alergies to:")
#        for allergy in patientInfo['Allergies']:
#            print("- "+allergy)
#        print("")
#    if patientInfo.get("Background Dieseases")!=None:
#        print(f"{patientInfo['Name']} has the following background dieseases:")
#        for brd in patientInfo['Background Dieseases']:
#            print("- "+brd)
#        print("")

from turtle import title
from menu import *
from re import T
import requests as req
from tkinter import *
from tkinter import messagebox


# create submit function for DB
def submit(patientInfo, firstName, lastName, Age, allergies, bgIlnesses, info):
    # handling name
    patientInfo.update({'Name':firstName.get().capitalize()+" "+lastName.get().capitalize()})
    
    # handling age
    try:
        age = int(Age.get())
        patientInfo.update({'Age':age})
    except Exception:
        messagebox.showinfo(title='Input error', message='ENTER ONLY INTEGERS!')
    
    #handling allergies
    allergyInfo = allergies.get().split(", ")
    if allergyInfo != [""]:
        patientInfo.update({'Allergies': []})
        for allergy in allergyInfo:
            
            allergy= allergy.lower()
            str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + allergy
            data =req.get(str).json()
            if (len(data['suggestionGroup']['suggestionList']) != 0):
               allergy = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
            else:
               messagebox.showinfo(title="ATTENTION", message=(f"{allergy.upper()} NOT FOUND!"))
               allergy="N/A"
            if allergy!="N/A":
                if checkForDuplicatePatientInfo("allergy", allergy, patientInfo) == False:
                   patientInfo['Allergies'].append(allergy.lower())
                   
    #handling background dieseases
    backgroundInfo = bgIlnesses.get().split(", ")
    if backgroundInfo != [""]:
        patientInfo.update({'Background Dieseases': []})
        for diesease in backgroundInfo:
            diesease = diesease.lower()
            if checkForDuplicatePatientInfo("background", diesease, patientInfo) == False:
               patientInfo['Background Dieseases'].append(diesease.lower())
     
    # #updating DB
    # conn.execute("INSERT INTO info (firstName,lastName,age,bgilnesses,allergies) \
    # VALUES (firstName.get(), lastName.get(), Age.get(),bgIlnesses.get(), allergies.get()")
    
    #clearing the text boxes
    firstName.delete(0, END)
    lastName.delete(0, END)
    Age.delete(0, END)
    bgIlnesses.delete(0, END)
    allergies.delete(0, END)
    info.destroy()
    
    
           
def getPatientInfo(patientInfo):
    info = Tk()
    
    # create text boxes
    firstName = Entry(info, width=30)
    firstName.grid(row=0, column=1, padx=20 )
    lastName = Entry(info, width=30)
    lastName.grid(row=1, column=1, padx=20 )
    Age = Entry(info, width=30)
    Age.grid(row=2, column=1, padx=20 )
    bgIlnesses = Entry(info, width=30)
    bgIlnesses.grid(row=4, column=1, padx=20 )
    allergies = Entry(info, width=30)
    allergies.grid(row=5, column=1, padx=20 )
        
    
    # create text box lables
    firstNameL = Label(info, text = "First Name")
    firstNameL.grid(row=0, column=0)
    
    lastNameL = Label(info, text = "Last Name")
    lastNameL.grid(row=1, column=0)
    
    ageL = Label(info, text = "Age")
    ageL.grid(row=2, column=0)
    
    bgIlnessesL = Label(info, text = "Background Ilnesses")
    bgIlnessesL.grid(row=4, column=0)
        
    allergiesL = Label(info, text = "Allergies")
    allergiesL.grid(row=5, column=0)
    
    
    #create submit button
    submitBtn = Button(info, text="Add record to DB", command= lambda: submit(patientInfo,firstName, lastName, Age, allergies, bgIlnesses, info))
    submitBtn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=100)
    
    
    
    info.mainloop()


def checkForDuplicatePatientInfo(mode, item, patientInfo):
    if mode == "allergy":
        for x in patientInfo['Allergies']:
            if x == item:
                return True
    elif mode == "background":
        for x in patientInfo['Background Dieseases']:
            if x == item:
                return True

    return False


# i created a DB - but i need to know how to approach the values inside of it (with "." or []?)


def reviewProfile():##!!!!!need to be taken from the patientInfo dictionary!!!!
    reviewInfo = Toplevel()
     #create text boxes
    firstName = info.firstName.get()
    firstName.grid(row=0, column=1, padx=20 )
    lastName = info.lastName.get()
    lastName.grid(row=1, column=1, padx=20 )
    age = info.age.get()
    age.grid(row=2, column=1, padx=20 )
    bgIlnesses = info.bgIlnesses.get()
    bgIlnesses.grid(row=4, column=1, padx=20 )

    # create text box lables
    firstNameL = Label(reviewInfo, text = "First Name: ")
    firstNameL.grid(row=0, column=0)

    lastNameL = Label(reviewInfo, text = "Last Name: ")
    lastNameL.grid(row=1, column=0)

    ageL = Label(reviewInfo, text = "Age: ")
    ageL.grid(row=2, column=0)

    bgIlnessesL = Label(reviewInfo, text = "Background Ilnesses: ")
    bgIlnessesL.grid(row=4, column=0)

    add = Button(reviewInfo,
                 text="EDIT",       
                 font=("Comic Sans", 20),
                 fg="White",
                 background="#20A5C9",
                 activebackground="#20A5C9",
                 activeforeground="White",
                 state=ACTIVE,
                 compound='bottom',
                 padx=10,
                 pady=10, width=25)
    
    
    reviewInfo.mainloop()