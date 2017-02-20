import urllib.request
def read_text():
	"""open lets us read content of file on computer"""
	quotes = open("/Users/briceida/Udacity/Python/ProgrammingFoundations/profanity_checker/movie_quotes.txt")
	contents_of_file = quotes.read()
	# print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)
def check_profanity(text_to_check):
	"""urlopen helps open a connection to the internet"""
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check))
	#output is in bits
	output = connection.read()
	# print(output)
	# print(type(output))

	#converts byte to string
	byte2String=output.decode("utf-8") 
	# print(type(a))
	# print(a)
	connection.close()
	if "true" in byte2String:
		print("Profanity Alert!")
	elif "false" in byte2String:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly :( ")

read_text()