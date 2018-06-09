# -*- coding: utf-8 -*-
"""
Created on Fri May 25 01:16:53 2018

@author: User
"""

from RasaNLU import interpreter 
import ConditionQuestions as cd
#print(interpreter.parse(u"my child is not passing motion"))

##today create for surgerical conditions

#write functions
#functions to write into record
def WriteAge(firstinput):
    if firstinput=="1":
        return "Patient age: 0-3mths"
    elif firstinput =="2":
        return "Patient age: 3-6mths"
    elif firstinput =="3":
        return "Patient age: 6-12mths"
    elif firstinput =="4":
        return "Patient age: 12-24mths"
    elif firstinput =="5":
        return "Patient age: 2-5yrs"
    elif firstinput =="6":
        return "Patient age: 5-10yrs"
    elif firstinput =="7":
        return "Patient age: More than 10yrs"
    
def WriteSurgeryRecently(secondinput):
    if secondinput=="2":
        return "Surgery recently: No\n"
    elif secondinput=="1":
        return "Surgery recently: Yes\n"
    
def WriteWhichSurgery(surgeryinput):
    if surgeryinput=="1":
        return "Surgery underwent: Circumcision\n"
    elif surgeryinput=="2":
        return "Surgery underwent: Billary Drainage\n"
    
def WriteBleeding(bleedinginput):
    if bleedinginput=="1":
        return "Bleeding: Yes\n"
    elif bleedinginput=="2":
        return "Bleeding: No\n"

def WritePus(rfpusinput):
    if rfpusinput=="1":
        return "Pus in Wound: Yes\n"
    elif rfpusinput=="2":
        return "Pus in Wound: No\n"

def WriteFluid(fluidinput):
    if fluidinput=="1":
        return "Fluid coming out of drain: Yes\n"
    elif fluidinput=="2":
        return "Fluid coming out of drain: No\n"

def WriteDrain(draininput):
    if draininput=="1":
        return "String of drain intact: Yes\n"
    elif draininput=="2":
        return "String of drain intact: No\n" 
def WritePastAdmit(admittedinput,pastconditions):
    if admittedinput=="1":
        if pastconditions=="1":
            return"Admitted to hospital recently?: Yes\nAdmitted condition: Asthma"
        elif pastconditions=="2":
            return"Admitted to hospital recently?: Yes\nAdmitted condition: Gastroentritis"
        elif pastconditions=="3":
            return"Admitted to hospital recently?: Yes\nAdmitted condition: Severe infection"
        elif pastconditions=="4":
            return"Admitted to hospital recently?: Yes\nAdmitted condition: Fits"
    elif admittedinput=="2":
        return "Admitted to hospital recently?: No"

#processing input
def ProcessFLACC(score):
    if score<6:
        return 0
    elif score>=6:
        #print("hi")
        return 1

#categorial questions
def RedFlag(Record):
    Record.write("\nSENT TO A&E")
    print("Please come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
    return 
def RedFlagSimilar(Record,pastconditioninput):
   
    if pastconditioninput=="1":
        
        Record.write("\nSENT TO A&E FOR POSSIBLE RECURRENCE OF ASTHMA")
        
        print("A recurrence of Asthma can have serious implications.\nPlease come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
    if pastconditioninput=="2":
        Record.write("\nSENT TO A&E FOR POSSIBLE RECURRENCE OF GASTROENTERITIS")
        
        print("A recurrence of Gastroenteritis can have serious implications.\nPlease come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
    if pastconditioninput=="3":
        Record.write("\nSENT TO A&E FOR POSSIBLE RECURRENCE OF INFECTION")
       
        print("A recurrence of Infection can have serious implications.\nPlease come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
    if pastconditioninput=="4":
        Record.write("\nSENT TO A&E FOR POSSIBLE RECURRENCE OF FITS")
        print("A recurrence of Fits can have serious implications.\nPlease come to our Childrens' Emergency at 5 Lower Kent Ridge Road, 119074. One of our Specialist Nurse will be calling your registered Phone Number to check on you in 10 mins.")
    return 1

def CompileFLACC(Record):
    Yes_No_Check=["1","2","3"]
    FLACCscore=0
    FirstQuestion="We will assess how severe the pain your child is experiencing"
    QuestionInstructions="\nPlease enter 1, 2 or 3 according to the labels in the question\n"
    DontUnderstand="Sorry i don't understand "
    One1="\n1. smiling or showing no particular expression"
    One2="\n2. shows the occasional grimice or frown or is withdrawn or uninterested "
    One3="\n3. Is frequently quivering his/her chin or is clenching his/her jaw\n"
    One=" \nObserving your child's expression he/she shows signs of:"+One1+One2+One3
    
    Two1="\n1. Normal position or relaxed"
    Two2="\n2. Uneasiness, restless or tense "
    Two3="\n3. Kicking, or legs drawn up\n"
    Two=" \nObserving your child's leg movements he/she shows signs of:"+Two1+Two2+Two3
    
    Three1="\n1. Lying quietly, normal position, moves easily"
    Three2="\n2. Squirming, shifting, back and forth, tense "
    Three3="\n3. Arched in pain, rigid or jerking\n"
    Three=" \nObserving your child's body behaviour he/she shows signs of:"+Three1+Three2+Three3
    
    Four1="\n1. Not crying"
    Four2="\n2. Moaning or whimpering; occasional complaint "
    Four3="\n3. Crying steadily, screams or sobs, frequent complaints\n"
    Four=" \nObserving your child's cry he/she shows signs of"+Four1+Four2+Four3
    
    Five1="\n1. Content, relaxed"
    Five2="\n2. Reassured by occasional touching, hugging or being talked to, distractible "
    Five3="\n3. Difficult to console or comfort\n"
    Five=" \nHow consolable is your child? he/she is:"+Five1+Five2+Five3
    
    OneRecord="Face:"
    TwoRecord="\nLeg:"
    ThreeRecord="\nActivity:"
    FourRecord="\nCrying:"
    FiveRecord="\nConsolability:"
    
    Record.write("Answers to question on circumcision"+"\n")
    OneInput=input(FirstQuestion+One+QuestionInstructions)
    while OneInput not in Yes_No_Check:
        OneInput=input(DontUnderstand+QuestionInstructions+One)
    if OneInput=="1":
        FLACCscore+=0
        Record.write(OneRecord+One1)
    elif OneInput=="2":
        FLACCscore+=1
        Record.write(OneRecord+One2)
    elif OneInput=="3":
        FLACCscore+=2
        Record.write(OneRecord+One3)
    
    TwoInput=input(Two+QuestionInstructions)
    while TwoInput not in Yes_No_Check:
        TwoInput=input(DontUnderstand+QuestionInstructions+Two)
    if TwoInput=="1":
        FLACCscore+=0
        Record.write(TwoRecord+Two1)
    elif TwoInput=="2":
        FLACCscore+=1
        Record.write(TwoRecord+Two2)
    elif TwoInput=="3":
        FLACCscore+=2
        Record.write(TwoRecord+Two3)
        
    if FLACCscore<6:
        ThreeInput=input(Three+QuestionInstructions)
        while ThreeInput not in Yes_No_Check:
            ThreeInput=input(DontUnderstand+QuestionInstructions+Three)
        if ThreeInput=="1":
            FLACCscore+=0
            Record.write(ThreeRecord+Three1)
        elif ThreeInput=="2":
            FLACCscore+=1
            Record.write(ThreeRecord+Three2)
        elif ThreeInput=="3":
            FLACCscore+=2
            Record.write(ThreeRecord+Three3)
        ProcessFLACC(FLACCscore)
    
    if FLACCscore<6:
        FourInput=input(Four+QuestionInstructions)
        while FourInput not in Yes_No_Check:
            FourInput=input(DontUnderstand+QuestionInstructions+Four)
        if FourInput=="1":
            FLACCscore+=0
            Record.write(FourRecord+Four1)
        elif FourInput=="2":
            FLACCscore+=1
            Record.write(FourRecord+Four2)
        elif FourInput=="3":
            FLACCscore+=2
            Record.write(FourRecord+Four3)
        ProcessFLACC(FLACCscore)
    
    if FLACCscore<6:
        FiveInput=input(Five+QuestionInstructions)
        while FiveInput not in Yes_No_Check:
            FiveInput=input(DontUnderstand+QuestionInstructions+One)
        if FiveInput=="1":
            FLACCscore+=0
            Record.write(FiveRecord+Five1)
        elif FiveInput=="2":
            FLACCscore+=1
            Record.write(FiveRecord+Five2)
        elif FiveInput=="3":
            FLACCscore+=2
            Record.write(FiveRecord+Five3)
    Record.write("\nFLACCScore: "+ str(FLACCscore)+"\n")
    return ProcessFLACC(FLACCscore)
        
def CircumcisionQuestions(Record): #questions, if no problem continue flow to ask for input'
    DontUnderstand="Sorry i don't understand. "
    Yes_No_Check=["1","2"]
    RF=CompileFLACC(Record)
    QuestionInstructions="\nPlease enter: \n 1 for Yes \n 2 for No\n"
    #Record= open("Patient record.txt", "a")
    #print("hihi")
    if RF==1:
        #print("hi2")
        RedFlag(Record) ###need to end chatbot here******  
        return 1
    
    else:        
        BleedingQuestion= "Is there any bleeding?"
        BleedInput=input(BleedingQuestion+QuestionInstructions)
        while BleedInput not in Yes_No_Check:
            BleedInput=input(DontUnderstand+BleedingQuestion+QuestionInstructions)
        Record.write(WriteBleeding(BleedInput)+"\n")
        
        RFPusquestion="Is there any pus around the wound?"
        RFPusInput=input(RFPusquestion+QuestionInstructions)
        while RFPusInput not in Yes_No_Check:
            RFPusInput=input(DontUnderstand+RFPusquestion+QuestionInstructions)
        Record.write(WritePus(RFPusInput)+"\n")
        if RFPusInput=="1":
            RedFlag(Record)
            return 1
        
        else:
            PainMedicationQuestion="Does giving the child prescribed pain medication help?"
            PainInput=input(PainMedicationQuestion+QuestionInstructions)
            while PainInput not in Yes_No_Check:
                PainInput=input(DontUnderstand+PainMedicationQuestion+QuestionInstructions)
            Record.write(WriteBleeding(PainInput)+"\n")
        if PainInput=="2" and BleedInput=="1":
            RedFlag(Record)
            return 1
        else:
            #Record.close()
            print("Here are some educational resource on circumcision for your child\n" )
            return 0#potential for continuation
    
    
def BillaryDrainageQuestions(Record):    
    DontUnderstand="Sorry i don't understand.\n"
    Yes_No_Check=["1","2"]
    RF=CompileFLACC(Record)
    QuestionInstructions="\nPlease enter: \n 1 for Yes \n 2 for No\n"
    #Record= open("Patient record.txt", "a")
    if RF==1:
        RedFlag(Record) ###need to end chatbot here******  
        return 1    
    else:        
        FluidQuestion= "Is there fluid coming out of drain?"
        FluidInput=input(FluidQuestion+QuestionInstructions)
        while FluidInput not in Yes_No_Check:
            FluidInput=input(DontUnderstand+FluidQuestion+QuestionInstructions)
        Record.write(WriteFluid(FluidInput)+"\n")
        if FluidInput=="1":
            RedFlag(Record)
            return 1
        
        DrainQuestion="Is the string around the drain intact"
        DrainInput=input(DrainQuestion+QuestionInstructions)
        while DrainInput not in Yes_No_Check:
            DrainInput=input(DontUnderstand+DrainQuestion+QuestionInstructions)
        Record.write(WriteDrain(DrainInput)+"\n")
        if DrainInput=="2":
            RedFlag(Record)
            return 1
        else:
            #Record.close()
            print("Educational resource on Draining" )
            return 0###potential for continuation
            
def PossibleConditions(Record): 
    OpeningQuestion=input("Alright, What seems to be the problem\n")
    Dictionary=interpreter.parse(OpeningQuestion)
    
    #condition to keep asking if cannot capture entity
    while Dictionary['entities']==[]:
        OpeningQuestion=input("Sorry, i cannot understand, can you tell me your problem again? if i still cant understand you after many tries, please seek help at A&E\n")
        Dictionary=interpreter.parse(OpeningQuestion)
        
    print(Dictionary)
    #extract entity value and value of value to give relevant question
    #Close and open file again?
    #Record.close()
    #Record=open("Patient record.txt", "a")
    OperateQuestions=cd.RelevantCondition(Dictionary) #start asking questions
    if OperateQuestions=="Drain":
        return BillaryDrainageQuestions() #return 0
    elif OperateQuestions=="Wound":
        return CircumcisionQuestions() #return 0
    else:
        return OperateQuestions #might be 0 or 1
    
###CHATBOT CONVERSATION FLOW
def startprocess():
    ##initial questions##
    HelpCount=0
    Helpful='1'
    while Helpful=='1':
        if HelpCount==0:
            FirstQuestion="Sorry, the doctor is not in at the moment, my name is Docs, i am here to help you understand your child's symptoms better.\nCan you tell me how old your child is ?  "
        else:
            FirstQuestion="Can you tell me how old your child is again ?"
        FirstQuestionInstructions= " \nPlease enter: \n 1 if your child is 0-3mths old\n 2 for 3-6mths\n 3 for 6-12mths\n 4 for 12-24mths\n 5 for 2-5years\n 6 for 5-10years\n 7 for >10years\n"
        FirstCheck=["1","2","3","4","5","6","7"]
        FirstInput=input(FirstQuestion+FirstQuestionInstructions) 
        DontUnderstand="Sorry i don't understand. "
        while FirstInput not in FirstCheck:
            FirstInput=input(DontUnderstand+FirstQuestionInstructions)
        Record  = open("Patient record.txt", "w") 
        Record.write(WriteAge(FirstInput)+"\n")
        
        Yes_No_Check=["1","2"]
        SecondQuestion="Did your child just undergo a surgery recently?"
        SecondQuestionInstructions="\nPlease enter: \n 1 for Yes \n 2 for No\n"
        SecondInput=input(SecondQuestion+SecondQuestionInstructions)
        while SecondInput not in Yes_No_Check:
            SecondInput=input(DontUnderstand+SecondQuestion+SecondQuestionInstructions)
        Record.write(WriteSurgeryRecently(SecondInput))
        
        QuestionInstructions="\nPlease enter: \n 1 for Yes \n 2 for No\n"
        
        ##start questions about operation##
        if SecondInput=="1":
            SurgeryInputInstructions="\nPlease enter: \n 1 for Circumcision \n 2 for Biliary Drainage\n"
            SurgeryQuestion="What surgery did your child underwent?"
            SurgeryInput=input(SurgeryQuestion+SurgeryInputInstructions)
            while SurgeryInput not in Yes_No_Check:
                SurgeryInput=input(DontUnderstand+SurgeryQuestion+SurgeryInputInstructions)
            Record.write(WriteWhichSurgery(SurgeryInput))
            #Record.close()
        
            ##seperate out to circumcision and billary drainage questions
            if SurgeryInput=="1":
                Exit=CircumcisionQuestions(Record)
                if Exit==1:
                    Record.close()
                    return
                elif Exit==0:
                    Exit=PossibleConditions(Record) #continue normal flow
                    if Exit==1:
                        Record.close()
                        return
                    
            elif SurgeryInput=="2":
                Exit=BillaryDrainageQuestions(Record)
                if Exit==1:
                    Record.close()
                    return
                elif Exit==0:
                    Exit=PossibleConditions(Record) #continue normal flow
                    if Exit==1:
                        Record.close()
                        return
        else:
            
            ##adimission to hospital##
            #Record= open("Patient record.txt", "a") #Dont need this as it is already opened and not closed 
            AdmittedQuestion="Have your child been admitted to hospital recently?"
            AdmittedInput=input(AdmittedQuestion+QuestionInstructions)
            while AdmittedInput not in Yes_No_Check:
                AdmittedInput=input(DontUnderstand+AdmittedQuestion+QuestionInstructions)
            if AdmittedInput=="1":
                check_condition=["1","2","3","4"]
                PastConditionQuestion="Was he admitted for any of these conditions?"
                ConditionQuestionInstructions="\nPlease enter: \n 1 for Asthma \n 2 for Gastroentritis \n 3 for Severe Infection \n 4 for Fits\n"
                PastConditionInput=input(PastConditionQuestion+ConditionQuestionInstructions)
                while PastConditionInput not in check_condition:
                    PastConditionInput=input(DontUnderstand+PastConditionQuestion+ConditionQuestionInstructions)
                Record.write(WritePastAdmit(AdmittedInput,PastConditionInput))
                
                ##Question on if child display similar symptom
                SimilarQuestion="Are the symptoms similar to that previous admission?"
                SimilarInput=input(SimilarQuestion+QuestionInstructions)
                while SimilarInput not in Yes_No_Check:
                    SimilarInput=input(DontUnderstand+SimilarQuestion+QuestionInstructions)
                if SimilarInput=="1":
                    Record.write("\nSymptoms:Similar to previous admission\n")
                    RedFlagSimilar(Record,PastConditionInput)
                    Record.close()
                    return
                elif SimilarInput=="2":
                    Record.write("\nSymptoms: Not similar to previous admission\n")
                    
                    ##OPENING QUESTION WHERE RASA NLU COMES IN
                    Exit=PossibleConditions(Record)
                    if Exit==1:
                        Record.close()
                        return
            elif AdmittedInput=="2":
                Exit=PossibleConditions(Record)
                if Exit==1:
                    Record.close()
                    return
                
            #ask if it is helpful?    
        HelpQuestion=input("Did you find this helpful?"+"\nPlease enter: \n 1 for Yes \n 2 for No\n")
        while HelpQuestion not in Yes_No_Check:
            HelpQuestion=input(DontUnderstand+"\nDid you find this helpful?"+QuestionInstructions)
        if HelpQuestion=='1':
            Record.write("\nDid patient find Docs helpful?: Yes")
            Record.close()
            Helpful=='helpful'
            return
        elif HelpQuestion=='2':
            HelpCount+=1
            if HelpCount<2:
                print("\nDocs is sorry :(, lets try again to better understand your child's situation")
            else:
                print("I am sorry, please bring your child to A&E ASAP!")
                Record.write("\nDid patient find Docs helpful?: No")
                Record.close()
                Helpful='Not helpful'
                    
        
    
    
startprocess()

    