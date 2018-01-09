"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    document = open(file_path).read()

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
    # word3 = []


    for word_index in range(0,len(words)-2):
        word1 = words[word_index]
        word2 = words[word_index + 1]
        word3 = words[word_index + 2]

        if (word1, word2) in chains:
            chains[(word1, word2)].append(word3)
        else:
            chains[(word1, word2)] = [word3]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    #for random_key in chains: #chains is our dictionary
    # print chains.keys()
    key = choice(chains.keys())
    words.append(key[0])
    words.append(key[1])
    
    while True:
        value_options = chains[key]
        next_word = choice(value_options)
        words.append(next_word)
        key = (key[1], next_word)
        if key not in chains.keys():
            break


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
