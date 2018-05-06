import change


a=input("please cheak 1 for manual modle and 2 for cmd modle")

if (a==1):
    a1 = change_scanner("processList", "2018-05-03 18:29:28", "2018-05-03 18:31:10")
    a1.chagne
elif (a==2):
    b=input("please enter file name: ")
    b1=input("please enter time at the format yyyy-mm-dd hh:mm:ss : ")
    b2=input("please enter time at the format yyyy-mm-dd hh:mm:ss : ")
    a1 = change_scanner(b, b1, b2)
    a1.chagne
else:
    print "please enter correct number"


