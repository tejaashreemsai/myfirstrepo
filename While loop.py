numberoftimes  = 1
totalmarks = 0
while numberoftimes < 6:
    marks = int(input("Enter your subject mark"))
    totalmarks = totalmarks + marks
    print("Mark of subject", numberoftimes,":",marks)
    print("Totalmarks at the end of iteration",numberoftimes,":",totalmarks)
    numberoftimes = numberoftimes+1
