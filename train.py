import argparse
import json
import re

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', type=str)
parser.add_argument('--model', type=str)
args = parser.parse_args()
if args.input_dir is not None:
    pass
else:
    text = input()
text = text.lower()
regex = re.compile('[^а-яА-Я \n]')
text = regex.sub('', text)
list_of_textes = list(text.split('\n'))
prefix1 = {}
prefix2 = {}
for text in list_of_textes:
    text = list(text.split())
    if len(text) >= 2:
        if text[0] not in prefix1:
            prefix1[text[0]] = []
        prefix1[text[0]].append(text[1])
    if len(text) >= 3:
        for i in range(2, len(text)):
            previous = " ".join(text[i - 2: i])
            if previous not in prefix2:
                prefix2[previous] = []
            prefix2[previous].append(text[i])
            if text[i - 1] not in prefix1:
                prefix1[text[i - 1]] = []
            prefix1[text[i - 1]].append(text[i])
with open("model.json", "w") as model_file:
    json.dump((prefix1, prefix2), model_file)
