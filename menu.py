#menu function prints the main menu
#showDrugList prints the drugs in druglist

def menu():
    print("\nChoose your preffered option:")
    print("1. Insert drugs")
    print("2. Show drug list")
    print("3. Check for drugs interactions")
    print("4. Drug info")
    print("5. Delete a drug")
    print("6. Patient information")
    print("7. Relevant allergies information")
    print("8. Quit\n")
    

def showDrugList(druglist):
    if(len(druglist)!=0):
        print("-----DRUG LIST-----")
        count = 1
        for i,j in druglist:
            print(str(count) + ". ", end="")
            print(i+" -- rxcui: "+j)
            count+=1
    else:
        print("\nInsert drugs first!")
