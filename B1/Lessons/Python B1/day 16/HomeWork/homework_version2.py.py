def quiz(user_answer, user_question):
    while True:
        if user_answer == user_question:
            print("Be a Friend")
            break
        elif user_answer != user_question:
            print("Kich His Ass")
            break
        else:
            print("Rob Him")
            

user_question = "Good Human  "
user_answer = input("Which type of Person you Are ? ")

quiz(user_answer, user_question)


