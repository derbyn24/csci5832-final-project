import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

# uncomment these to download when running for the first time
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('wordnet')

def sentence_detection(text):
    sentences = sent_tokenize(text)
    return sentences

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def part_of_speech_tagging(text):
    tokens = tokenize(text)
    pos_tagged = pos_tag(tokens)
    return pos_tagged

def word_frequency(text):
    #TODO
    return text

def convert_pos_to_wordnet(tag):
    if tag.startswith('J'):
        return 'a'  # Adjective
    elif tag.startswith('V'):
        return 'v'  # Verb
    elif tag.startswith('N'):
        return 'n'  # Noun
    elif tag.startswith('R'):
        return 'r'  # Adverb
    else:
        return 'n'  # Default to noun

def lemmatization(text):
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tagged_tokens = pos_tag(tokens)
    lemmatized_tokens = [lemmatizer.lemmatize(token, convert_pos_to_wordnet(pos_tag)) for token, pos_tag in tagged_tokens]
    return lemmatized_tokens

def chunking(text):
    #TODO
    return text

