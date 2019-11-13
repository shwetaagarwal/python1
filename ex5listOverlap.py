import random
#list1 = [1,2,3,4,5,10,10]
#list2 = [2,5,7,8,9,10,10]

list1 = random.sample(range(10),7)
list2 = random.sample(range(10),9)

list_common =[]
for ele in list1:
	if ele in list2 :
		if ele not in list_common:
			list_common.append(ele)
print(list1)
print(list2)
print(list_common)