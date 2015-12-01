from sense_hat import SenseHat
import re
import time
from collections import defaultdict
from sys import argv

pixel_on=(0,255,0)
pixel_off=(0,0,0)



def pad(line):
	global pixel_off
	padding=[pixel_off,]*(8-len(line))
	return line + padding

def read_character_file(charfile='small.txt'):
	on_char='o'
	off_char='-'
	global pixel_on, pixel_off

	char_def=defaultdict(list)
	char_code=None
	for linenum, line in enumerate( open(charfile, "rb"), start=1 ):
		if re.match("^#", line):
			char_code=line[1]
			print 'Found Start of Definition for character :%s'%char_code
			next
		else:
			if char_code==None or len(char_code)!=1:
				raise ValueError( "Error reading definition file %s, Line %d. No character defined ? (use '#<char>' on line above)"%(charfile, linenum) )
			char_def[char_code].append(  map(lambda x: pixel_on if x==on_char else pixel_off , line.strip() ) )


	for char_code in sorted( char_def.keys() ):
		for linenum, line in enumerate( char_def[ char_code ] ): # pad each line to max width
			char_def[ char_code ][ linenum ]=pad( line )
		char_height=len(char_def[char_code])
		for linenum in range(8-char_height):	# pad empty lines to max height
			char_def[ char_code ].append( pad([]) )
		
		temp_list=[]
		for line in char_def[ char_code ]:	# merge everything into a single list
			temp_list=temp_list + line
		char_def[char_code]=temp_list

	sense=SenseHat()
	sense.set_rotation(180)
	while True:
		for char_code in sorted( char_def.keys() ):
			sense.set_pixels( char_def[char_code] )
			time.sleep(0.5)
"""
while True:
	time.sleep(1)
	sense.set_pixels( test2 )
	time.sleep(1)
"""

if __name__=='__main__':
	if len(argv)==1:
		read_character_file('smallhex.txt')
	else:
		read_character_file(argv[1])


