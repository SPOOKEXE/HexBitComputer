
def split_into_chunks( value : str | list, size : int = 1 ) -> str | list:
	for i in range(0, len(value), size): yield value[i:i+size]

def convert_to_hex( binary : str ) -> str:
	return hex( int(binary, 2) ).upper()[2:]

def convert_line_to_hex( line : str, sep : str = ' ' ) -> str:
	return sep.join([
		''.join([
			convert_to_hex( binary )
			for binary in split_into_chunks(seg, size=4)
		])
		for seg in line.split(sep)
	])

for line in """01110000 000000100000 0000000000000001
01110000 000000100001 0000000000000010
00011000 000000100000 000000000001
00011000 000000100001 000000000010
10000000 000000000000 000000000000
00100000 000000000100 000000100010
01100000 000000100010 000000000000""".split('\n'):
	print(convert_line_to_hex(line))
