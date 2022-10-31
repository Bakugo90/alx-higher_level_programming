#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorti = sorted(a_dictionary.items())

    for k, v in sorti:
        print(k, v)


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)