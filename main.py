def main():

    #User Basic Information
    print("")
    print("*******************************************************")
    print("")
    print("Let's create your student porfolio!")
    print("")
    userName = input("Enter first name: ")
    userGrade = input("Enter your grade level: ")
    print("")
    print("*******************************************************")
    print("")

    #Welcome Message
    print(userName,",","Welcome to the GPA calculator[V1]! ")
    print("")
    print("*******************************************************")
    print("")

    #Goes from input classes => input class scores => calculate average => moves average to main.py 
    from classes import generate_Classes
    from classes import returnAverage
    generate_Classes() 

    print("Loading...")
    print("**************************************************************************************")
    
    # Grabs average and conditions it to its respective GPA
    from gpa import gpaCalc
    average = returnAverage()
    gpaCalc(average)

    #Ask user if they want to use the calculator again 
    userResponse = input( "\nTry again? [Y or N] ")
    
    if userResponse.lower == "Y":
        userResponse = True
    elif userResponse.lower == "n":
        print("Program ends")
    

    while userResponse == True:
        generate_Classes()
        average = returnAverage()
        gpaCalc(average)
    if userResponse == False:
        print("See you later ",userName,"!")

main()


