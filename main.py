from classes import Question, CQuestion, Player, Quiz, add_players

def quiz_option():
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
    question_list = []
    category_option = quiz_option()
    question_amount = int(input("\nHow many questions will your quiz have?\nAmount: "))   
    print("\nWhat would you like your question to be?")
    
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
    pass



if __name__ == "__main__":
    main()
