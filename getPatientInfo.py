#from re import T
#import requests as req
##getPatientInfo function recieves the folowing info:
##-Name
##-Age
##-A list of allergies
##-A list of background diseases

##showPatientInfo function shows all of the information described above from the patientInfo dictionary

from turtle import title
from menu import *
from re import T
import requests as req
from tkinter import *
from tkinter import messagebox
from updateDB import *

def updatepatientInfo(patientInfo,firstName, lastName, Age, bgillnessWindow):
    #allergies and bg illnesses already updated
    patientInfo.update({'firstName': firstName.capitalize()})
    patientInfo.update({'lastName': lastName.capitalize()})
    patientInfo.update({'Age': Age})
    bgillnessWindow.destroy()
    updateDB("", "", patientInfo, "", "","patientinfo")

def deleteAllergies(patientInfo, window):
    patientInfo.update({'Allergies': []})
    updateDB("", "", patientInfo, "", "patientinfo")
    window.destroy()
    messagebox.showinfo(title="Success", message="All of the allergies deleted")

def deletebgIllness(patientInfo, window):
    patientInfo.update({'Background Dieseases': []})
    updateDB("", "", patientInfo, "", "patientinfo")
    window.destroy()
    messagebox.showinfo(title="Success", message="All of the background dieseases deleted")


def addAllergy(patientInfo, allergy, allergybox):
    allergybox.delete(0, END)
    if allergy != "":
        if patientInfo.get('Allergies') == None:
            patientInfo.update({'Allergies': []})
        allergy= allergy.lower()
        str = "https://rxnav.nlm.nih.gov/REST/spellingsuggestions.json?name=" + allergy
        data =req.get(str).json()
        if (len(data['suggestionGroup']['suggestionList']) != 0):
           allergy = data['suggestionGroup']['suggestionList']['suggestion'][len(data['suggestionGroup']['suggestionList']['suggestion'])-1]
        else:
           messagebox.showinfo(title="ATTENTION", message=(f"{allergy.upper()} NOT FOUND!"))
           allergy="N/A"
        if allergy!="N/A":
            messagebox.showinfo(title="Succeed", message=(f"{allergy.upper()} ADDED!"))
            if checkForDuplicatePatientInfo("allergy", allergy, patientInfo) == False:
               patientInfo['Allergies'].append(allergy.lower())
    else:
        messagebox.showerror(title="Insert allergy", message="Insert allergy first!")

def addIllness(patientInfo, diesease, dieseasebox):
     #handling background dieseases
     dieseasebox.delete(0, END)
     if diesease != "":
        if patientInfo.get('Background Dieseases') == None:
            patientInfo.update({'Background Dieseases': []})
        diesease = diesease.lower()
        if checkForDuplicatePatientInfo("background", diesease, patientInfo) == False:
           messagebox.showinfo(title="Succeed", message=(f"{diesease.upper()} ADDED!"))
           patientInfo['Background Dieseases'].append(diesease.lower())  
     else:
        messagebox.showerror(title="Insert BG illness", message="Insert background illness first!")


def bgillnessInsert(patientInfo,firstName, lastName, Age, allergyWindow):
    allergyWindow.destroy()
    bgillnessWindow= Tk()
    #handling allergies
    illness = Entry(bgillnessWindow, width=30)
    illness.grid(row=0, column=1)
    illnessL = Label(bgillnessWindow, text = "Background illness")
    illnessL.grid(row=0, column=0)
    finishBtn = Button(bgillnessWindow,
                     text="finish",
                     command= lambda: updatepatientInfo(patientInfo,firstName, lastName, Age, bgillnessWindow),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    finishBtn.grid(row=1, column=1, padx=10, ipadx=50)
    previewsBtn = Button(bgillnessWindow,
                     text="previews",
                     command= lambda: allergiesInsert(patientInfo,firstName, lastName, Age, bgillnessWindow),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    previewsBtn.grid(row=1, column=0, padx=10, ipadx=50)
    addillnessBtn = Button(bgillnessWindow,
                     text="add illness",
                     command= lambda: addIllness(patientInfo,illness.get(), illness),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    addillnessBtn.grid(row=0, column=3, padx=10, ipadx=50)
    bgillnessWindow.eval('tk::PlaceWindow . center')
    bgillnessWindow.mainloop()




def allergiesInsert(patientInfo, firstName, lastName, Age, info):
    # handling name
    #patientInfo.update({'firstName':firstName.capitalize(), 'lastName': lastName.capitalize()})
    
    # handling age
    try:
        int(Age)
        #patientInfo.update({'Age':age})
    except Exception:
        messagebox.showinfo(title='Input error', message='ENTER ONLY INTEGERS!')
        info.destroy()
        getPatientInfo(patientInfo, firstName, lastName, "", "")
        return
        
    info.destroy()
    allergyWindow= Tk()
    #handling allergies
    allergies = Entry(allergyWindow, width=30)
    allergies.grid(row=0, column=1)
    allergiesL = Label(allergyWindow, text = "Allergies")
    allergiesL.grid(row=0, column=0)
    nextBtn = Button(allergyWindow,
                     text="next",
                     command= lambda: bgillnessInsert(patientInfo,firstName, lastName, Age, allergyWindow),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    nextBtn.grid(row=1, column=1, padx=10, ipadx=50)
    previewsBtn = Button(allergyWindow,
                     text="previews",
                     command= lambda: getPatientInfo(patientInfo,firstName, lastName, Age, allergyWindow),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    previewsBtn.grid(row=1, column=0, padx=10, ipadx=50)
    addallergyBtn = Button(allergyWindow,
                     text="add allergy",
                     command= lambda: addAllergy(patientInfo,allergies.get(), allergies),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    addallergyBtn.grid(row=0, column=3, padx=10, ipadx=50)
    allergyWindow.mainloop()
                   
   
     
    # #updating DB
    # conn.execute("INSERT INTO info (firstName,lastName,age,bgilnesses,allergies) \
    # VALUES (firstName.get(), lastName.get(), Age.get(),bgIlnesses.get(), allergies.get()")
    
    #clearing the text boxes
    
    
    
           
def getPatientInfo(patientInfo, firstname, lastname, age, allergywindow):
    try:
        allergywindow.destroy()
    except Exception:
        pass
    info = Tk()
    
    # create text boxes
    firstName = Entry(info, width=30)
    firstName.insert(0, firstname)
    firstName.grid(row=0, column=1, padx=20 )
    lastName = Entry(info, width=30)
    lastName.insert(0, lastname)
    lastName.grid(row=1, column=1, padx=20 )
    Age = Entry(info, width=30)
    Age.insert(0, age)
    Age.grid(row=2, column=1, padx=20 )
    #bgIlnesses = Entry(info, width=30)
    #bgIlnesses.grid(row=4, column=1, padx=20 )
    #allergies = Entry(info, width=30)
    #allergies.grid(row=5, column=1, padx=20 )
        
    
    # create text box lables
    firstNameL = Label(info, text = "First Name")
    firstNameL.grid(row=0, column=0)
    
    lastNameL = Label(info, text = "Last Name")
    lastNameL.grid(row=1, column=0)
    
    ageL = Label(info, text = "Age")
    ageL.grid(row=2, column=0)
    
    #bgIlnessesL = Label(info, text = "Background Ilnesses")
    #bgIlnessesL.grid(row=4, column=0)
        
    #allergiesL = Label(info, text = "Allergies")
    #allergiesL.grid(row=5, column=0)
    
    
    #create submit button
    nextBtn = Button(info,
                     text="next",
                     command= lambda: allergiesInsert(patientInfo,firstName.get(), lastName.get(), Age.get(), info),
                     font=("Comic Sans", 16),
                     fg="White",
                     background="#20A5C9",
                     activebackground="#20A5C9",
                     activeforeground="White")
    nextBtn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=50)
    
    
    
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


def reviewProfile(patientInfo):##!!!!!need to be taken from the patientInfo dictionary!!!!
    reviewInfo = Toplevel()
    reviewInfo.configure(bg="white")
    headline=Label(reviewInfo, bg= 'white', font=('Ariel', 18), padx=20, pady=10, justify='center', text="-----Patient Info-----")
    textbox = Label(reviewInfo, bg= 'white', font=('Ariel', 14), padx=20, pady=10, justify='left')
    text=f"The information of {patientInfo['firstName']} {patientInfo['lastName']}:\n\nAge: {patientInfo['Age']}\n"
    if len(patientInfo['Allergies'])!=0:
        text = text +"\nAllergies:\n"
        for allergy in patientInfo['Allergies']:
            text = text+ f"- {allergy}\n"
    else:
        text = text +"\nHas no allergies\n"
    if len(patientInfo['Background Dieseases'])!=0:
        text = text +"\nBackground Dieseases:\n"
        for diesease in patientInfo['Background Dieseases']:
            text = text+ f"- {diesease}\n"
    else:
        text = text +"\nHas no background dieseases\n"
    
    textbox.configure(text=text)
    headline.grid(row=0,column=0, columnspan=2)
    textbox.grid(row=1,column=0, columnspan=2)
    add = Button(reviewInfo,
                 command= lambda: getPatientInfo(patientInfo, patientInfo['firstName'], patientInfo['lastName'], patientInfo['Age'], reviewInfo),
                 text="EDIT INFO",       
                 font=("Comic Sans", 20),
                 fg="White",
                 background="#20A5C9",
                 activebackground="#20A5C9",
                 activeforeground="White",
                 state=ACTIVE,
                 compound='bottom',
                 padx=10,
                 pady=10, width=25)
    add.grid(row=3, column=0)

    deleteallergies = Button(reviewInfo,
                 command= lambda: deleteAllergies(patientInfo, reviewInfo),
                 text="DELETE ALLERGIES",       
                 font=("Comic Sans", 20),
                 fg="White",
                 background="#20A5C9",
                 activebackground="#20A5C9",
                 activeforeground="White",
                 state=ACTIVE,
                 compound='bottom',
                 padx=10,
                 pady=10, width=25)
    deleteallergies.grid(row=2, column=0)

    deletebgillness = Button(reviewInfo,
                 command= lambda: deletebgIllness(patientInfo, reviewInfo),
                 text="DELETE BG DIESEASES",       
                 font=("Comic Sans", 20),
                 fg="White",
                 background="#20A5C9",
                 activebackground="#20A5C9",
                 activeforeground="White",
                 state=ACTIVE,
                 compound='bottom',
                 padx=10,
                 pady=10, width=25)
    deletebgillness.grid(row=2, column=1)
    
    back = Button(reviewInfo,
                 command= lambda: reviewInfo.destroy(),
                 text="Back to menu",       
                 font=("Comic Sans", 20),
                 fg="White",
                 background="#20A5C9",
                 activebackground="#20A5C9",
                 activeforeground="White",
                 state=ACTIVE,
                 compound='bottom',
                 padx=10,
                 pady=10, width=25)
    back.grid(row=3, column=1)
    
    reviewInfo.mainloop()
