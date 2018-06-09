# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:35:36 2018

@author: User
"""

def CorrectCount(entity,value,text,CorrectCount,SequenceCount):
    if entity=="Constipation":
        options=["0","1","2"]
        print(value)
        if value=="not passing motion" or SequenceCount==1:
                if text in options:
                    return CorrectCount
                else:
                    CorrectCount+=1
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
    if start==1: #output value question and updated sequence count, when sequence count is 0, update to value's index
        question_index=str(Question_Index[value]) #derive from current value
        SequenceCount=Question_Index[value] #update the sequence count to its rightful number
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
        question_index=str(Question_Index[value]) #derive from current value
        SequenceCount=Question_Index[value] #update the sequence count to its rightful number
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