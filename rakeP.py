import rake
import operator
import io

stoppath = "SmartStoplist.txt"

rake_object = rake.Rake(stoppath, 5, 3, 5)

#sample_file = io.open("data/docs/fao_test/w2167e.txt", 'r',encoding="iso-8859-1")
sample_file = io.open("/home/saba/minor project/RAKE/data/docs/test/india.txt", 'r',encoding="iso-8859-1")

text = sample_file.read()
#print(text)

keywords = rake_object.run(text)
for i in keywords:
	print(i[0])
		#print(i[1])
	#print('\n')
#print(keywords,sep='\n')


'''
rake_object = rake.Rake(stoppath)

text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
       "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
       "systems and systems of mixed types."



sentenceList = rake.split_sentences(text)

for sentence in sentenceList:
    print("Sentence:", sentence)

stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
print("Phrases:", phraseList)

wordscores = rake.calculate_word_scores(phraseList)

keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
    print("Keyword: ", keyword[0], ", score: ", keyword[1])

print(rake_object.run(text))'''


