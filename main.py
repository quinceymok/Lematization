from lematization import lemmatize, synonyms, lemmatize_new, nltk, pos_tag, word_count
from nltk.stem import WordNetLemmatizer

def main():
    description = "In sprint 3 I was busy making an actionplan actionplan to analyze  scientific articles. I first wrote the " \
                  "plan of action in the form of a summary. "

    review = "sprint 3 was good. very excellent analyzed actionplan actionplan written!"

    dictionary = dict.fromkeys(pos_tag(description, ["NN"]), 0)
    a = lemmatize(dictionary, review)

    tekst = "Jesper en Quincey gaan op avontuur"
    print(a)

if __name__ == "__main__":
    main()
