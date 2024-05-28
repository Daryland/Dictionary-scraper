import requests
from bs4 import BeautifulSoup 
import re
import json


# Create empty dictionary that will be of the format {word: length of word}, pulled from URL
word_dict = {}

# Gather content from URL
url = 'https://www.mit.edu/~ecprice/wordlist.10000'
#url = "https://lotr.fandom.com/wiki/Elvish_word_list" 
response = requests.get(url) # Get response from URL

if response.status_code == 200: # Checking that URL is accessible
        soup = BeautifulSoup(response.content, 'html.parser') # Parse HTML content
        text = soup.get_text() # Extract text
        words = re.findall(r'\b\w+\b', text.lower()) # Split text into words

        # Create word dictionary
        for word in words: # Loop through words and add them to word_dict
            word_length = len(word) # Get length of word
            if 4 <= word_length <= 7:  # Filter out words with length greater than 7 or less than 2
            	word_dict[word] = word_length # Add word to word_dict

else: 
	print(f"Failed to fetch webpage: {url}. Status code: {response.status_code}") # Print error message if URL is not accessible

# Create a new {} using the keys from word_dict and converting them into numeric code
mapping = {								# Create mapping dictionary
        'a': '2', 'b': '2', 'c': '2',
        'd': '3', 'e': '3', 'f': '3',
        'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5',
        'm': '6', 'n': '6', 'o': '6',
        'p': '7', 'q': '7', 'r': '7', 's': '7',
        't': '8', 'u': '8', 'v': '8',
        'w': '9', 'x': '9', 'y': '9', 'z': '9'
    }

numeric_code_dict = {}		   # Create numeric code dictionary

for word in word_dict.keys(): # Pull words from word_dictionary
	numeric_code = ''.join(mapping[char] for char in word.lower()) # Convert word to numeric code
	numeric_code_dict[word] = numeric_code # Add word and numeric code to numeric_code_dict
	# print(numeric_code_dict)

# # Search numeric_code_dict for matches to a user input phone number
# input_number = input("Enter a 7-digit number: ") 

# if len(input_number) != 7 or not input_number.isdigit(): # Verify validity of input
#     raise ValueError("Invalid input. Please enter a 7-digit number.")

# else:
# 	print(f"phone number entered: {input_number}")

# Instead of inputting a 7-digit number, iterate over all possible numeric codes of length 4-7
matching_words = {}	# Create dictionary to contain all matches found

for word, numeric_code in numeric_code_dict.items(): # Loop through numeric_code_dict
	if 4 <= len(numeric_code) <= 7: # Ensure numeric code is 4-7 characters long
		# print(numeric_code)
		matching_words[word] = numeric_code # Add word and numeric code to matching_words
  
# Print the matching words and their numberic codes
# for word, numeric_code in matching_words.items():
# 	print(f"Word: {word}, Numeric Code: {numeric_code}")

# for i in range(len(input_number)): # Parse input number into smaller sections
#     for j in range(i + 1, len(input_number) + 1): # Loop through all possible sections
#         section = input_number[i:j] # Get section of input number
#         if 5 <= len(section) <= 7: # Filter out sections with length greater than 7 or less than 2
#            # print(section)
#             for word, numeric_code in numeric_code_dict.items(): # Search numeric_code_dict for matching section
#                 if section == numeric_code: # Change this line of code to allow flexibility in capturing more results
#                     print(section, numeric_code, word)

# Save the scraped data to a JSON file
with open('dictionary.json', 'w') as f:
    json.dump(word_dict, f)