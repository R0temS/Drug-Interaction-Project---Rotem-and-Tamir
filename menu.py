#menu function prints the main menu
#showDrugList prints the drugs in druglist
from tkinter import *
from tkinter import messagebox
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
        