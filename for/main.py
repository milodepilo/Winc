from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
def shortest_names(list_of_countries):
    min_len = 10
    list_of_shortest_names = []
    for country in list_of_countries:
        if len(country) < min_len:
            min_len = len(country)
            list_of_shortest_names.append(country)
        else:
            continue
    return list_of_shortest_names

def most_vowels(list_of_countries):
    max_vowel_names = []
    max_vowel = 0
    #for country in list_of_countries:

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
