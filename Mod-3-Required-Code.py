def word_mixer(word_list):
    new_words = []
    word_list.sort()
    while len(word_list) > 5:
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop(-1))
    return new_words


inp = input("insert a poem or something: ")

word_list = inp.split()
leng = len(word_list)
for i in range(0, leng):
    if len(word_list[i]) >= 4:
        word_list[i] = word_list[i].lower()
    elif len(word_list[i]) >= 7:
        word_list[i] = word_list[i].upper()

mixed_word_list = word_mixer(word_list)
print(" ".join(mixed_word_list))

