import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt")
data = fp.read()
print '\n-----\n'.join(tokenizer.tokenize(data))