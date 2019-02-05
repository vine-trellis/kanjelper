import requests
import io
import re

import core.dataops.put

disc = re.compile(r'([一-龯]+[一-龯ぁ-ゔゞァ-・ヽヾ゛゜ー]*)', re.UNICODE)
input_filename = 'resources/w5.txt'
words = set()
with io.open(input_filename, "r", encoding='utf-8') as f:
    for line in f:
        word = disc.search(line)
        if word:
            words.add(word.group(1))

chosen_kanji = words.pop()
payload = {'keyword': chosen_kanji}
r = requests.get('https://jisho.org/api/v1/search/words', params=payload)

entry = {
    'kanji' : chosen_kanji,
    'data' : r.json()['data'][0]
}
print(r.url)
print(r.json()['data'][0])
print(entry)