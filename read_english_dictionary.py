def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def save_words(words):
    df=open('5_letter_words.txt','w')
    for word in words:
        if len(word) == 5:
            df.write(word.upper())
            df.write('\n')
    df.close()


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    save_words(english_words)
