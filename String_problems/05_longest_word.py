def longest_word_length(words):
    if not words:
        return 0
    return max(len(word) for word in words)

print(longest_word_length(["jump", "tooning", "haripreetam"]))