from difflib import SequenceMatcher

def run():
	def print_message():
		print("******************************")
		print("Find The Most Similar Norwegian Neme To Yours In 100 Most Popular Norwegian Names!")
		print("******************************")

	def search_names(sex, name):
		"""
		Search in the names and find most similar norwegian names.
		"""
		# Try to open the text file and read lines.
		try:
			f = open(f"{sex}.txt", 'r')
			f.readline()
			found = False # Usage: if doesn't found similar name print a message.

			# Loop through each line of file and find the most similar names
			for line in f:
				sequence = SequenceMatcher(None, name.lower(), line.lower())
				if sequence.ratio() > 0.5:
					print(line)
					found = True
			# If doesn't found any similar name print a message.
			if not found:
				print(f"Sorry, We dont find a good match to {name}")
			f.close()
		# If file name was incorrect
		except:
			print("Wrong sex input!!!")
			run()
		
	print_message()
	sex = input("What is your sex? [Male/Female]: ") # Get the user sex
	name = input("What is your name? ")# Get the user name
	search_names(sex.lower(), name)

run()