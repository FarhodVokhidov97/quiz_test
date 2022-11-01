from traceback import print_tb


quize = {
    "question1":{
        'question':'what is the capital of France?',
        'answer':'Paris'
    },
    "question2":{
        'question':'what is the capital of Germany?',
        'answer':'Berlin'
    },
    "question3":{
        'question':'what is the capital of Italy?',
        'answer':'Rome'
    },
    "question4":{
        'question':'what is the capital of Spain?',
        'answer':'Madrid'
    },
    "question5":{
        'question':'what is the capital of Portugal?',
        'answer':'Lisbon'
    },
    "question6":{
        'question':'what is the capital of Switzerland?',
        'answer':'Bern'
    },
    "question6":{
        'question':'what is the capital of Austria?',
        'answer':'Vienna'
    }
}
score = 0

for key,value in quize.items():
    print(value['question'])
    anwer = input("answer= ")

    if anwer.lower() == value['answer'].lower():
        print('Corrent')
        score = score + 1
        print("Your Score is :"+str(score))
        print("")
        print("")
        
    else:
        print("Wrong!")
        print("The answer is :" + value['answer'] )
        print("Your score is:" + str(score))
        print("")
        print("")

print("You got" + str(score)+" out of 7 questions correctly")
print("Your percentage is " + str(score/7*100)+'%')