import lemmatization


def test_lemmatize():
    dictionary = {"short": 0,
                  "explanation": 0,
                  "clearly": 0
                  }
    text = "You can see that you understand the purpose, even if the introduction is a bit short. For the following " \
           "you may want to give the brief explanation of the symbols their own page and not put them in the " \
           "introduction. The symbols and explanations that go with it are clearly stated "
    assert lemmatization.lemmatize(dictionary, text) == {'short': 1, 'explanation': 2, 'clearly': 1}, \
        "Should be {'short': 1, 'explanation': 2, 'clearly': 1}"


def test_synonyms():
    assert lemmatization.synonyms("woman") == {'char', 'womanhood', 'adult_female', 'woman', 'charwoman', 'fair_sex',
                                               'cleaning_woman', 'cleaning_lady'}, "Should be {'char', 'womanhood', " \
                                                                                   "'adult_female', 'woman', " \
                                                                                   "'charwoman', 'fair_sex', " \
                                                                                   "'cleaning_woman', 'cleaning_lady'} "


def test_get_words():
    wordlist = ['cookie', 'candy', 'cake']
    text = "The girl with a cookie in her hand also wanted to eat candy and a piece of cake."
    assert lemmatization.get_words(wordlist, text) == ['cookie', 'candy', 'cake'], "Should be ['cookie', 'candy', " \
                                                                                   "'cake'] "


def test_post_tag():
    text = "In sprint 3 I was busy making an actionplan actionplan to analyze scientific articles. I first wrote the " \
           "plan of action in the form of a summary. "
    word_sort = "VB"
    assert lemmatization.pos_tag(text, word_sort) == ['analyze'], "Should be ['analyze']"


def test_word_count():
    text = "This is the.. test test text"
    assert lemmatization.word_count(text) == 6, "Should be 6"


def test_unique_word_count():
    text = "This is the.. test test text"
    assert lemmatization.unique_word_count(text) == 5, "Should be 5"


test_lemmatize()
test_synonyms()
test_get_words()
test_post_tag()
test_word_count()
test_unique_word_count()
print("All tests passed")
