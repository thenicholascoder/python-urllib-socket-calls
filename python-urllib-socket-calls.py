#import urllib library which makes socket calls a lot simpler
import urllib.request, urllib.parse, urllib.error

#set up file handler for the data
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#using indefinite loop
for line in fhand:

	#inorder to manipulate we should decode the data from file handler first
	print(line.decode().strip())