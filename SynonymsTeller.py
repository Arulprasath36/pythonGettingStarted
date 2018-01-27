from nltk.corpus import wordnet
import nltk
word = raw_input("Enter your word: ")
print("You have entered "+ word)
synonyms = wordnet.synsets(word)
meaning = synonyms[0].definition()
example = synonyms[0].examples()
print("Synonyms of "+ word+ " is "+ meaning)
print(example)

