import time
s = "giangduong"
p = input("Enter your password: ")

while(s != p):
    print("Your password is wrong. Please try again. ^ ^")
    p = input("Enter your password again: ")

if(s == p):
    for i in range(0,11):
        print("===============================>", 10*i ,"%")
        time.sleep(0.5)
    f = open("ascii-art.txt", "r")
    for j in f:
        print(j, end="")
        time.sleep(0.2)
