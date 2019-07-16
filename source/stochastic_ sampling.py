from histogram_lists import array
import random

def probability(histogram):
    total_freq = 0
    cumulative_probability = 0.0

    # Adds up all word frequency from the histogram
    for element in histogram:
        total_freq += element[1]

    # picks a random word weighted through frequency
    random_num = random.uniform(0, 1)
    for element in histogram:
        cumulative_probability += element[1]/total_freq
        if cumulative_probability >= random_num:
            return element[0]

def check_accuracy(histogram):
    proof_dict = dict()

    # fills a dictionary with a word as a key and sets probability to 0 
    for element in histogram:
        proof_dict[element[0]] = 0
    # stores each individual sample of 1000 function calls
    for _ in range(0, 10000):
        proof_dict[probability(histogram)] += 1

    return(proof_dict)

# print(array)
# print(probability(array))
print(check_accuracy(array))
