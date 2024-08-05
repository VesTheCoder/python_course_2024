apple = 40
banana = 50
tea = 10
money = float(input("How much money do u have?"))
if money >= apple + banana + tea:
    print("Buy everything dude!")
elif money >= apple + banana:
    print("Buy the fruits, fuck the tea!")
elif money >= banana + tea:
    print("Buy the banana, or an apple and the tea!")
elif money >= apple + tea:
    print("Buy the apple and tea, or the banana without the tea!")
elif money >= tea:
    print("Buy the tea!")
else:
    print("Sorry, you're too poor today, try next time.")
