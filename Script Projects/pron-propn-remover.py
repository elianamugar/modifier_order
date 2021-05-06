import os
import nltk
from nltk.corpus import *
import nltk, re, pprint
from nltk import word_tokenize

# function to strip proper and pronouns
def main():

    # prints all text files available for stripping
    path = "/Users/EMWork/Desktop/Boston University/EVL/Script Projects/Strip PNs/Thorndykestripped/Anstey"
    for text_file in os.listdir(path):
        if '.txt' in text_file:
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            my_file = os.path.join(THIS_FOLDER, text_file)
            f = open(my_file, 'r+')
            raw = f.read()

        # stores user's text choice
        #chosen_text = input("Enter text file name with .txt EXACTLY as listed: ")
        #with open(chosen_text, 'r') as f:
            #raw = f.read()

        # tags all words with corresponding part-of-speech in user's text file choice
            tokens = nltk.word_tokenize(raw)
            tagged_corpus = nltk.pos_tag(tokens)
            update_corpus = ""
            punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''

            # strips proper and pronouns
            for i in range(len(tagged_corpus)):
                if ('NNP' not in tagged_corpus[i]) and ('PRP' not in tagged_corpus[i]) and ('PRP$' not in tagged_corpus[i]) and ('NNPS' not in tagged_corpus[i]):
                    if tagged_corpus[i][0] in punctuations:
                        update_corpus += tagged_corpus[i][0]
                    else:
                        update_corpus += " " + tagged_corpus[i][0]

            # stores user's filename choice
            #user_f = text_file

            # writes line count and data to text file of user's filename choice
            f.write(update_corpus)
            #f.close()

# user input to run, re-run, or stop the program
while True:
    answer = input("Run the 'Pronoun and Proper Noun Remover' program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break