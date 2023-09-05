n = int(input("1=make picture|2=instainfo|3=logo |4=chatgbt|با توجه به نیازتون وارد کنید"))

if n == 1:
    exec(open('amirbot1.py').read())
elif n == 2:
    exec(open('amirbot2.py').read())
elif n == 3:
    exec(open('amirbot3.py').read())
elif n == 4:
    exec(open('amirbot4.py').read())
else:
    print("Invalid number entered.")
