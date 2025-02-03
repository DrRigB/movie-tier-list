import requests
from bs4 import BeautifulSoup
import random
import time

def scrape_dictionary(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        words = []
        for word in soup.find_all('a', class_='entry-link'):  # Adjust the selector based on the actual HTML structure
            words.append(word.text.strip())
        return words
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

def generate_random_word(length, dictionary):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    word = []
    has_vowel = False

    # Generate a word based on a simple syllable structure
    while len(word) < length:
        if len(word) > 0 and word[-1] == 'q':  # If the last letter is 'q', the next must be 'u'
            word.append('u')
        else:
            if random.choice([True, False]) and not has_vowel:  # Ensure at least one vowel
                letter = random.choice(vowels)
                has_vowel = True
            else:
                letter = random.choice(consonants)

        word.append(letter)

        # Ensure a simple structure: CV or CVC
        if len(word) > 1 and word[-2] in consonants and letter in consonants:
            # If the last two letters are both consonants, replace the last one with a vowel
            word[-1] = random.choice(vowels)

    # If no vowel was added, replace a random consonant with a vowel
    if not has_vowel:
        index = random.randint(0, length - 1)
        word[index] = random.choice(vowels)

    generated_word = ''.join(word)

    # Check if the generated word is in the dictionary
    if generated_word in dictionary:
        return generated_word
    else:
        return None  # Return None if the word is not valid

# URL for words starting with 'A'
url = 'https://dictionary.cambridge.org/us/browse/english/a/'
dictionary = scrape_dictionary(url)

while True:
    if 1 == 1:
        word_length = random.randint(3, 8)  # Random word length between 3 and 8
        random_word = generate_random_word(word_length, dictionary)  # Generate a random word
        if random_word:
            print(random_word)  # Print the generated word if valid
        else:
            print("Generated word is not valid.")  # Indicate if the word is not valid
        time.sleep(0.01)  # Wait for 0.01 seconds after printing
    else: 
        break