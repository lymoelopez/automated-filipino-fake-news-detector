import re

def removeCharactersAndLowercase(text):
    text = re.sub('https?://\S+|www\.\S+', '', text)                    # remove URLs
    text = re.sub(r'\S+@\S+', '', text)                                 # remove emails
    text = re.sub(r'#\w+', '', text)                                    # remove hashtags
    text = re.sub('\[.*?\]', '', text)                                  # remove square brackets and their contents
    text = re.sub('\(.*?\)', '', text)                                  # remove parenthesis and their contents
    text = re.sub('<.*?>+', '', text)                                   # remove angle brackets and the characters inside them
    text = re.sub('\n', ' ', text)                                      # remove newline characters
    text = re.sub(r'[^\x00-\x7f]',r'', text)                            # remove non-ASCII characters (e.g. emojis, greek letters, chinise characters
    text = re.sub('\s+',' ',text)                                       # remove extra whitespaces
    text = text.strip()                                                 # remove whitespaces at the beginning and end of the text
    text = text.lower()                                                 # convert to lowercase

    return text
