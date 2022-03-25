from classes import Question, CQuestion, Quiz, add_players
from time import sleep

question_list = []

def quiz_option():
    # An option to either have or not have a category option in the quiz.
    print("Welcome Quiz host, we would like to ask a simple question before we start the quiz prep.")
    print("\nWould you like to have a category option in your quiz?")
    option = input("(Y/N): ")
    if option.lower() == "y":
        print("\nYou have selected the category option, thank you for your input. Good luck and have fun with your quiz.")
    
    elif option.lower() == "n":
        print("\nYou have selected the non category option, thank you for your input. Good luck and have fun with your quiz.")
    
    else:
        print("\nSorry something went wrong we shall not add categories option to your quiz. Good luck and have fun with your quiz.")
    
    return option

def quiz_setup():
    # Global variable for the questions and answers that way this function isn't needed to be called again.
    global question_list
    # Makes a variable to check if there should be a category option in the quiz.
    category_option = quiz_option()
    question_amount = int(input("\nHow many questions will your quiz have?\nAmount: "))   
    print("\nWhat would you like your question to be?")
    
    # Creates the questions and answers to the quiz and adds them to an array.
    for i in range(question_amount):
        qq = str(input(f"\nQuestion {i + 1}. : "))
        print(f'\nAnd what is the answer to "{qq}"?')
        answer = str(input("Answer: "))
        
        if category_option.lower() == "y":
            print(f'And what category would you like to put "{qq}?" in?')
            category = str(input("Category: "))
            question_list.append(CQuestion(qq, answer, category))
            
        else:
            question_list.append(Question(qq, answer))
    
    return question_list

def main():
    # Start up the quiz with a quick setup and welcomes the user to the quiz.
    quiz_setup()
    print("Welcome to the quiz.\nFirst things first is that we need to find out how many players are going to be playing\n")
    players = add_players()
    
    # Welcomes the player(s)
    for char in players:
        print(f"\nHello: {char} and good luck on the quiz")

    # Creating a empty array for correct answers
    ca_list = []
    # Loops through the players and has them answer the questions to the quiz.
    for player in players:
        pa_list = []
        ca = 0
        # Loops through the question list and compares the players input and the correct answer.
        for i in range(len(question_list)):
            print(f"\n{player}. What is your answer to:")
            print(question_list[i].get_question())
            pa = input("Your answer: ")
            pa_list.append(pa)
            if pa.lower() == question_list[i].get_answer().lower():
                ca += 1
        ca_list.append(ca)

    # Two variables that determine what happens in the correct answer loop.
    i = 0
    mc = 0
    # Loops through players again to check who had the most amount of correct answers.
    for player in players:
        pw = ""
        print(f"{player} got {ca_list[i]} amount of correct answers")
        if ca_list[i] > mc:
            mc = ca_list[i]
            pw = player
        i += 1

    # Prints who won the quiz.
    print("And the player that one is:")
    sleep(1)
    print(pw)

    # Adds the option to improve the code farther if you has multiple quizes you can check what qna's and players,
    # As well as who the winner was in certain quizes.
    Quiz(question_list, players, pw)

if __name__ == "__main__":
    main()
