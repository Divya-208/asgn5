#1 check yr. leap or not
x=int(input(enter the year))
if year%4==0:   
	print("year is not a lp year")
else
	print("year is not a leap yr.")
	
# 2 take length and breadth and check they are dim. of sq. or rect
x=int(input("enter the length"))
print(x)
y=int(input("enter the breadth"))
print(y)
if x==y:
    print("dim. are of square")
else:
    print("dim. are of rect")

# take ther input ager of 3 people and determnine the youngest and oldest in them
a = int(input("enter your age"))
b = int(input("enter your age"))
c = int(input("enter your age"))
if (a > b):
    if (a > c):
        print("a is older")
    else:
        print("c is older")
else:
    if (b > c):
        print("b is older")
    else:
        print("c is older")

    # 4.Write an if statement to lets competitor know which of these prizes they won.
a = int(input("Enter the points:"))
f = 1
if a < 200:
    if 1 < a < 50:
        f = 0
        print("No Prize")
    elif 50 < a < 150:
        prize = "jewellery"
    elif 150 < a < 180:
        prize = "clothes"
    elif 180 < a < 200:
        prize = "Chocolates"
    if f != 0:
        print("Congratulations! You won a {}".format("prize"))

# prog to print total cost for user
n = int(input("enter the cost:"))
p = n * 100
if p > 1000:
    disc = p * .1
    r = p - disc
    print('total cost= ', r)