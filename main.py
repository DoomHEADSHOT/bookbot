from numpy import char, sort


def main():
    filePath = "books/frankenstein.txt"
    text = get_book_text(filePath)
    print(f"this book has {word_counter(text)} words")
    list = sortandreverse_dict_to_list(text)
    for i in list:
        if i['char'].isalpha():
            print(f"we have {i['char']} {i['num']} times")
    print("-- End Report--")
    
def sortandreverse_dict_to_list(text):
    sorted_list = []
    dict_sorted = dict(
        sorted(char_count_dict(text).items(), key=lambda item: item[1] )
    )
    for ch in dict_sorted:
        sorted_list.append({"char":ch ,"num":dict_sorted[ch]})
    sorted_list.reverse()
    return sorted_list


def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def word_counter(text):
    return len(text.split())

def char_count_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered]=1
    return chars


main()


