# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:45:44 2018

@author: User
"""
 
##processing counts
def RedFlag(Record):
    Record.write("\nSENT TO A&E")
    print("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
    return 
def RedFlag2(Record):
    Record.write("\nSENT TO A&E")
    print("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074.")
    return 
def ProcessSequence(SequenceCount):
    if SequenceCount==6:
        return 1
    else:
        SequenceCount+=1
        return SequenceCount

def ProcessCorrectCount(CorrectCount,Record,NormalCount): #need normal count to determine when to give resource
    if CorrectCount<3 and NormalCount>=5: #5 cause process correct count comes before normal count
        print("Relevant educational resource")
        return "hi"
    elif CorrectCount>=3:
        RedFlag2(Record)
        return 10
def ProcessNormalCount(NormalCount,ProcessedCorrectCount):
    if ProcessedCorrectCount==10:
        NormalCount=7
        return NormalCount
    else:
        NormalCount+=1
        return NormalCount
    
def FunctionalConstipation(value,Record):
    CorrectCount=0
    NormalCount=0
    SequenceCount=0
    Yes_No_Check=["1","2"]
    DontUnderstand="Sorry i don't understand."
    QuestionInstructions="\nPlease enter: \n 1 for Yes \n 2 for No\n"
    PassMotionQuestionInstructions="\nPlease enter sensible numeric answers. e.g 2 if your child pass motion twice a week\n"
   
    Question_Index={"not passing motion":1,"straining":2,"blood poo":3,"large stool":4,"painful":5,"bloated":6}
    Question_Dictionary={"1":"How many times is your child passing motion in 1 week?","2":"Does your child have to strain when passing motion?","3":"Is there any blood when your child passes motion?","4":"Does your child usually pass large sized stools?","5":"Is it painful when your child passes motion?","6":"Is your child's belly bloated?"}
    
    SequenceCount=Question_Index[value] #get first relevant question
    while NormalCount<6:
        if SequenceCount==1:
            key=str(SequenceCount)
            #To make sure we can process the integer that the user input
            while True:
                try:
                    Question=int(input(Question_Dictionary[key]+PassMotionQuestionInstructions))
                    while Question<0:
                        Question=input(DontUnderstand+Question_Dictionary[key]+PassMotionQuestionInstructions)
                        Question=int(Question)
                    break
                except ValueError:
                    print(DontUnderstand)
            if Question<3 and Question>=0:
                CorrectCount+=1
            Record.write("\n"+Question_Dictionary[key]+":"+str(Question))
            a=ProcessCorrectCount(CorrectCount,Record,NormalCount)
            NormalCount=ProcessNormalCount(NormalCount,a) #to make sure we dont repeat questions, and stop when flagged
            ProcessCorrectCount(CorrectCount,Record,NormalCount) ##necessary to repeat twice to give relevant resource...
            SequenceCount=ProcessSequence(SequenceCount)# ask questions sequentially
            
        else:
            #to check if it is redflag question
            if SequenceCount==3 or SequenceCount==6:
                key=str(SequenceCount)
                Question=input(Question_Dictionary[key]+QuestionInstructions)
                while Question not in Yes_No_Check:
                    Question=input(DontUnderstand+Question_Dictionary[key]+QuestionInstructions)
                Record.write("\n"+Question_Dictionary[key]+":"+str(Question))
                NormalCount=ProcessNormalCount(NormalCount,a)###PROBLEM PRINT EDUCATION RESOURCE
                SequenceCount=ProcessSequence(SequenceCount)
                if Question=="1":
                    RedFlag(Record)
                    return 1
            else:
                 key=str(SequenceCount)
                 Question=input(Question_Dictionary[key]+QuestionInstructions)
                 while Question not in Yes_No_Check:
                     Question=input(DontUnderstand+Question_Dictionary[key]+QuestionInstructions)
                 if Question=="1":
                     CorrectCount+=1
                 Record.write("\n"+Question_Dictionary[key]+":"+str(Question))
                 a=ProcessCorrectCount(CorrectCount,Record,NormalCount)
                 NormalCount=ProcessNormalCount(NormalCount,a)
                 #print(NormalCount)
                 SequenceCount=ProcessSequence(SequenceCount)
    if a==10:
        return 1
    else:
        print("relevant constipation resource")
        return 0
    #when normalcount>6, go to did you find this helpful from interpreter file     
    return
def GastroEnteritis(value):
    return
def Feeding(value):
    return

# return to two flcc question if is the other things
def RelevantCondition(Dictionary,Record):
    Entity=Dictionary['entities'][0]['entity']
    Value=Dictionary['entities'][0]['value']
    if Entity=='Constipation':
        return FunctionalConstipation(Value,Record)      
    elif Entity=='Drain':
        Record.write("Billary Drainage problem")
        return 'Drain'
    elif Entity=='Wound':
        Record.write("Circumcision wound problem")
        return 'Wound'