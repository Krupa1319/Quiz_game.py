#Designing the quiz with atleast three questions
#Each question contains Multiple Options
quiz_questions = {
    "\n1.What is the extension for python?": {
        "A": ".pi",
        "B": ".py",
        "C": ".python",
        "D": "None of these",
        "Correct": "B"
    },
    
    
    "\n2.When did python released?": {
        "A": "1991",
        "B": "1994",
        "C": "1995",
        "D": "2008",
        "Correct": "A"
    },
    
    
    "\n3.python programming language was created by whom?": {
        "A": "Triavis Oliphant",
        "B": "McKinney",
        "C": "Guido Van Rossum",
        "D": "Cleve Molar",
        "Correct": "C"
    }
}
#Organization of code into functions or Classes,
#and implementation of Scoring mechanismto track the user's correct answer
def quiz_game():
    score = 0
    for question, options in quiz_questions.items():
        print(question)
#Feedback on each question,indicating whether the User's answer was correct or incorrect.
        for option, value in options.items():
            if option != "Correct":
                print(f"{option}: {value}")
        answer = input("Choose your answer (A, B, C, D): ")
        if answer.upper() == options["Correct"]:
            print("Correct answer!")
#Display the correct answer if the User is Wrong.
        else:
            print(f"Incorrect answer. The correct answer is {options['Correct']}.")

# To Display of user's Final Score
    print(f"\nQuiz finished! Your final score is {score}/{len(quiz_questions)}")

def main():
    print("Welcome to the Quiz Game!")
    quiz_game()
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
