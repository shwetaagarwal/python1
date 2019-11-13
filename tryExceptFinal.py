import sys
numgo = 0
while True:
	numgo = numgo + 1
	try:
		num = int(input("Enter a number: "))
		print(20/num)
		break
	except ZeroDivisionError as detail:
		print("Exception Occured: ",detail)
	except IOError as e:
		print("error({0}): {1}".format(e.errno, e.strerror))
	except:
		#import sys
		print("Unexpected error:", sys.exc_info()[0])
		#raise can be used to exit the program
		raise
		
	finally:
		print(numgo," tries")