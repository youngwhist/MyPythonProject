"""Статистика текста: слова, частые слова, предложения."""
import collections
import re

WORD = re.compile(r"\w+")


def word_count(text):
    """Количество слов в тексте."""
    return len(WORD.findall(text))


def top_words(text, n=3):
    """n самых частых слов (без учёта регистра)."""
    words = WORD.findall(text.lower())
    return collections.Counter(words).most_common(n)


def sentence_count(text):
    """Количество предложений (по знакам . ! ?)."""
    return len([s for s in re.split(r"[.!?]+", text) if s.strip()])
