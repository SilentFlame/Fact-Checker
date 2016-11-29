import sopex
import nltk
from nltk import tokenize

fp = open("test.txt")
data = fp.read()

sentences = tokenize.sent_tokenize(data)

triplets = []
for i in xrange(len(sentences)):
	p=sopex.extract(sentences[i])    # sopex.extractor.SOPTriplet object. where every object will have .object, .subject, .predicate attributes.
	triplets.append(p)

p = input("Input the fact please: ")
target = sopex.extract(p)

flag = 0
for j in range(len(triplets)):
	if(triplets[i]==target):
		flag=1
		break
	else:
		continue
	# here we can put an else if for the third part(OBJECT) as an antonym and put flag=2 to say that the fact is false or what?


if(flag==1):
	print "The fact mentioned above is True."
else:
	print "The fact mentioned above is False."



