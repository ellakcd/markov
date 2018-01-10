"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    big_list_of_words = []
    for file1 in file_path:
        big_list_of_words.append(open(file1).read())
    # print big_list_of_words
    document = " ".join(big_list_of_words)

    # document = open(file_path).read()

    return document



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()
    chains = {}
    user_ngram = int(raw_input("How long would you like your n-gram to be?"))


    for word_index in range(0,len(words)-user_ngram):
        words_list = []
        counter = 0
        while counter < user_ngram:
            word = words[word_index + counter]
            words_list.append(word)
            counter += 1
        word_tuple = tuple(words_list)
        value = words[word_index + user_ngram]
    

        if (word_tuple) in chains:
            chains[(word_tuple)].append(value)
        else:
            chains[(word_tuple)] = [value]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # key = None
    # #for random_key in chains: #chains is our dictionary
    # # print chains.keys()
    # while True: 
    #     key = (choice(chains.keys()))
    #     if key[0].capitalize() == key[0]:
    #         for i in range(0, len(key)):
    #             words.append(key[i])
    #         break

    key = (choice(chains.keys()))
    for i in range(0, len(key)):
        words.append(key[i])
   

    
    while True:
        value_options = chains[key]
        next_word = choice(value_options)
        words.append(next_word)
        key = list(key)
        key = key[1:] + [next_word]
        key = tuple(key)
        if key not in chains.keys():
            break

    words[0] = words[0].capitalize()
    return " ".join(words)


input_path = argv[1:] #input all files except first one


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)


# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
