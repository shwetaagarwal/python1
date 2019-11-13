''' module to find size
'''
SUFFIXES = {1000: ['KB','MB','GB','TB','PB', 'EB', 'ZB', 'YB'],
			1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
			
def approximate_size(size, a_kilobyte_is_1024_bytes=True):
	'''Convert a file size to human readable format
	returns string '''
	if size < 0:
		raise ValueError('number must not be negative')
		
	multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
	for suffix in SUFFIXES[multiple]:
		size /= multiple
		if size < multiple:
			return '{0:.1f}{1}'.format(size, suffix)
	#else:#not required note:indentation
	#	raise ValueError('size too large')
	raise ValueError('size too large')
	
if __name__ == '__main__':
	print(approximate_size(100000000000000000000000000,False))
	print(approximate_size(100000000000000000000000000))
	print(approximate_size(1000000000000000000000000000,False))
	print(approximate_size(1000000000000000000000000000))