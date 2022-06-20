__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import zipfile


cache_path = os.path.join(os.getcwd(), 'files\cache')
zip_path = os.path.join(os.getcwd(), 'files\data.zip')


def main():
    clean_cache()
    cache_zip(zip_path, cache_path)
    print(find_password(cached_files()))    


def clean_cache():
    try:
        os.mkdir(cache_path)
    except FileExistsError:            
        for f in os.listdir(cache_path):
            os.remove(os.path.join(cache_path, f))


def cache_zip(zip_path, cache_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_path)


def cached_files():
    list_of_cached_files = []
    for f in os.listdir(cache_path):
        list_of_cached_files.append(os.path.join(cache_path, f))        
    return list_of_cached_files


def find_password(list_of_files):
    for file_path in list_of_files:           
        with open(file_path) as f:            
            read_lines = f.readlines()
            for line in read_lines:
                if 'password' in line.lower():                    
                    return line[line.find(':') + 2:].strip()                           


if __name__ == '__main__':
    main()
    