# een prototype waarmee je synoniemen uit een review haalt en vergelijkt met de woorden uit de dictionnary

import nltk
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()


def lemmatize(word_dictionary, text):
    """
    The function will remove the punctuations in the text. Then lemmatize the text and
    return the given dictionary with the amount of words.
    """
    punctuations = "?:!.,;"
    sentence_words = nltk.word_tokenize(text)
    # remove the punctuations
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)
    # check for all the nouns
    for word in sentence_words:
        lemmatized_word = wordnet_lemmatizer.lemmatize(word, pos="n")
        if lemmatized_word in word_dictionary:
            word_dictionary[lemmatized_word] = word_dictionary[lemmatized_word] + 1
            sentence_words.remove(word)
    # check for all the verbs
    for word in sentence_words:
        lemmatized_word = wordnet_lemmatizer.lemmatize(word, pos="v")
        if lemmatized_word in word_dictionary:
            word_dictionary[lemmatized_word] = word_dictionary[lemmatized_word] + 1
            sentence_words.remove(word)
    # check all adjectivs
    for word in sentence_words:
        lemmatized_word = wordnet_lemmatizer.lemmatize(word, pos="a")
        if lemmatized_word in word_dictionary:
            word_dictionary[lemmatized_word] = word_dictionary[lemmatized_word] + 1
            sentence_words.remove(word)
    # check all adverbs
    for word in sentence_words:
        lemmatized_word = wordnet_lemmatizer.lemmatize(word, pos="r")
        if lemmatized_word in word_dictionary:
            word_dictionary[lemmatized_word] = word_dictionary[lemmatized_word] + 1
            sentence_words.remove(word)

    return word_dictionary
