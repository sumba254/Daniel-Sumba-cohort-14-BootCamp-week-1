def word_count(sentence):
	wordcount={}
	words = sentence.split()
	for word in words:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1
	for item in wordcount.items():
		print("{}:\t{}".format(*item))
word_count("hello  world")
