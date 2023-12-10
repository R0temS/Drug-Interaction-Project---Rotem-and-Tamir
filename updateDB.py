import sqlite3

#this function receives the information from the DB and updates the variables  
def getInfoFromDB(druglist, drugsInfoDic, patientInfo, historyDrugs):
    conn = sqlite3.connect('patient_info.db')
    c = conn.cursor()

    #druglist
    c.execute('SELECT drugname FROM drugList')
    drugname = c.fetchall()
    c.execute('SELECT drugrxcui FROM drugList')
    drugrxcui = c.fetchall()
    c.execute('SELECT perweek FROM drugList')
    perweek = c.fetchall()
    c.execute('SELECT perday FROM drugList')
    perday = c.fetchall()

    for drugname, drugrxcui, perweek, perday in zip (drugname, drugrxcui, perweek, perday):
        druglist.append([drugname, drugrxcui, perweek, perday])

    #history
    c.execute('SELECT drugname FROM historyDrugs')
    drugname = c.fetchall()
    c.execute('SELECT drugrxcui FROM historyDrugs')
    drugrxcui = c.fetchall()
    c.execute('SELECT perweek FROM historyDrugs')
    perweek = c.fetchall()
    c.execute('SELECT perday FROM historyDrugs')
    perday = c.fetchall()

    for drugname, drugrxcui, perweek, perday in zip (drugname, drugrxcui, perweek, perday):
        historyDrugs.append([drugname, drugrxcui, perweek, perday])

    #patient info
    c.execute('SELECT firstName FROM info')
    firstName = c.fetchall()
    c.execute('SELECT lastName FROM info')
    lastName = c.fetchall()
    c.execute('SELECT age FROM info')
    age = c.fetchall()
    c.execute('SELECT bgilnesses FROM info')
    bgilnesses = c.fetchall()
    c.execute('SELECT allergies FROM info')
    allergies = c.fetchall()
   
    patientInfo.update({'firstName': firstName, 'lastName': lastName, 'Age': age, 'Allergies': [], 'Background Dieseases': []})
    for bgilnesses in bgilnesses:
        patientInfo['Background Dieseases'].append(bgilnesses)

    for allergies in allergies:
        patientInfo['Allergies'].append(allergies)


    #drugs information dic
    
    c.execute('SELECT rxcui FROM drugsInfo')
    rxcui = c.fetchall()
    c.execute('SELECT drugName FROM drugsInfo')
    drugName = c.fetchall()
    c.execute('SELECT INDICATION_AND_USAGE FROM drugsInfo')
    INDICATION_AND_USAGE = c.fetchall()
    c.execute('SELECT WARNINGS FROM drugsInfo')
    WARNINGS = c.fetchall()
    c.execute('SELECT DOSAGE_AND_ADMINISTRATION FROM drugsInfo')
    DOSAGE_AND_ADMINISTRATION = c.fetchall()

    drugsInfoDic.update({"druginfo": []})
    for rxcui, drugName, INDICATION_AND_USAGE, WARNINGS, DOSAGE_AND_ADMINISTRATION in zip (rxcui, drugName, INDICATION_AND_USAGE, WARNINGS, DOSAGE_AND_ADMINISTRATION):
        drugsInfoDic['druginfo'].append({"rxcui": rxcui, "drugName": drugName, "INDICATION AND USAGE": INDICATION_AND_USAGE, "WARNINGS": WARNINGS, "DOSAGE AND ADMINISTRATION": DOSAGE_AND_ADMINISTRATION})
    
    conn.close()
    

def updateDB(druglist, drugsInfoDic, patientInfo, historyDrugs, mode):
        conn = sqlite3.connect('patient_info.db')
        c = conn.cursor()
       
        if mode == "druglist":
            c.execute('UPDATE druglist SET drugname = NULL, drugrxcui = NULL, perweek = NULL, perday = NULL')  #initializing the table values

            for item in druglist:
                for drugname, drugrxcui, perweek, perday in item:
                    c.execute('INSERT INTO drugList (drugname, drugrxcui, perweek, perday) VALUES (?, ?, ?, ?)', (drugname, drugrxcui, perweek, perday))

        if mode == "drughistory":
            c.execute('UPDATE historyDrugs SET drugname = NULL, drugrxcui = NULL, perweek = NULL, perday = NULL')  #initializing the table values

            for item in historyDrugs:
                for drugname, drugrxcui, perweek, perday in item:
                    c.execute('INSERT INTO historyDrugs (drugname, drugrxcui, perweek, perday) VALUES (?, ?, ?, ?)', (drugname, drugrxcui, perweek, perday))
        
        if mode == "patientinfo":
            c.execute('UPDATE info SET firstName = NULL, lastName = NULL, age = NULL, bgilnesses = NULL, allergies = NULL')  #initializing the table values
            
            
         
        if mode == "druginfo":
            c.execute('UPDATE drugsInfo SET rxcui = NULL, drugName = NULL, INDICATION_AND_USAGE = NULL, WARNINGS = NULL, DOSAGE_AND_ADMINISTRATION = NULL')  #initializing the table values
            
            
        conn.commit()           
        conn.close()