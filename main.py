def main():

    #User Basic Information
    userName = input("Enter first name: ")
    userGrade = input("Enter your grade level: ")
    print("")

    #Welcome Message
    print(userName,", ","Welcome to the GPA calculator[V1]! ")
    print("")

    from classes import generate_Classes
    generate_Classes() #Generates classes 

    print("Loading...")
    print("")

    from gpa import gpaCalc
    from classes import average 

    gpaCalc(average)

main()


