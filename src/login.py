from os.path import expanduser
try:
	home= expanduser("~")
	file=open(home + "/acct")

	try:
		username=file.readline().rstrip("\n")
		password=file.readline().rstrip("\n")
		print username+" "+password
	finally:
		file.close

except IOError:
	print ("file not found")


