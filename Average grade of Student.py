print("Enter the Grade Obtained in 7 Subjects: ")

Sub_1 = int(input("PFSD Grade="))
Sub_2 = int(input("AOOP Grade="))
Sub_3 = int(input("DBMS Grade="))
Sub_4 = int(input("SOCIAL INTERNSHIP Grade="))
Sub_5 = int(input("PSQT Grade="))
Sub_6 = int(input("ESE Grade="))
Sub_7 = int(input("CNS Grade="))

total=(Sub_1+Sub_2+Sub_3+Sub_4+Sub_5+Sub_6+Sub_7)
average=(total)/7
print("\n")
print("You got",average,"SGPA")
if average == 10:
    print("CONGRATULATIONS for your 10 SGPA")
elif average == 9 :
    print("Congratulations for your 9 SGPA")
elif average == 8:
    print("CONGARTS for your 8 GPA")
elif average == 7:
    print("cONGRATS for your 7 GPA")
else:
    print("Better luck Next Time")


