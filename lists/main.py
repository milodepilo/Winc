# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def main():
    films = ['I Passed for White', 'Because They"re Young', 'The Secret Ways', 'Lost in Space' ]
    print(alphabetical_order(films))

    print(won_golden_globe('jaws'))
    print(remove_toto_albums(['Fahrenheit', 'The Seventh One','The John Towner Touch']))

def alphabetical_order(list):
    return sorted(list, key=str.lower)

def won_golden_globe(name_of_film):
    golden_globe_awards = ['jaws', 'star Wars: episode IV - a new hope', 'e.t the extra terrestrial', 'memoirs of a geisha']
    if name_of_film.lower() in golden_globe_awards:
        return True
    return False

def remove_toto_albums(list_of_albums):
    toto_albums = ['Fahrenheit', 'The Seventh One']
    clean_list = [x for x in list_of_albums if x not in toto_albums]         
    return clean_list


if __name__ == '__main__':
    main()
