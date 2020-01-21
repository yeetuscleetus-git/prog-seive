#Finds HTML tags. This works only on Python 3.x.

#Exception for when tag(s) are not found
class NotFoundError(Exception):pass
class HTMLSeive:
	def __init__(self, file_name):
		self.file_name = file_name
		
	#Finds all tags on line
	def find(tag,line): 
		file_content = open(HTMLSeive.file_name,"r").read()
		file_content = file_content.split("\n")
		l = file_content[line-1]
		if tag not in l:
			raise NotFoundError("Tag {tag} not found on line {str(line)} of {HTMLSeive.file_name}")
		else:
			return l
	
	#Finds all tags in file
	def findAll(tag):		
		file_content = open(HTMLSeive.file_name,"r").read()
		file_content = file_content.split("\n")
		listOfFoundTags = []
		for line in file_content:
			if tag in line:
				listOfFoundTags.append(line)
			else:continue
		if len(ListofFoundTags) =< 0:
			raise NotFoundError("Tag {tag} not found in {HTMLSeive.file_name")
		else:
			for x in listOfFoundTags:
				print(x)
