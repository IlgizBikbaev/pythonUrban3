def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.upper()
    for word in other_words:
       if root_word in word.upper() or word.upper() in root_word:
           same_words.append(word)
    return same_words




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)

