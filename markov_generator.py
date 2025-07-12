import random
import re
from collections import defaultdict

def load_text(text):
    text = text.lower()
    return re.sub(r'[^\w\s]', '', text)

def build_markov_chain(text, n=2):
    words = text.split()
    markov_chain = defaultdict(list)
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        next_word = words[i+n]
        markov_chain[key].append(next_word)
    return markov_chain

def generate_text(chain, length=50):
    key = random.choice(list(chain.keys()))
    result = list(key)
    for _ in range(length):
        next_words = chain.get(key)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        key = tuple(result[-len(key):])
    return ' '.join(result)
