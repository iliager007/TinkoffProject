import argparse
import json
import random

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str)
parser.add_argument('--prefix', type=str)
parser.add_argument('--length', type=int)
args = parser.parse_args()

with open(args.model, 'r') as model_file:
    model = json.load(model_file)
prefix1 = model[0]
prefix2 = model[1]

length = args.length

if args.prefix is not None:
    beginning = args.prefix
else:
    beginning = random.choice(list(prefix2.keys()))

continuation = []
for i in range(length):
    if beginning in prefix2:
        continuation.append(random.choice(prefix2[beginning]))
        beginning = beginning.split()[1] + " " + continuation[-1]
    elif beginning.split()[1] in prefix1:
        continuation.append(random.choice(prefix1[beginning.split()[1]]))
        beginning = beginning.split()[1] + " " + continuation[-1]
    else:
        continuation.append(random.choice(random.choice(list(prefix1.values()))))
        beginning = beginning.split()[1] + " " + continuation[-1]

print(*continuation)
