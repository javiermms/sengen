from clean_text import words_array

class Tuplegram(list):
    """Tuplegram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Tuplegram, self).__init__()  # Initialize this as a new list
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
    
        if word in self[0]:
            self[1] += count
            self.tokens += count
        else:
            self.append(word, count)
            self.tokens += count
            self.types += 1

if __name__ == '__main__':
    objects = Tuplegram(words_array)
    print(objects)


# '''
# Tuples Implementation of Histogram
# '''
def tuplegram(text):
    words_list = [] #creates empty list object
    #accesses word in array
    for word in text: 
        #set found to false
        found = False
        #looping through list object 
        for index in words_list:
            #if the word is in the list already
            if index[0] == word:
                #increase frequency
                freq = index[1] + 1
                #remove index since tuples are immutable
                words_list.remove(index)
                #append word again with new freq
                words_list.append((word, freq))
                #set found to True
                found = True
        if not found:
            #if word isnt there, add the word and word freq
            words_list.append((word, 1))
    
    return words_list

