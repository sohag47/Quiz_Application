# this is the main app all function goes here:
def Quiz_App():

    # this is header design for  home page:
    header = '''
    ***** Welcome To Quiz Appplication BD *****
    please login
            1. User
            2. Admin
            3. Exit
    '''

    # this is Footer design for last page:
    footer = "Copyright SohagInc Allright Reserved 2020"
    print(header)

    # take user commend for what type of login:
    login_data = int(input("Enter Your Number:"))

    # check signin or signup:
    if(login_data == 1):
        user_manu = """
        1. SignIn
        2. SignUp
        3. Cancel
        """
        # create dictionary for the Question, answer store:
        user_info = {}
        print(user_manu)
        user_choice = int(input("Enter Your Choice:"))

        # user Signin form:
        if(user_choice == 1):

            # file read user registration file:
            data_store = open(
                "./Data/Registration_info/register_data.txt", "r")

            # user signin form:
            email = input("Enter Your Email:")
            password = input("Enter Your Password:")

            result = data_store.read()
            (key, value) = result.split()
            data_store.close()

            # user login validation:
            if(key == email and value == password):
                print("\nLogin Successfully!!!\n")
                print("'" + email + "' " + "Welcome to Quiz Application")

                # Question, Options, Check_Answer working in the main app():
                def Main_app():

                    # question, answer file read:
                    question_answer = open(
                        "./Data/Question_Ans/question_ans.txt", "r")
                    # for line by line reading:
                    data = question_answer.readlines()
                    temp = len(data)
                    i = 0

                    # Show All Question, Options:
                    while(i < temp-1):
                        print(data[i])
                        i = i+1
                    question_answer.close()

                    # get User data here:
                    user_answer = str(input("Enter your number:"))

                    # Check Answer it is currect or wrong:

                    def Check_Answer(user_answer, data):
                        if(user_answer in data[5]):
                            print(
                                "{} Awesome! The Answer is Currect.".format(data[5]))
                        else:
                            print("Wrong Answer!!!")

                    # Pass user_answer, Options in the Check_Answer():
                    Check_Answer(user_answer, data)

                Main_app()

                # Exit Quiz App:

                def Exit_QuizApp():
                    User_permission = input("Are you want to Log out? (y/n):")
                    if(User_permission == "n"):

                        # back to home page:
                        Result = Main_app()
                        Result = Exit_QuizApp()
                    elif(User_permission == "y"):
                        Quiz_App()

                Exit_QuizApp()
            else:
                print("\nLogin Unsuccessfull!!!")
                print("Please try again later...")

                Quiz_App()

        # user registration form:
        elif(user_choice == 2):
            print("Create Your Account")

            # file create for the user info store:
            data_store = open(
                "./Data/Registration_info/register_data.txt", "w")
            email = input("Enter Your Email:")
            password = input("Enter Your Password:")
            space = " "
            data_store.write(str(email))
            data_store.write(str(space))
            data_store.write(str(password))
            data_store.close()
            print("\nYour Registration Successfully!!!")
            print("'" + email + "' " + "Welcome to Quiz Application\n")

            # Question, Options, Check_Answer working in the main app():
            def Main_app():

                # question, answer file read:
                question_answer = open(
                    "./Data/Question_Ans/question_ans.txt", "r")
                # for line by line reading:
                data = question_answer.readlines()
                temp = len(data)
                i = 0
                # Show All question, answer:
                while(i < temp-1):
                    print(data[i])
                    i = i+1
                question_answer.close()
                # get User data here for Answer:
                user_answer = str(input("Enter your number:"))

                # Check Answer it is currect or wrong:

                def Check_Answer(user_answer, data):
                    if(user_answer in data[5]):
                        print(
                            "{} Awesome! The Answer is Currect.".format(data[5]))
                    else:
                        print("Wrong Answer!!!")
                # Pass user_answer, Options in the Check_Answer():
                Check_Answer(user_answer, data)

            Main_app()

            # Exit Quiz App:

            def Exit_QuizApp():
                User_permission = input("Are you want to Log out? (y/n):")
                if(User_permission == "n"):
                    # Back to Home Page:
                    Result = Main_app()
                    Result = Exit_QuizApp()
                elif(User_permission == "y"):
                    Quiz_App()

            Exit_QuizApp()

        # user sign/signup cancel option:
        elif(user_choice == 3):
            Quiz_App()

    # Admin page:
    elif(login_data == 2):
        header_admin = '''
        ***** Welcome To Admin *****
                1. SignIn
                2. SignUp
                3. Cancel
        '''
        print(header_admin)
        admin_choice = int(input("Enter Your Choice:"))
        if(admin_choice == 1):
            # file read admin registration file:
            data_store = open(
                "./Data/Registration_info/register_data_admin.txt", "r")

            # admin signin form:
            email = input("Enter Your Email:")
            password = input("Enter Your Password:")

            result = data_store.read()
            (key, value) = result.split()
            data_store.close()

            # admin login validation:
            if(key == email and value == password):
                print("\nLogin Successfully!!!\n")
                print("'" + email + "' " + "Welcome to Quiz Application")

                # admin control panel:

                def control_panel():
                    control_monitor = """
                    ****** Control Panel ******
                    1. Add Question & Answer
                    2. Delete Question & Answer
                    3. Modify Question & Answer
                    4. Cancel
                    """
                    print(control_monitor)
                    # Admin choose option:
                    admin_control_choice = int(input("Enter Your Choice:"))
                    if(admin_control_choice == 1):
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
                            # Exit Quiz App:

                            def Exit_QuizApp():
                                User_permission = input(
                                    "Are you want to Log out? (y/n):")
                                if(User_permission == "n"):
                                    # Back to Home Page:
                                    Result = Add_Question_Answer()
                                    Result = Exit_QuizApp()
                                elif(User_permission == "y"):
                                    control_panel()

                            Exit_QuizApp()

                        Add_Question_Answer()

                        def Exit_QuizApp():
                            User_permission = input(
                                "Are you want to Log out? (y/n):")
                            if(User_permission == "n"):
                                # Back to Home Page:
                                Result = control_panel()
                                Result = Exit_QuizApp()
                            elif(User_permission == "y"):
                                Quiz_App()

                            Exit_QuizApp()
                    if(admin_control_choice == 4):
                        Quiz_App()
                control_panel()

        # Admin SignUp form:
        elif(admin_choice == 2):
            print("Create Your Account")

            # file create for the user info store:
            data_store = open(
                "./Data/Registration_info/register_data_admin.txt", "w")
            email = input("Enter Your Email:")
            password = input("Enter Your Password:")
            space = " "
            data_store.write(str(email))
            data_store.write(str(space))
            data_store.write(str(password))
            data_store.close()
            print("\nAdmin Registration Successfully!!!")
            print("'" + email + "' " + "Welcome to Quiz Application\n")

            # Question, Options, Check_Answer working in the main app():
            def Main_app():

                Main_app()

                # Exit Quiz App:

                def Exit_QuizApp():
                    User_permission = input("Are you want to Log out? (y/n):")
                    if(User_permission == "n"):
                        # Back to Home Page:
                        Result = Main_app()
                        Result = Exit_QuizApp()
                    elif(User_permission == "y"):
                        Quiz_App()

                Exit_QuizApp()

        elif(admin_choice == 3):
            Quiz_App()

    # Software close:
    elif(login_data == 3):
        print("Thank You!")
        print(footer)
        pass


Quiz_App()
