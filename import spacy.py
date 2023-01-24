import spacy

nlp = spacy.load( 'en_core_web_md' )

sentence_to_compare = "Why is my cat on the car"

sentences = [ "where did my dog go" ,
"Hello, there is my car" ,
"I\'ve lost my car in my car" ,
"I\'d like my boat back" ,
"I will name my dog Diana" ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)