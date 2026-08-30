# # Write count_words(text)  → dict of frequencies. Then most_common_word(text) that calls it and 
# # returns the top word
def count_words(text) : 
    frequeny = dict()
    text = text.split()
    for word in text :
        num = text.count(word)
        frequeny.update({word : num})
    return ((frequeny))


def most_common_word(text) :
    frequency = count_words(text)
    length = []
    for key , val in frequency.items() :
       length.append(val)

    for key, val in frequency.items() :
        if frequency[key] == max(length) :
            print(key,":",val) 


text = "Python is easy to learn, and Python is powerful because Python is used in many fields."
most_common_word(text)