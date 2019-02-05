import requests
import io
import re
import sys
import os
import glob

sys.path.append(os.getcwd() + '/core/dataops')
import put

disc = re.compile(r'([一-龯]+[一-龯ぁ-ゔゞァ-・ヽヾ゛゜ー]*)', re.UNICODE)

for kanji_list in glob.glob('resources/*.txt'):
    print(kanji_list)
    words = set()
    with io.open(kanji_list, "r", encoding='utf-8') as f:
        for line in f:
            word = disc.search(line)
            if word:
                words.add(word.group(1))

    for kanji in words:
        payload = {'keyword': kanji}
        r = requests.get('https://jisho.org/api/v1/search/words', params=payload)
        print(r.url)
        if r.json()['data']:
            entry = {
                'kanji' : kanji,
                'data' : r.json()['data'][0]
            }
            put.putToTable('Kanji', entry)
