import datetime
username = input('Enter your name: ')
userage = input('Enter your age: ')
yearToAdd = 100 - int(userage)
thisyear = datetime.date.today().year
print("you will be hundred in ",thisyear+yearToAdd)
