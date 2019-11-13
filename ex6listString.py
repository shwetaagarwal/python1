s1 = input("Enter a string :")
def is_palindrome(s1):
	s1_len = len(s1)
	s1_half_len = int( s1_len/2 )
	all_match = True
	for i in range(s1_half_len):
		if( s1[i] != s1[s1_len-i-1]):
			all_match = False
			break
		else:
			continue
	return all_match
	
def is_palindrome2(s1):
	all_match = False
	if s1 == s1[::-1]:
		all_match = True
	return all_match

if is_palindrome2(s1):
	print(s1," is a palindrome.")
else:
	print(s1, "is not a palindrome.")



