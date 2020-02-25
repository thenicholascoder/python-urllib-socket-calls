#import urllib library which makes socket calls a lot simpler
import urllib.request, urllib.parse, urllib.error

#set up file handler for the data
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#create an empty dictionary
counts = dict()

#using indefinite loop to itterate the lines
for line in fhand:

	#inorder to manipulate we should decode the data from file handler first
	words = line.decode().strip()

	#another indefinite loop to itterate the words per line
	for word in words:

		#inside the counts dictionary i will store a key of word and will add 1 as value to that key
		counts[word] = count.get(word, 0) + 1