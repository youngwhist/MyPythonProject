"""Пример использования модуля text_stats."""
from text_stats import sentence_count, top_words, word_count

SAMPLE = "Мама мыла раму. Рама была чистая, мама была довольна."

if __name__ == "__main__":
    print("Слов:", word_count(SAMPLE))
    print("Частые слова:", top_words(SAMPLE))
    print("Предложений:", sentence_count(SAMPLE))
