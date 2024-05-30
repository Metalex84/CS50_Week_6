from cs50 import get_string


def main():

    text = get_string("Text: ")

    L = count_letters(text) / count_words(text) * 100
    S = count_sentences(text) / count_words(text) * 100

    c_index = round(0.0588 * L - 0.296 * S - 15.8)

    if c_index < 1:
        print("Before Grade 1")
    elif c_index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {c_index}")


def count_letters(text):

    letters = 0
    for caracter in text:
        c = ord(caracter)
        if (c >= 65 and c <= 90) or (c >= 97 and c <= 122):
            letters += 1

    return letters


def count_words(text):

    if not text:
        return 0
    words = 1
    length = len(text)
    for i in range(length):
        if text[i].isspace():
            j = i
            if not text[j + 1].isspace():
                words += 1
            else:
                while text[j].isspace():
                    j += 1
    return words


def count_sentences(text):

    sentences = 0
    length = len(text)
    for i in range(length):
        if text[i] == '!' or text[i] == '?' or text[i] == '.':
            sentences += 1
    return sentences


if __name__ == "__main__":
    main()
