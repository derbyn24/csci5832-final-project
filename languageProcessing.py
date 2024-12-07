import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.tree import Tree
from fileReader import get_first_line

def sentence_detection(text):
    sentences = sent_tokenize(text)
    return sentences

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

def part_of_speech_tagging(text):
    tokens = tokenize(text)
    pos_tagged = pos_tag(tokens)
    strings = []
    for token in pos_tagged:
        strings.append(str(token[0]) + " [" + str(token[1]) + "]")
    strings = " ".join(strings)
    return strings
    # text, tags = ""
    # for token in pos_tagged:
    #     text += str(token[0]) + "\t"
    #     tags += str(token[1]) + "\t"
    # string = text + "\n" + tags
    # return string

def word_frequency(text, preview = False):
    tokens = tokenize(text)
    fq = FreqDist(token.lower() for token in tokens)
    if preview:
        return fq.most_common(10)
    string = ""
    for word in fq:
        string += word + " {" + str(fq.get(word)) + "}\n"
    return string

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
    string = " ".join(lemmatized_tokens)
    return string

def get_first_sentence():
    line = get_first_line()
    first_sentence = sentence_detection(line)[0]
    return first_sentence

def named_entity_recognition(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)
    string = ""
    for chunk in named_entities:
        if isinstance(chunk, Tree):
            entity = " ".join(c[0] for c in chunk)
            label = chunk.label()
            string += " " + label + " " + entity
    string += " "
    return string

