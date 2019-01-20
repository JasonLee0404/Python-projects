#data.json contains data of a real dictionary
#what we do in this script is we load in the data from data.json file, and then 
#we read the input from the user, and then if the input is in the dictionary, we 
#return the definition in it, otherwise we inform the user



import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word_arg):

	word_arg = word_arg.lower();

	#trace the dictionary using the key 'word_arg'

	#if the word is inside the dictionary we have
	if word_arg in data:
		return data[word_arg]
	elif len(get_close_matches(word_arg,data.keys())) > 0:


		#we call get close matches and get the first element out of it to replace in the returning message
		ans = input("Did you mean %s instead ?" % get_close_matches(word_arg,data.keys())[0])

		if ans == "y":
			return data[get_close_matches(word_arg,data.keys())[0]]
		elif ans == "n":
			return "the word does not exist in our dictionary"
		else:
			return "we didn't understand your answer"

	else:
		return "The word does not exist. Please double check it"



#get input from the user
word = input("Enter word: ")





print(translate(word))