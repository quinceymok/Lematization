# een prototype waarmee je synoniemen uit een review haalt en vergelijkt met de woorden uit de dictionnary

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

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


def synonyms(word):
    synonyms = []
    """text"""
    for synonym in wordnet.synsets(word):
        for l in synonym.lemmas():
            synonyms.append(l.name())
    return set(synonyms)


def lemmatize_new(word_list, text):
    amount = []

    punctuations = "?:!.,;"
    sentence_words = nltk.word_tokenize(text)
    # remove the punctuations
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)
    # check for all the nouns
    for word in sentence_words:

        lemmatized_word = wordnet_lemmatizer.lemmatize(word, pos="n")
        if lemmatized_word in word_list:
            amount.append(word)

    return amount


def pos_tag(text, word_sort):
    sentences = nltk.sent_tokenize(text)  # tokenize text
    words = []  # empty to array to hold all nouns

    for sentence in sentences:
        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if pos in word_sort:
                if word not in words:
                    words.append(word)
    return words


def word_count(text, unique):
    """
    this function will count the words in the text. It will return unique words if (unique == True).
    """
    punctuations = "?:!.,;"
    word_list = nltk.word_tokenize(text)
    for word in word_list:
        if word in punctuations:
            word_list.remove(word)

    if unique:  # check if unique words == True, return the length of the list as a set
        return len(set(word_list))
    else:
        return len(word_list)


def word_count_quality(description, review):


def check_quality(description, review):
    """
    Returns the average of all the quality checks
    :param description: string
    :param review: string
    :return:
    """
    all_qualities = [word_count_quality(description, review), sentiment_quality(description, review) ]


