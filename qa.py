import sys
import random

if len(sys.argv) < 2:
	print("suppy QA file")
	exit(1)

qafname = sys.argv[1]
rfh = open(qafname, "r")

qa_dict = {}

for line in rfh:
	entry = line.strip().split(",")
	qa_dict[entry[0]] = entry[1]

rfh.close()

while True:
	#index = random.randint(0,len(qa_dict))
	#rand_contr = qa_dict[index].key
	
	#error dict_keys does not support indexing 
	#rand_contr = random.choice(qa_dict.keys())
	rand_contr = random.choice( list ( qa_dict.keys() ) )
	in_cap = input("enter capital of " + rand_contr)
	if in_cap == qa_dict[rand_contr]:
		print("correct !")
	else:
		print("incorrect, "+ qa_dict[rand_contr])
	ch_input = input("to quit press q: ")
	if ch_input == 'q':
		break


