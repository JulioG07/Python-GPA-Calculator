def gpaCalc(average):

    #from classes import average 

    if average in range(90,100):
        print("Grade: A" )
        print("Unweighted GPA: 4.0 ")
    elif average in range(87,89):
        print("Grade: A-" )
        print("Unweighted GPA: 3.7 ")
    elif average in range(83,86):
        print("Grade: B+" )
        print("Unweighted GPA: 3.3 ")
    elif average in range(80,82):
        print("Grade: B" )
        print("Unweighted GPA: 3.0")   
    elif average in range(77,79):
        print("Grade: B-" )
        print("Unweighted GPA: 2.7")
    elif average in range(73,76):
        print("Grade: C+" )
        print("Unweighted GPA:2.3")
    elif average in range(70,72):
        print("Grade: C" )
        print("Unweighted GPA:2.0")

#gpaCalc()