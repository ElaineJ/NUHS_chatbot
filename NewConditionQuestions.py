# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:35:36 2018

@author: User
"""
import time
import datetime
import random
from fpdf import FPDF
def CorrectCount(entity,value,text,CorrectCount,SequenceCount):
    if entity=="Constipation":
        options=["0","1","2"]
        print(value)
        if value=="not passing motion" or SequenceCount==1:
                if text in options:
                    CorrectCount+=1
                    return CorrectCount
                else:
                    return CorrectCount
        else:
            if text=="Yes":
                CorrectCount+=1
                return CorrectCount
            else:
                return CorrectCount
    

def ConstipationQuestion(value,SequenceCount,start):
    Question_Index={"not passing motion":0,"straining":1,"blood poo":2,"large stool":3,"painful":4,"bloated":5}
    Question_Dictionary={"0":"How many times is your child passing motion in 1 week?","1":"Does your child have to strain when passing motion?","2":"Is there any blood when your child passes motion?","3":"Does your child usually pass large sized stools?","4":"Is it painful when your child passes motion?","5":"Is your child's belly bloated?"}
    if start==1:
        #output value question and updated sequence count, when sequence count is 0, update to value's index
        try:
             
             question_index=str(Question_Index[value]) #derive from current value
             SequenceCount=Question_Index[value] #update the sequence count to its rightful number
             question=Question_Dictionary[question_index] #get question
        except KeyError:
             question_index=str(0) #derive from current value
             SequenceCount=0#update the sequence count to its rightful number
             question=Question_Dictionary[question_index] #get question
        if SequenceCount<5:
            SequenceCount+=1 #update sequence count to output
        else:
            SequenceCount=0
        return question,SequenceCount
    else:
        question_index=str(SequenceCount)
        question=Question_Dictionary[question_index]
        if SequenceCount<5:
            SequenceCount+=1
        else:
            SequenceCount=0
        
        return question,SequenceCount
    
def GastroenteritisQuestion(value,SequenceCount,start): #remember need to take into account age later.
    Question_Index={"diarrhea":0,"vomit":2}
    Question_Dictionary={"0":"How many times is the diarrhea in 1 day","1":"Is there blood in the diarrhea?","2":"How many times is the vomiting in 1 day?","3":"Is there blood in the vomit?","4":"Is there greenish fluid from vomit?","5":"Does the vomit shoot out?","6":"Does your child want to drink water?"}
    if start==1: #output value question and updated sequence count, when sequence count is 0, update to value's index
        try:
            question_index=str(Question_Index[value]) #derive from current value
            SequenceCount=Question_Index[value] #update the sequence count to its rightful number
            question=Question_Dictionary[question_index] #get question
        except KeyError:
            question_index=str(0) #derive from current value
            SequenceCount=0#update the sequence count to its rightful number
            question=Question_Dictionary[question_index] #get question
        if SequenceCount<6:
            SequenceCount+=1 #update sequence count to output
        else:
            SequenceCount=0
        return question,SequenceCount
    else:
        question_index=str(SequenceCount)
        question=Question_Dictionary[question_index]
        if SequenceCount<6:
            SequenceCount+=1
        else:
            SequenceCount=0
        
        return question,SequenceCount

def recordend(user_data):
    #record in file
        #generate random record number
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    number=random.randrange(0,10000000)
    filename="Patient "+str(number)+".txt"
    Record  = open(filename, "w")
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    Record.write("Start time: "+user_data["starttime"]+"\n")
    pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
    Record.write("Age: "+user_data["age"]+"\n")
    pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
    Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
    pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
    if "surgery" in user_data.keys():
        Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
        pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
    if "score" in user_data.keys():
        Record.write("FLACC score: "+str(user_data["score"])+"\n")
        pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
    if "bleed" in user_data.keys():
        Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
        pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
    if "puswound" in user_data.keys():
        Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
        pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
    if "painmed" in user_data.keys():
        Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
        pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
    if "drain" in user_data.keys():
        Record.write("Draining function working?: "+user_data["drain"]+"\n")
        pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
    if "string" in user_data.keys():
        Record.write("Is the string intact?: "+user_data["string"]+"\n")
        pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
    if "hospital?" in user_data.keys():
        Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
        pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
    if "Past Symptoms" in user_data.keys():
        Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
        pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
    if "similar?" in user_data.keys():
        Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
        pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
    if "notunderstood" in user_data.keys():
        Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
    if "understood" in user_data.keys():
        Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
    if "entity" in user_data.keys():
        Record.write("Condition detected: "+user_data["entity"]+"\n")
        pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
    if "shitfrequency" in user_data.keys():
        Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
        pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
    if "strain?" in user_data.keys():
        Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
        pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
    if "bloodpoo" in user_data.keys():
        Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
        pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
    if "largestool?" in user_data.keys():
        Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
        pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
    if "painful?" in user_data.keys():
        Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
        pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
    if "bloated?" in user_data.keys():
        Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
        pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
    if "food" in user_data.keys():
        Record.write("Exposure to new food: "+user_data["food"]+"\n")
        pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
    if "diarrheaNo" in user_data.keys():
        Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
        pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
    if "vomitingNo" in user_data.keys():
        Record.write("Number of vomits per day: "+user_data["vomits"]+"\n")
        pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
    if "blooddiarrhea" in user_data.keys():
        Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
        pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
    if "bloodvomit" in user_data.keys():
        Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
        pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
    if "green" in user_data.keys():
        Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
        pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
    if "shoot" in user_data.keys():
        Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
        pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
    if "drink" in user_data.keys():
        Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
        pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
    ts=time.time()
    endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    Record.write("End time: "+str(endtime)+"\n")
    pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
    Record.write("Conclusion:Patient was urged to go A&E")
    pdf.cell(60, 10, "Conclusion:Patient was urged to go A&E", 0,1,)
    pdf.output("Patient "+str(number)+".pdf", 'F')
    Record.close()    
def recordhelpful1(user_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    number=random.randrange(0,10000000)
    filename="Patient "+str(number)+".txt"
    Record  = open(filename, "w")
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    Record.write("Start time: "+user_data["starttime"]+"\n")
    pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
    Record.write("Age: "+user_data["age"]+"\n")
    pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
    Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
    pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
    if "surgery" in user_data.keys():
        Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
        pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
    if "score" in user_data.keys():
        Record.write("FLACC score: "+str(user_data["score"])+"\n")
        pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
    if "bleed" in user_data.keys():
        Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
        pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
    if "puswound" in user_data.keys():
        Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
        pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
    if "painmed" in user_data.keys():
        Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
        pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
    if "drain" in user_data.keys():
        Record.write("Draining function working?: "+user_data["drain"]+"\n")
        pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
    if "string" in user_data.keys():
        Record.write("Is the string intact?: "+user_data["string"]+"\n")
        pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
    if "hospital?" in user_data.keys():
        Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
        pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
    if "Past Symptoms" in user_data.keys():
        Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
        pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
    if "similar?" in user_data.keys():
        Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
        pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
    if "notunderstood" in user_data.keys():
        Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
    if "understood" in user_data.keys():
        Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
    if "entity" in user_data.keys():
        Record.write("Condition detected: "+user_data["entity"]+"\n")
        pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
    if "shitfrequency" in user_data.keys():
        Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
        pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
    if "strain?" in user_data.keys():
        Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
        pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
    if "bloodpoo" in user_data.keys():
        Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
        pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
    if "largestool?" in user_data.keys():
        Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
        pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
    if "painful?" in user_data.keys():
        Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
        pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
    if "bloated?" in user_data.keys():
        Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
        pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
    if "food" in user_data.keys():
        Record.write("Exposure to new food: "+user_data["food"]+"\n")
        pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
    if "diarrheaNo" in user_data.keys():
        Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
        pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
    if "vomitingNo" in user_data.keys():
        Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
        pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
    if "blooddiarrhea" in user_data.keys():
        Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
        pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
    if "bloodvomit" in user_data.keys():
        Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
        pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
    if "green" in user_data.keys():
        Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
        pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
    if "shoot" in user_data.keys():
        Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
        pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
    if "drink" in user_data.keys():
        Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
        pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
    ts=time.time()
    endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    Record.write("End time: "+str(endtime)+"\n")
    pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
    Record.write("Conclusion:Patient was given advice and found it helpful")
    pdf.cell(60, 10, "Conclusion:Patient was given advice and found it helpful", 0,1,)
    pdf.output("Patient "+str(number)+".pdf", 'F')
    Record.close()    
def recordnotagain(user_data):  
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    number=random.randrange(0,10000000)
    filename="Patient "+str(number)+".txt"
    Record  = open(filename, "w")
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    Record.write("Start time: "+user_data["starttime"]+"\n")
    pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
    Record.write("Age: "+user_data["age"]+"\n")
    pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
    Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
    pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
    if "surgery" in user_data.keys():
        Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
        pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
    if "score" in user_data.keys():
        Record.write("FLACC score: "+str(user_data["score"])+"\n")
        pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
    if "bleed" in user_data.keys():
        Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
        pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
    if "puswound" in user_data.keys():
        Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
        pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
    if "painmed" in user_data.keys():
        Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
        pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
    if "drain" in user_data.keys():
        Record.write("Draining function working?: "+user_data["drain"]+"\n")
        pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
    if "string" in user_data.keys():
        Record.write("Is the string intact?: "+user_data["string"]+"\n")
        pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
    if "hospital?" in user_data.keys():
        Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
        pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
    if "Past Symptoms" in user_data.keys():
        Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
        pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
    if "similar?" in user_data.keys():
        Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
        pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
    if "notunderstood" in user_data.keys():
        Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
    if "understood" in user_data.keys():
        Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
    if "entity" in user_data.keys():
        Record.write("Condition detected: "+user_data["entity"]+"\n")
        pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
    if "shitfrequency" in user_data.keys():
        Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
        pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
    if "strain?" in user_data.keys():
        Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
        pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
    if "bloodpoo" in user_data.keys():
        Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
        pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
    if "largestool?" in user_data.keys():
        Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
        pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
    if "painful?" in user_data.keys():
        Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
        pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
    if "bloated?" in user_data.keys():
        Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
        pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
    if "food" in user_data.keys():
        Record.write("Exposure to new food: "+user_data["food"]+"\n")
        pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
    if "diarrheaNo" in user_data.keys():
        Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
        pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
    if "vomitingNo" in user_data.keys():
        Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
        pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
    if "blooddiarrhea" in user_data.keys():
        Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
        pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
    if "bloodvomit" in user_data.keys():
        Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
        pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
    if "green" in user_data.keys():
        Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
        pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
    if "shoot" in user_data.keys():
        Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
        pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
    if "drink" in user_data.keys():
        Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
        pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
    ts=time.time()
    endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    Record.write("End time: "+str(endtime)+"\n")
    pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
    Record.write("Conclusion:Patient did not find it helpful and did not want to try again. Urged patient to go A&E")
    pdf.cell(60, 10, "Conclusion:Patient did not find it helpful and did not want to try again. Urged patient to go A&E", 0,1,)
    pdf.output("Patient "+str(number)+".pdf", 'F')
    Record.close() 
    
 #RELATED TO NOT HELPFUL   
def recordnothelpful(number,user_data):  #recording the second file where patient did not find it helpful the first time
    filename="Patient "+str(number)+".txt"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    Record  = open(filename, "a")
    Record.write("\n\nPatient did not find it helpful the first time, continuing attempt 2\n\n")
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    pdf.cell(60, 10, "Patient did not find it helpful the first time", 0,1,)
    pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
    #record dont need age and surgery, only pdf need
    pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
    pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
    if "surgery" in user_data.keys():
        Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
        pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
    if "score" in user_data.keys():
        Record.write("FLACC score: "+str(user_data["score"])+"\n")
        pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
    if "bleed" in user_data.keys():
        Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
        pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
    if "puswound" in user_data.keys():
        Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
        pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
    if "painmed" in user_data.keys():
        Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
        pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
    if "drain" in user_data.keys():
        Record.write("Draining function working?: "+user_data["drain"]+"\n")
        pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
    if "string" in user_data.keys():
        Record.write("Is the string intact?: "+user_data["string"]+"\n")
        pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
    if "hospital?" in user_data.keys():
        Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
        pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
    if "Past Symptoms" in user_data.keys():
        Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
        pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
    if "similar?" in user_data.keys():
        Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
        pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
    if "notunderstood" in user_data.keys():
        Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
    if "understood" in user_data.keys():
        Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
    if "entity" in user_data.keys():
        Record.write("Condition detected: "+user_data["entity"]+"\n")
        pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
    if "shitfrequency" in user_data.keys():
        Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
        pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
    if "strain?" in user_data.keys():
        Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
        pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
    if "bloodpoo" in user_data.keys():
        Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
        pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
    if "largestool?" in user_data.keys():
        Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
        pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
    if "painful?" in user_data.keys():
        Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
        pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
    if "bloated?" in user_data.keys():
        Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
        pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
    if "food" in user_data.keys():
        Record.write("Exposure to new food: "+user_data["food"]+"\n")
        pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
    if "diarrheaNo" in user_data.keys():
        Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
        pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
    if "vomitingNo" in user_data.keys():
        Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
        pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
    if "blooddiarrhea" in user_data.keys():
        Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
        pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
    if "bloodvomit" in user_data.keys():
        Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
        pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
    if "green" in user_data.keys():
        Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
        pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
    if "shoot" in user_data.keys():
        Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
        pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
    if "drink" in user_data.keys():
        Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
        pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
    endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    Record.write("End time: "+str(endtime)+"\n")
    pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
    Record.write("Conclusion:Patient did not find it helpful after a second try. Urged patient to go A&E")
    pdf.cell(60, 10, "Conclusion:Patient did not find it helpful after a second try. Urged patient to go A&E", 0,1,)
    pdf.output("Patient "+str(number)+"Second"+".pdf", 'F')
    Record.close() 

#
def recordtryagain(number,user_data): #i wrote in the old details first. Change this to another pdf file
    filename="Patient "+str(number)+".txt"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    Record  = open(filename, "w")
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    Record.write("Start time: "+user_data["starttime"]+"\n")
    pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
    Record.write("Age: "+user_data["age"]+"\n")
    pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
    Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
    pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
    if "surgery" in user_data.keys():
        Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
        pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
    if "score" in user_data.keys():
        Record.write("FLACC score: "+str(user_data["score"])+"\n")
        pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
    if "bleed" in user_data.keys():
        Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
        pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
    if "puswound" in user_data.keys():
        Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
        pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
    if "painmed" in user_data.keys():
        Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
        pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
    if "drain" in user_data.keys():
        Record.write("Draining function working?: "+user_data["drain"]+"\n")
        pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
    if "string" in user_data.keys():
        Record.write("Is the string intact?: "+user_data["string"]+"\n")
        pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
    if "hospital?" in user_data.keys():
        Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
        pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
    if "Past Symptoms" in user_data.keys():
        Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
        pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
    if "similar?" in user_data.keys():
        Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
        pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
    if "notunderstood" in user_data.keys():
        Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
    if "understood" in user_data.keys():
        Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
    if "entity" in user_data.keys():
        Record.write("Condition detected: "+user_data["entity"]+"\n")
        pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
    if "shitfrequency" in user_data.keys():
        Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
        pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
    if "strain?" in user_data.keys():
        Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
        pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
    if "bloodpoo" in user_data.keys():
        Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
        pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
    if "largestool?" in user_data.keys():
        Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
        pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
    if "painful?" in user_data.keys():
        Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
        pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
    if "bloated?" in user_data.keys():
        Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
        pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
    if "food" in user_data.keys():
        Record.write("Exposure to new food: "+user_data["food"]+"\n")
        pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
    if "diarrheaNo" in user_data.keys():
        Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
        pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
    if "vomitingNo" in user_data.keys():
        Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
        pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
    if "blooddiarrhea" in user_data.keys():
        Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
        pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
    if "bloodvomit" in user_data.keys():
        Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
        pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
    if "green" in user_data.keys():
        Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
        pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
    if "shoot" in user_data.keys():
        Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
        pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
    if "drink" in user_data.keys():
        Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
        pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
    ts=time.time()
    endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    Record.write("End time: "+str(endtime)+"\n")
    pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
    Record.write("Conclusion:Patient did not find it helpful and want to try again")
    pdf.cell(60, 10, "Conclusion:Patient did not find it helpful and want to try again", 0,1,)
    pdf.output("Patient "+str(number)+"First"+".pdf", 'F') #first file for same patient
    Record.close()   
    
def recordhelpful2(number,user_data): #found it helpful a second time
     filename="Patient "+str(number)+".txt"
     pdf = FPDF()
     pdf.add_page()
     pdf.set_xy(0, 0)
     pdf.set_font('arial', 'B', 13.0)
     Record  = open(filename, "w")
     pdf.cell(60, 10, "Patient "+str(number), 0,1,)
     Record.write("Start time: "+user_data["starttime"]+"\n")
     pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
     Record.write("Age: "+user_data["age"]+"\n")
     pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
     Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
     pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
     if "surgery" in user_data.keys():
         Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
         pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
     if "score" in user_data.keys():
         Record.write("FLACC score: "+str(user_data["score"])+"\n")
         pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
     if "bleed" in user_data.keys():
         Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
         pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
     if "puswound" in user_data.keys():
         Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
         pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
     if "painmed" in user_data.keys():
         Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
         pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
     if "drain" in user_data.keys():
         Record.write("Draining function working?: "+user_data["drain"]+"\n")
         pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
     if "string" in user_data.keys():
         Record.write("Is the string intact?: "+user_data["string"]+"\n")
         pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
     if "hospital?" in user_data.keys():
         Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
         pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
     if "Past Symptoms" in user_data.keys():
         Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
         pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
     if "similar?" in user_data.keys():
         Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
         pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
     if "notunderstood" in user_data.keys():
         Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
         pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
     if "understood" in user_data.keys():
         Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
         pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
     if "entity" in user_data.keys():
         Record.write("Condition detected: "+user_data["entity"]+"\n")
         pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
     if "shitfrequency" in user_data.keys():
         Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
         pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
     if "strain?" in user_data.keys():
         Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
         pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
     if "bloodpoo" in user_data.keys():
         Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
         pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
     if "largestool?" in user_data.keys():
         Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
         pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
     if "painful?" in user_data.keys():
         Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
         pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
     if "bloated?" in user_data.keys():
         Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
         pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
     if "food" in user_data.keys():
         Record.write("Exposure to new food: "+user_data["food"]+"\n")
         pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
     if "diarrheaNo" in user_data.keys():
         Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
         pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
     if "vomitingNo" in user_data.keys():
         Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
         pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
     if "blooddiarrhea" in user_data.keys():
         Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
         pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
     if "bloodvomit" in user_data.keys():
         Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
         pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
     if "green" in user_data.keys():
         Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
         pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
     if "shoot" in user_data.keys():
         Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
         pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
     if "drink" in user_data.keys():
         Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
         pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
     ts=time.time()
     endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
     Record.write("End time: "+str(endtime)+"\n")
     pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
     Record.write("Conclusion:Patient found it helpful a second time, educational resource given")
     pdf.cell(60, 10, "Conclusion:Patient found it helpful a second time, educational resource given", 0,1,)
     pdf.output("Patient "+str(number)+"Second"+".pdf", 'F') #first file for same patient
     Record.close()
     
    
    
def recordred2(number,user_data):
     filename="Patient "+str(number)+".txt"
     pdf = FPDF()
     pdf.add_page()
     pdf.set_xy(0, 0)
     pdf.set_font('arial', 'B', 13.0)
     Record  = open(filename, "w")
     pdf.cell(60, 10, "Patient "+str(number), 0,1,)
     Record.write("Start time: "+user_data["starttime"]+"\n")
     pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
     Record.write("Age: "+user_data["age"]+"\n")
     pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
     Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
     pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
     if "surgery" in user_data.keys():
         Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
         pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
     if "score" in user_data.keys():
         Record.write("FLACC score: "+str(user_data["score"])+"\n")
         pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
     if "bleed" in user_data.keys():
         Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
         pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
     if "puswound" in user_data.keys():
         Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
         pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
     if "painmed" in user_data.keys():
         Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
         pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
     if "drain" in user_data.keys():
         Record.write("Draining function working?: "+user_data["drain"]+"\n")
         pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
     if "string" in user_data.keys():
         Record.write("Is the string intact?: "+user_data["string"]+"\n")
         pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
     if "hospital?" in user_data.keys():
         Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
         pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
     if "Past Symptoms" in user_data.keys():
         Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
         pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
     if "similar?" in user_data.keys():
         Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
         pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
     if "notunderstood" in user_data.keys():
         Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
         pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
     if "understood" in user_data.keys():
         Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
         pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
     if "entity" in user_data.keys():
         Record.write("Condition detected: "+user_data["entity"]+"\n")
         pdf.cell(60, 10, "Condition detected: "+user_data["entity"], 0,1,)
     if "shitfrequency" in user_data.keys():
         Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
         pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
     if "strain?" in user_data.keys():
         Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
         pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
     if "bloodpoo" in user_data.keys():
         Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
         pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
     if "largestool?" in user_data.keys():
         Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
         pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
     if "painful?" in user_data.keys():
         Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
         pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
     if "bloated?" in user_data.keys():
         Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
         pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
     if "food" in user_data.keys():
         Record.write("Exposure to new food: "+user_data["food"]+"\n")
         pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
     if "diarrheaNo" in user_data.keys():
         Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
         pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
     if "vomitingNo" in user_data.keys():
         Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
         pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
     if "blooddiarrhea" in user_data.keys():
         Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
         pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
     if "bloodvomit" in user_data.keys():
         Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
         pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
     if "green" in user_data.keys():
         Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
         pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
     if "shoot" in user_data.keys():
         Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
         pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
     if "drink" in user_data.keys():
         Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
         pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
     ts=time.time()
     endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
     Record.write("End time: "+str(endtime)+"\n")
     pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
     Record.write("Conclusion:Patient got a redflag the second time, sent to A&E")
     pdf.cell(60, 10, "Conclusion:Patient got a redflag the second time, sent to A&E", 0,1,)
     pdf.output("Patient "+str(number)+"Second"+".pdf", 'F') #first file for same patient
     Record.close() 
def recordattempt(number,user_data,tryagain):
    filename="Patient "+str(number)+".txt"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 13.0)
    Record  = open(filename, "w")
    pdf.cell(60, 10, "Patient "+str(number), 0,1,)
    Record.write("Start time: "+user_data["starttime"]+"\n")
    pdf.cell(60, 10, "Start time: "+user_data["starttime"], 0,1,)
    Record.write("Age: "+user_data["age"]+"\n")
    pdf.cell(60, 10, "Age: "+user_data["age"], 0,1,)
    Record.write("Did child underwent surgery?: "+user_data["Surgery?"]+"\n")
    pdf.cell(60, 10, "Did child underwent surgery?: "+user_data["Surgery?"], 0,1,)
    if "surgery" in user_data.keys():
        Record.write("Type of Surgery: "+user_data["surgery"]+"\n")
        pdf.cell(60, 10, "Type of Surgery: "+user_data["surgery"], 0,1,)
    if "score" in user_data.keys():
        Record.write("FLACC score: "+str(user_data["score"])+"\n")
        pdf.cell(60, 10, "FLACC score: "+str(user_data["score"]), 0,1,)
    if "bleed" in user_data.keys():
        Record.write("Bleeding in wound?: "+user_data["bleed"]+"\n")
        pdf.cell(60, 10, "Bleeding in wound?: "+user_data["bleed"], 0,1,)
    if "puswound" in user_data.keys():
        Record.write("Pus in wound?: "+user_data["puswound"]+"\n")
        pdf.cell(60, 10, "Pus in wound?: "+user_data["puswound"], 0,1,)
    if "painmed" in user_data.keys():
        Record.write("Pain medicine working?: "+user_data["painmed"]+"\n")
        pdf.cell(60, 10, "Pain medicine working?: "+user_data["painmed"], 0,1,)
    if "drain" in user_data.keys():
        Record.write("Draining function working?: "+user_data["drain"]+"\n")
        pdf.cell(60, 10, "Draining function working?: "+user_data["drain"], 0,1,)
    if "string" in user_data.keys():
        Record.write("Is the string intact?: "+user_data["string"]+"\n")
        pdf.cell(60, 10, "Is the string intact?: "+user_data["string"], 0,1,)
    if "hospital?" in user_data.keys():
        Record.write("Admittance to hospital recently?: "+ user_data["hospital?"]+"\n")
        pdf.cell(60, 10, "Admittance to hospital recently?: "+ user_data["hospital?"], 0,1,)
    if "Past Symptoms" in user_data.keys():
        Record.write("Admitted for : "+ user_data["Past Symptoms"]+"\n")
        pdf.cell(60, 10, "Admitted for : "+ user_data["Past Symptoms"], 0,1,)
    if "similar?" in user_data.keys():
        Record.write("Similar Symptoms to previous admission? :"+user_data["similar?"]+"\n")
        pdf.cell(60, 10, "Similar Symptoms to previous admission? :"+user_data["similar?"], 0,1,)
    if "notunderstood" in user_data.keys():
        Record.write("Patient's problem that chatbot did not understood: "+user_data["notunderstood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot did not understood: "+user_data["notunderstood"], 0,1,)
    if "understood" in user_data.keys():
        Record.write("Patient's problem that chatbot understood: "+user_data["understood"]+"\n")
        pdf.cell(60, 10, "Patient's problem that chatbot understood: "+user_data["understood"], 0,1,)
    if "entity" in user_data.keys():
        Record.write("Condition detected: "+str(user_data["entity"])+"\n")
        pdf.cell(60, 10, "Condition detected: "+str(user_data["entity"]), 0,1,)
    if "shitfrequency" in user_data.keys():
        Record.write("Pass motion frequency per week: "+user_data["shitfrequency"]+"\n")
        pdf.cell(60, 10, "Pass motion frequency per week: "+user_data["shitfrequency"], 0,1,)
    if "strain?" in user_data.keys():
        Record.write("Straining to pass motion?: "+user_data["strain?"]+"\n")
        pdf.cell(60, 10, "Straining to pass motion?: "+user_data["strain?"], 0,1,)
    if "bloodpoo" in user_data.keys():
        Record.write("Blood in poo? :"+user_data["bloodpoo"]+"\n")
        pdf.cell(60, 10, "Blood in poo? :"+user_data["bloodpoo"], 0,1,)
    if "largestool?" in user_data.keys():
        Record.write("Presence of large stool? :"+ user_data["largestool?"]+"\n")
        pdf.cell(60, 10, "Presence of large stool? :"+ user_data["largestool?"], 0,1,)
    if "painful?" in user_data.keys():
        Record.write("Does patient find it painful to pass motion?: "+ user_data["painful?"]+"\n")
        pdf.cell(60, 10,"Does patient find it painful to pass motion?: "+ user_data["painful?"], 0,1,)
    if "bloated?" in user_data.keys():
        Record.write("Is patient bloated?: "+user_data["bloated?"]+"\n")
        pdf.cell(60, 10, "Is patient bloated?: "+user_data["bloated?"], 0,1,)
    if "food" in user_data.keys():
        Record.write("Exposure to new food: "+user_data["food"]+"\n")
        pdf.cell(60, 10, "Exposure to new food: "+user_data["food"], 0,1,)
    if "diarrheaNo" in user_data.keys():
        Record.write("Number of diarrhea per day: "+user_data["diarrheaNo"]+"\n")
        pdf.cell(60, 10, "Number of diarrhea per day: "+user_data["diarrheaNo"], 0,1,)
    if "vomitingNo" in user_data.keys():
        Record.write("Number of vomits per day: "+user_data["vomites"]+"\n")
        pdf.cell(60, 10, "Number of vomits per day: "+user_data["vomites"], 0,1,)
    if "blooddiarrhea" in user_data.keys():
        Record.write("Presence of blood in diarrhea: "+user_data["blooddiarrhea"]+"\n")
        pdf.cell(60, 10, "Presence of blood in diarrhea: "+user_data["blooddiarrhea"], 0,1,)
    if "bloodvomit" in user_data.keys():
        Record.write("Presence of blood in vomit: "+user_data["bloodvomit"]+"\n")
        pdf.cell(60, 10, "Presence of blood in vomit: "+user_data["bloodvomit"], 0,1,)
    if "green" in user_data.keys():
        Record.write("Presence of greenish fluid in vomit: "+user_data["green"]+"\n")
        pdf.cell(60, 10, "Presence of greenish fluid in vomit: "+user_data["green"], 0,1,)
    if "shoot" in user_data.keys():
        Record.write("Vomit shoots out?: "+user_data["shoot"]+"\n")
        pdf.cell(60, 10, "Vomit shoots out?: "+user_data["shoot"], 0,1,)
    if "drink" in user_data.keys():
        Record.write("Does child want to drink water?: "+user_data["drink"]+"\n")
        pdf.cell(60, 10,"Does child want to drink water?: "+user_data["drink"], 0,1,)
    ts=time.time()
    endtime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    Record.write("End time: "+str(endtime)+"\n")
    pdf.cell(60, 10, "End time: "+str(endtime), 0,1,)
    Record.write("Conclusion:Chatbot did not understand text input. Patient was urged to go A&E")
    pdf.cell(60, 10, "Conclusion:Chatbot did not understand text input. Patient was urged to go A&E", 0,1,)
    if tryagain==1:
        pdf.output("Patient "+str(number)+"Second"+".pdf", 'F') #second file for same patient
    else:
        pdf.output("Patient "+str(number)+".pdf", 'F')
    Record.close() 