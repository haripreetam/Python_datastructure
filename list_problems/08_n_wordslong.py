def n_words_long(words,n):
    return [word for word in words if len(word)>n]

input_list = ["apple", "banananana" , "orange", "fig"]
print(n_words_long(input_list ,5))