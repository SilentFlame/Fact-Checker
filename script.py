import sopex
import nltk
from nltk import tokenize
import sopex
import nltk
from nltk.corpus import wordnet
fp = open("test.txt")
data = fp.read()
dd={}      #Dictionary for handling negation cases
sentences = tokenize.sent_tokenize(data)
for x in xrange(len(sentences)):
	if sentences[x].find("not") !=-1:	
		dd[sentences[x]]=1
	else:
		dd[sentences[x]]=0		
	print sentences[x]
	

triplets = []
for i in xrange(len(sentences)):
	p=sopex.extract(sentences[i])    # sopex.extractor.SOPTriplet object. where every object will have .object, .subject, .predicate attributes.
	triplets.append(p)

p = input("Input a fact from the doc. please: ")
target = sopex.extract(p)


#print triplets[0].object
#need t

flag1 = -1
flag2 = -1
flag = 0
for j in xrange(len(triplets)):
	#if triplets[j].object == target.object and triplets[j].predicate == target.predicate and triplets[j].subject == target.subject:
	w1 = wordnet.synsets(triplets[j].object)[0]
	w2 = wordnet.synsets(target.object)[0]
	w11 = wordnet.synsets(triplets[j].predicate)[0]
	w22 = wordnet.synsets(target.predicate)[0]
	print w1.wup_similarity(w2)
	print w11.wup_similarity(w22)
	if w1.wup_similarity(w2)>=0.5 and w11.wup_similarity(w22)>=0.5 and triplets[j].subject == target.subject:		
		#sprint "aaya"
		flag1=1
		if p.find("not") !=-1:
			flag1=0
		if dd[sentences[j]] == 1:
			flag2=1	
		if flag1==0 and flag2==1:
			flag=1
			break
		if dd[sentences[j]]!=1 and p.find("not") ==-1:
			flag=1
			break	

	# here we can put an else if for the third part(OBJECT) as an antonym and put flag=2 to say that the fact is false or what?
	

if flag==1 :
	print "The fact mentioned above is True."
else:
	print "The fact mentioned above is False."


