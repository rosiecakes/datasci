import re
import read
import operator


# https://en.wikipedia.org/wiki/Most_common_words_in_English

common_words = ['the', 'be', 'to', 'do', 'and', 'a', 'in',
                'that', 'have', 'of', 'it', 'for', 'with', 
                'not', 'he', 'as', 'i', 'you', 'at', 'on']
words = []        
counts = {}


def _clean_words(series):
    """ For all the words that make up headlines:
        - take out non-alpha chars
        - convert to lowercase
        
        Finally add to list and return it
    """
    
    for line in series:
        for word in str(line).split():
            words.append(word.lower())

    cleaned = [re.sub('[^a-zA-Z]+', '', word) for word in words]
    
    return cleaned


def get_word_count(series):
    """ For all the the cleaned words:
        - count each time it occurs
        - ignore blanks
        
        Return the top 100 most frequent words
    """
    
    cleaned = _clean_words(series)
    
    for word in cleaned:
        if word in common_words:
            continue
        elif word in counts:
            counts[word] += 1
        elif word == '':
            continue
        else:
            counts[word] = 1
        
    results = sorted(counts.items(), key = operator.itemgetter(1))

    results.reverse()
    
    return results[:101]


def get_series_count(series):
    """ Return the top 100 values in a series
    """
    
    return series.value_counts()[:101]
