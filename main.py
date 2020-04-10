from lematization import lemmatize


def main():
    a = {"short": 0,
         "explanation": 0,
         "clearly": 0
         }
    review = "You can see that you understand the purpose, even if the introduction is a bit short. For the following " \
             "you may want to give the brief explanation of the symbols their own page and not put them in the " \
             "introduction. The symbols and explanations that go with it are clearly stated "
    print(lemmatize(a, review))
    help(lemmatize)


if __name__ == "__main__":
    main()
