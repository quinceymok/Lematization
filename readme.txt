# Lemmatization
Lemmatization is een Python module dat inzicht geeft om teksten te analyseren.

## Installation
Deze module maakt gebruik van NLTK. Zie [NLTK](http://www.nltk.org/install.html) om NLTK te installeren.

Via nltk.download() download je de volgende modules: punkt, snowball_data
Ook download je de volgende packages in de corpora: gazetteers, wordnet

Zet de lemmatization module in je project om er gebruik van te maken.

## Usage
```python
import lemmatization

lemmatization.word_count("een grote tekst") # returns '3'
lemmatization.word_count("een zeer grotere tekst") # returns '4'
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
