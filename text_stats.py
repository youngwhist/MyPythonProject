import re,collections
def word_count(text):
    return len(re.findall(r"\w+",text))
def TopWords(text,n=3):
    words=re.findall(r"\w+",text.lower())
    return collections.Counter(words).most_common(n)
def sentence_count(text):
    return len([s for s in re.split(r"[.!?]+",text) if s.strip()])
