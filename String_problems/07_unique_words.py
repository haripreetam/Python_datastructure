def sorted_unique_words():
    words = input("Enter the word").split(',')
    words = sorted(set(words))
    print(" ".join(words))

sorted_unique_words()