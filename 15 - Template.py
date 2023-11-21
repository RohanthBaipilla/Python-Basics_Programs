a="Dear <|NAME|>,\n\t You are selected \n\t\t<|DATE|>"
name=(input("Enter the name\n"))
date=input("Enter the date\n")
a=a.replace("<|NAME|>",name)
a=a.replace("<|DATE|>",date)
print(a)
