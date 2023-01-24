#=====importing libraries===========
import spacy #NLP library

#loading the language model and assign it to a variable.
nlp = spacy.load( 'en_core_web_md' )

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''Output
0.5929929675536907 (Highest similarity as both animals)
0.40415016164997786 (Middle similarity as Monkey and banana connacted as Monkey eats banana)
0.22358825939615987 (Lowest similarity as cats dont eat banana)
'''
nlp_simpler = spacy.load( 'en_core_web_sm' )

word1 = nlp_simpler("cat")
word2 = nlp_simpler("monkey")
word3 = nlp_simpler("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("-"*100)

tokens = nlp('cat apple monkey banana ' )

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
print("-"*100)

sentence_to_compare = "Why is my cat on the car"

#list of sentences
sentences = [ "where did my dog go" ,
"Hello, there is my car" ,
"I\'ve lost my car in my car" ,
"I\'d like my boat back" ,
"I will name my dog Diana" ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)