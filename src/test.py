'''
Created on Jan 12, 2015

@author: snoecker
'''

if __name__ == '__main__':
    pass
from gmusicapi import Mobileclient, Api
import login

api = Mobileclient()
GAcct=login.readGoogleLogin()

if GAcct:
    logged_in = api.login(GAcct.GUserName, GAcct.GPassword)
#     logged_in is True if login was successful

    if logged_in == True:
        print "logged in"
    
    song_list= api.get_all_songs(True)
    for songs in song_list:
        print "size of list" + str(len(songs))
    logged_out= api.logout()
    print "logged out " + str(logged_out)
    
    