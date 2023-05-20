def correct_sentence(sentence):
    sentence = sentence.capitalize()
    if sentence[-1] != ".":
        sentence = sentence + "."
    return sentence

#sentence = str(input("Введіть речення:"))
sentence = "greetings, friends."
print(correct_sentence(sentence))
