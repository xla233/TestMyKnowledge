'''
Testing your knowledge
'''

import random as r
import os.path
##os.path.isfile(fname)  gives whether the file exists


def read_string_list_from_file(file):
    file_content = open(file, "r")
    file_list = []
    for line in file_content:
        string = line[0:len(line)-1]
        file_list.append(string)

    file_content.close()
    return file_list

def list_trans(student_list1):  #Transforms the student_list to [['AAAA','12344'],...] format and 'kills' the spaces
    for i in range(len(student_list1)):   #student_list1 is a local var
        s = 0                                #s will be the number of spaces in the file
        for x in range(len(student_list1[i])):
            if student_list1[i][x] == '~':
                s += 1
                #print('TRACE s =',s)
        if s > 0:
            student_list1[i] = student_list1[i].split('~'*s)
            #print('TRACE student_list1[i]=',student_list1[i],'s=',s)
    return student_list1

def q_list(ans_key):
    stud_empty = []
    for i in range(len(ans_key)):
        stud_empty.append(i)
    return stud_empty

def random_qs(ans,q_list):
    i = 0
    q = [] + q_list
    stud_answers_list = []
    qs_asked = []
    stud_choice = input('Would you like to start answering?input END to end:').upper()
    if stud_choice != 'END' and len(q) > 0:
        #print('TRACE len(q)=',len(q))
        print('')
        r1 = r.choice(q)
        print('Q',r1+1,'Whats is/are',ans[r1][0],'? \n')
        stud_ans = input('You have one chance:')
        while stud_ans != 'END' and len(q) > 0:
            #print('TRACE len(q)=',len(q))
            print('')
            print('You answered "',stud_ans,'"for Q',r1+1)
            print('')
            stud_answers_list.append(stud_ans)
            qs_asked.append(r1)
            q.remove(r1)
            if len(q) > 0:
                r1 = r.choice(q)
                print('Q',r1+1,'Whats is/are',ans[r1][0],'? \n')
                stud_ans = input('You have one chance:')
    if len(q) == 0:
        print('\nWOW, you answered ALL of the questions!')
    res = [stud_answers_list] + [qs_asked]    #[[x,x,x,x],[#,#,#,#,#]],xxxx will be the answers, #### will be the question numbers
    print('')
    return res

def random_qs1(ans,q_list):
    i = 0
    q = [] + q_list
    stud_answers_list = []
    qs_asked = []
    stud_choice = input('Would you like to start answering? END to end:').upper()
    if stud_choice != 'END' and len(q) > 0:
        #print('TRACE len(q)=',len(q))
        r1 = r.choice(q)
        print('\nQ',r1+1,ans[r1][0],'? \n')
        stud_ans = input('You have one chance:')
        while stud_ans != 'END' and len(q) > 0:
            #print('TRACE len(q)=',len(q))
            print('')
            print('You answered "',stud_ans,'" for Q',r1+1)
            stud_answers_list.append(stud_ans)
            qs_asked.append(r1)
            q.remove(r1)
            if len(q) > 0:
                r1 = r.choice(q)
                #print('TRACE r1=',r1)
                print('\nQ',r1+1,ans[r1][0],'? \n')
                stud_ans = input('You have one chance:')
    if len(q) == 0:
        print('\nWOW, you answered ALL of the questions!')
    res = [stud_answers_list] + [qs_asked]    #[[x,x,x,x],[#,#,#,#,#]],xxxx will be the answers, #### will be the question numbers
    print('')
    return res


def checking(stud_answers,ans_key):
    print('Checking The answers! \n')
    points = 0
    wrong_qs1 = []
    for i in range(len(stud_answers[0])):
        print('\n You answered "',stud_answers[0][i],'" for Q',stud_answers[1][i] + 1,', "',ans_key[stud_answers[1][i]][0],'" and the correct answer is "',ans_key[stud_answers[1][i]][1],'"')
        y = input("Did you get answer it correctly?input y if it's correct:")
        print('')
        if y in 'Yy':
            points += 1
        else:
            wrong_qs1.append(['Q:',ans_key[stud_answers[1][i]][0],'answer:',ans_key[stud_answers[1][i]][1],'end'])  #one element containing 5 items is appeneded
    print('')
    print('You got',points,'points in total out of',len(ans_key),'Qs. Keep it up!')
    return wrong_qs1


#============================================
#Top level
print('Please ensure there are only "~"s between the question and answer. \n')
print("Please ensure there isn't any extra spaces in the txt document. \n")
print('Please note "What is"..."?" will be added to your questions if asked. No need to write it out on the notes. :) \n')
print('Questions are in random order \n')
knowledge = input("Please enter the file name here (I'll add .txt for you) =>")
knowledge += '.txt'

while os.path.isfile(knowledge) == False:
    print("Opps, I cannot seem to file the file",knowledge,",can you re-enter the file name?")
    knowledge = input("Please write a different file name here (I'll add .txt for you) =>")
    knowledge += '.txt'
    

print("Great! I have found the file now!")

##   anskey = read_string_list_from_file('MATH154 must remember.txt')
print('')
anskey = read_string_list_from_file(knowledge)
anskey = list_trans(anskey)
q_list = q_list(anskey)
what = input("Would you like me to add 'what is' to your questions? [If your file name doesn't have '-n', then it NEEDS 'What is']input y if yes=>")
print('')
if what in 'Yy':
    answers = random_qs(anskey,q_list)
else:
    answers = random_qs1(anskey,q_list)

print('======================================================')
wrong_qs = checking(answers,anskey)

if len(wrong_qs) > 0:
    print('You got some questions wrong, here are the questions and corresponding correct answers, please remember them. :)')
    for i in range (len(wrong_qs)):
        for q in range (len(wrong_qs[i])):
            print(wrong_qs[i][q])
        

ending_choice = input('After you finish reviewing, input anything to end the program.')
