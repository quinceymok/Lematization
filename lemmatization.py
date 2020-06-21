import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

wordnet_lemmatizer = WordNetLemmatizer()


def lemmatize(word_dictionary, text):
    """
    The function will remove the punctuations in the text and then lemmatize it.
    Then it adds up all the words with the same prefix/suffix that were given in the word_dictionary
    :param word_dictionary: a dictionary with words and a counter
    :param text: string
    :return: the given dictionary with the amount of words.
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
    """
    This function will look up all synonyms for a given word as known in wordnet.
    :param word: a string
    :return: a set of strings
    """
    synonyms_list = []
    for synonym in wordnet.synsets(word):
        for i in synonym.lemmas():
            synonyms_list.append(i.name())
    return set(synonyms_list)


def get_words(word_list, text):
    """
    Takes a wordlist and look for all of those words in the given text
    :param word_list: list of words
    :param text: string
    :return: returns a list with words that were found
    """
    found_words = []

    punctuations = "?:!.,;"
    sentence_words = nltk.word_tokenize(text)
    # remove the punctuations
    for word in sentence_words:
        if word in punctuations:
            sentence_words.remove(word)
    # check for all the nouns
    for word in sentence_words:
        lemmatized_word = wordnet_lemmatizer.lemmatize(word, pos="n")
        # If it's in the word_list append the word to found_words
        if lemmatized_word in word_list:
            found_words.append(word)

    return found_words


def pos_tag(text, word_sort):
    """
    This function looks in the text for all words that are the same as the word sort.

    The following options for word_sort are available: CC, CD, DT, EX, FW, IN, JJ, JJR, JJS,
    LS, MD, NN, NNS, NNP, NNPS, PDT, POS, PRP, PRP$, RB, RBR, RBS, RP, TO, UH, VB, VBD, VBG,
    VBN, VBP, VBZ, WDT, WP, WP$, WRB
    :param text: string
    :param word_sort: POS tag string
    :return: returns a list of words with the found words in text
    """
    sentences = nltk.sent_tokenize(text)  # tokenize text
    words = []  # empty to array to hold all words

    for sentence in sentences:
        for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
            if pos in word_sort:
                if word not in words:
                    words.append(word)
    return words


def word_count(text):
    """
    calculates the amount of words in a given text.
    :param text: string
    :return: integer
    """
    word_list = nltk.word_tokenize(text)
    for word in word_list:
        if not word.isalpha():
            word_list.remove(word)
    return len(word_list)


def unique_word_count(text):
    """
    calculates the unique amount of words in a given text.
    :param text: string
    :return: integer
    """
    word_list = nltk.word_tokenize(text)
    for word in word_list:
        if not word.isalpha():
            word_list.remove(word)

    return len(set(word_list))
