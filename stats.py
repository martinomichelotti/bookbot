def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters_frequency(text):
    characters = {}
    for char in text.lower():
        if char not in characters:
            characters[char] = 0
        characters[char] += 1
    return characters

def sort_on(items):
    return items["num"]

def get_sorted_list_of_characters(characters):
    list=[]
    for entry in characters:
        list.append({"char": entry, "num": characters[entry]})
    list.sort(key=sort_on, reverse=True)
    return list