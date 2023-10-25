def gpaCalc(average):
    if 90 <= average <101:
        print("Grade: A" )
        print("Unweighted GPA: 4.0 ")
        print("*******************************************************")
    elif 87 <= average < 90:
        print("Grade: A-" )
        print("Unweighted GPA: 3.7 ")
        print("*******************************************************")
    elif 83 <= average < 87:
        print("Grade: B+" )
        print("Unweighted GPA: 3.3 ")
        print("*******************************************************")
    elif 80 <= average < 83:
        print("Grade: B" )
        print("Unweighted GPA: 3.0")  
        print("*******************************************************") 
    elif 77 <= average < 80:
        print("Grade: B-" )
        print("Unweighted GPA: 2.7")
        print("*******************************************************")
    elif 73 <= average < 77:
        print("Grade: C+" )
        print("Unweighted GPA: 2.3")
        print("*******************************************************")
    elif 70 <= average < 73:
        print("Grade: C" )
        print("Unweighted GPA: 2.0")
        print("*******************************************************")
    elif 67 <= average < 70:
        print("Grade: C-")
        print("Unweighted GPA: 1.7")
        print("*******************************************************")
    elif 63 <= average < 67:
        print("Grade: D+")
        print("Unweighted GPA: 1.3")
        print("*******************************************************")
    elif 60 <= average < 63:
        print("Grade: D ")
        print("Unweighted GPA: 1.0")
        print("*******************************************************")
    elif 50 <= average < 60:
        print("Grade: D-")
        print("Unweighted GPA: 0.7")
        print("*******************************************************")
    elif 0 <= average < 50:
        print("Grade: F ")
        print("Unweighted GPA: 0.0")
        print("*******************************************************")
    else:
        print("Your average is out of range, students can't a get grade that is greather than 100")
        print("**************************************************************************************")