# I've only used this function with limited data and haven't tested it --Emilio Lehoucq 2/15/23

from nltk import word_tokenize
import re

def my_parser(text, words_to_remove, remove_http = False):
    """
    Function to parse text.
    
    Input:
        text (string). Text to be parsed.
        words_to_remove (list). List of words to be removed (such as stopwords).
        remove_http (Boolean). If True, removes hyperlinks from text before tokenizing it. Defaults to False.
    Output:
        List of parsed words.

    Dependencies:
        from nltk import word_tokenize
        import re (necessary if remove_http = True)
    
    Code inspired from:
        - https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python/40823105#40823105
        - https://deepnote.com/@code-along-tutorials/Natural-Language-Processing-in-Python-Exploring-Word-Frequencies-with-NLTK-47ec085a-7a46-4f5d-89a1-e08be7d164c5
    """
    # if remove_http = True, remove hyperlinks:
    if remove_http: text = re.sub(r'http\S+', '', text)

    # Tokenize:
    words = word_tokenize(text)

    # Remove punctuation, use lower case, and remove words_to_remove:
    result = []
    for word in words:
        if word.isalpha():
            if word.lower() not in words_to_remove:
                result.append(word.lower())

    # Return list of parsed words:           
    return result