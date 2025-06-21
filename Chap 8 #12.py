def pig_latin(word):
    if len(word) == 1:
        return word.upper() + "AY"
    else:
        # Remove first letter, add it to end, then add "ay"
        return (word[1:] + word[0]).upper() + "AY"

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    pig_latin_words = [pig_latin(word) for word in words]
    result = " ".join(pig_latin_words)
    print(result)

if __name__ == "__main__":
    main()
