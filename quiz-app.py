
questions = {
     "What Country Has The Most Vending Machines Per Capita?": "A",
     "What Was The First Toy To Be Advertised On Television? ": "B",
     "What Is The Most Frequently Sold Item At Walmart? ": "C",
     "What Are The Folds Of Skin On A Cat's Ears Called? ": "A",
     "On Average, How Long Does It Take Food To Pass Through The Human Body?":"D",
     "Which Country Owns Every Panda In The World?":"A",
     "Who Invented The Word Vomit?":"B",
     "Ph.D. Stands For What?":"C",
     "Which Country Has Not Fought A War Since 1814?":"D",
     "What Is The Second Smallest Country In The World?":"B"
}
options=[["A. japan","B. india","C. china","D. amarica"],
         ["A. mr. Potato","B. mr. potato Head","C. mr. Head","D. mr. "],
         ["A. orange","B. Apple","C. banana","D. juice"],
         ["A. henry's pockets","B. pockets","C. henry's","D. no Thing"],
         ["A. 52 hours","B. 51 hours","C. 50 hours","D. 53 hours"],
         ["A. china","B. eygpt","C. india","D. united kingdom"],
         ["A. ineshtine","B. william shakespeare","C. ibn Sina","D. ibn alhaitham"],
         ["A. philosophy","B. doctor","C. doctor of philosophy","D. all these"],
         ["A. nether land","B. jerman","C. italia","D. sweden"],
         ["A. bahrian","B. monaco","C. oman","D. kwait"]]


def new_game():
    guesses=[]
    question_num=0

    counter=0
    for key in questions:
        print("------------------------")
        counter+=1
        print(counter,".",key)
        for i in options[question_num]:
            print(i.capitalize())
        quess= input("Enter (A, B, C, or D): ")
        guess=quess.upper()
        guesses.append(quess.upper())

        question_num+=1


new_game()
