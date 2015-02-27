"""Library to read file to get login/pw for Google acct.  File is expected in this format:
username
password
"""

from collections import namedtuple
from os.path import expanduser
# from sys import argv
import sys

Glogin= namedtuple("GoogleLogin","GUserName GPassword")


def readGoogleLogin(gfilename=""):

	try:
		if not gfilename:
			home = expanduser("~")+"/acct"
			gfile=open(home,"r")
		else:
			gfile=open(gfilename,"r")
		
	
		try:
			username=gfile.readline().rstrip("\n")
			password=gfile.readline().rstrip("\n")
			print username+" "+password
			return Glogin(username,password)
		finally:
			file.close
	
	except IOError:
		print ("file not found")

if __name__ == '__main__':
	if len(sys.argv)>1 :
		readGoogleLogin(sys.argv[1])
	else:
		pass