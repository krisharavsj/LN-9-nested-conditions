attendance = int(input("please enter your attendance"))
if attendance>=75:
        print("student is allowed")
if attendance<75:
    medical=(input("please enter if you have any medical cause"))
    if medical ==True:
         print ("the student is allowed")
    else:
        print("the student is not allowed")