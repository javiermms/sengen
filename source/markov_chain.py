"""
Psuedo-Code c('.'c)

Mission/Task at Hand: Take a corpus and create a markov chain using a dictionary or list of tuples.

Things your keeping track of:

- current word
- previous_word
- if the word has already been seen 

"""
import random
import list_of_tuples 
from stochastic_sampling import probability
import string
from clean_text import words_array

def create_markov(array):
    markov_chain = {}
    arr_length = len(array) - 1
    counter = 0
    
    while counter < arr_length:

        previous_word =  array[counter]

        if counter + 1 <= arr_length:
            current_word = array[counter + 1]

        if previous_word not in markov_chain:
            markov_chain[previous_word] = Dictogram([current_word])  
        else:
            markov_chain[previous_word].add_count(current_word)
        
        counter += 1

    return markov_chain

def random_start(array):
    random_word = random.choice(list(array.keys()))
    return random_word

def generate_sentence(markov_chain):
    length = 15
    first_word = random_start(markov_chain)
    sentence = first_word.capitalize()

    for word in range(random.randint(1, length)):
        second_word = probability(markov_chain[first_word])
        first_word = second_word
        sentence += ' ' + second_word
    
    return sentence

    

# print(random_start(words_array))
print(generate_sentence(create_markov(words_array)))
# random_start(markov)

