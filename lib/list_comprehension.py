#!/usr/bin/env python3

def return_evens(num_list):
    print([num for num in num_list if num %2 ==0])

return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    print([sentence + "!" for sentence in sentence_list])
    
make_exclamation(["Hello", "How are you?"])