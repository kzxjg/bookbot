def word_count(text):
    word_list = text.split()

    return(len(word_list))

def letter_count(text):
    letter_dict = {}
    text = text.lower()

    for i in text:
        letter_dict[i] = 0
    
    for i in text:
        if i in letter_dict:
            letter_dict[i] += 1
    
    return letter_dict    


def sorted_letters(text):
    dict_list = []
    new_text = ""
    for i in text:
        if i.isalpha():
            new_text += i

    letter_dict = letter_count(new_text)

    def sort_on(dict):
        return dict['count']

    for i in letter_dict:

        new_dict = {'letter' : None, 
                'count': None}

        new_dict['letter'] = i
        new_dict['count'] = letter_dict[i]
        dict_list.append(new_dict)
    

    dict_list.sort(reverse=True, key = sort_on)
    return dict_list
