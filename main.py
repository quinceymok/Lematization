from lematization import lemmatize, synonyms, lemmatize_new


def main():
    b = synonyms('short')
    a = [b,]
    print(b)
    review = "You can see that you understand the purpose, even if the introduction is a bit shortstop short clear clearly clear. For the following " \
             "you may want to give the brief explanation of the symbols their own page and not put them in the " \
             "introduction. The symbols and explanations that go with it are clearly stated "
    print(lemmatize_new(b, review))


if __name__ == "__main__":
    main()
