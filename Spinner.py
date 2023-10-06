# This assignment is completed independently

import random


class Spinner:
    def __init__(self, synonym_file):
        self.synonyms = self._load_synonyms(synonym_file)

    def _load_synonyms(self, synonym_file):
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for line in file:
                word, syns = line.strip().split(':')
                synonyms[word] = syns.split(',')
        return synonyms

    def spin_text(self, text, probability):
        words = text.split()
        spun_words = []
        for word in words:
            if word in self.synonyms and random.randint(1, 100) > probability:
                spun_words.append(random.choice(self.synonyms[word]))
            else:
                spun_words.append(word)
        return ' '.join(spun_words)
