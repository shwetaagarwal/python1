import random
l1 = random.sample( range(20),10 )
l2 = [ele for ele in l1 if ele % 2 == 0]
print(l1)
print(l2)
