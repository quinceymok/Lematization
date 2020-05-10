from lematization import lemmatize, synonyms, lemmatize_new, nltk, pos_tag


def main():
    description = "In sprint 3 I was busy making an actionplan actionplan to analyze scientific articles. I first wrote the " \
                  "plan of action in the form of a summary. "

    review = "sprint 3 was good. very excellent actionplan  written!"

    dictionary = dict.fromkeys(pos_tag(description, ["NN"]), 0)
    a = lemmatize(dictionary, review)
    print(a)


if __name__ == "__main__":
    main()
