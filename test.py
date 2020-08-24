# Question, Options, Check_Answer working in the main app():
def Add_Question_Answer():

    # question, answer file read:
    add_question_answer = open(
        "./Data/Question_Ans/question_ans.txt", "w")
    add_question = input("Enter Your Question:")
    add_option1 = input("Enter Your 1st Option:")
    add_option2 = input("Enter Your 2nd Option:")
    add_option3 = input("Enter Your 3rd Option:")
    add_option4 = input("Enter Your 4th Option:")
    add_option5 = input("Enter Your Currect Answer:")

    add_question_answer.write(str(add_question))
    add_question_answer.write('\n')
    add_question_answer.write(str(add_option1))
    add_question_answer.write('\n')
    add_question_answer.write(str(add_option2))
    add_question_answer.write('\n')
    add_question_answer.write(str(add_option3))
    add_question_answer.write('\n')
    add_question_answer.write(str(add_option4))
    add_question_answer.write('\n')
    add_question_answer.write(str(add_option5))

    add_question_answer.close()
    print("\nCreate Question Successfully!!!")


Add_Question_Answer()
