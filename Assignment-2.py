import pandas as pd
def count_vowels(string):
    if not isinstance(string, str):
        return 0
    temp = 0
    vowels = 'aeiouAEIOU'
    for i in string:
        if i in vowels:
            temp += 1
    return temp


imdb_data = pd.read_csv('titles.csv')
imdb_data['vowel_count'] = imdb_data['title'].apply(count_vowels)

print(imdb_data.head(40))
