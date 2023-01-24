#=====importing libraries===========
import spacy #NLP library

#loading the language model and assign it to a variable.
nlp = spacy.load( 'en_core_web_md' )

#passing the string through the language model
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#similarity check
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''Output
0.5929929675536907 (Highest similarity as both animals)
0.40415016164997786 (Middle similarity as Monkey and banana connacted as Monkey eats banana)
0.22358825939615987 (Lowest similarity as cats dont eat banana)
'''

print("-"*100)

#loading the simplier language model and assign it to a variable.
nlp_simpler = spacy.load( 'en_core_web_sm' )

#passing the string through the language model
word1 = nlp_simpler("cat")
word2 = nlp_simpler("monkey")
word3 = nlp_simpler("banana")

#similarity check
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''Output
UserWarning: [W007] The model you're using has no word vectors loaded
                    'en_core_web_md'     'en_core_web_sm'    
cat vs monkey    > 0.5929929675536907    0.6770567131180597
banana vs monkey > 0.40415016164997786   0.7276310914874259
cat vs banana    > 0.22358825939615987   0.6806929608512433 

simplier model says cat-banana more similar than cat-monkey / however it says that banana-monkey is well related.
the 'en_core_web_sm' model not give useful similarity judgements, not consistant.
'''

print("-"*100)


tokens = nlp('cat apple monkey banana ' )

#for loop to compare each word
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
print("-"*100)

#passing the string through the language model
sentence_to_compare = "Why is my cat on the car"

#list of sentences
sentences = [ "where did my dog go" ,
"Hello, there is my car" ,
"I\'ve lost my car in my car" ,
"I\'d like my boat back" ,
"I will name my dog Diana" ]

model_sentence = nlp(sentence_to_compare)

#for loop to compare each sentence to "Why is my cat on the car"
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)