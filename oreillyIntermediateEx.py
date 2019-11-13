''' module to find size
'''
import random
print ("a rand int :")
print(random.randint(1,6))

#reading and writing files

countries = []
# 
rfh = open("countries.txt","r")
for line in rfh:
	line = line.strip()
	print(line)
	countries.append(line)

print(len(countries))
rfh.close()

wfh = open("scores.txt","w")

while True:
	participant = input("participant name >")
	
	if participant == "quit":
		print("quitting...")
		break
		
	score = input("Score for "+ participant + ">")
	
	wfh.write(participant + "," + score + "\n")
	
	
wfh.close()

rfh = open("scores.txt","r")

participants = {}

for line in rfh:
	entry = line.strip().split(",")
	participants[entry[0]] = entry[1]

rfh.close()
print(participants)

