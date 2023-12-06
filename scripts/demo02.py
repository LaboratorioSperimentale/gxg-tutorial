text = "Sei anni dopo una riforma che fu definita epocale, "\
        "la scuola superiore cambia volto. Crolla il liceo "\
        "classico e cambia pelle lo scientifico, che diventa sempre più light."



# # Import SpaCy and parse text

import spacy

nlp_pipeline = spacy.load("it_core_news_sm")
parsed_text = nlp_pipeline(text)


# # Print sentences one by one

sentences = list(parsed_text.sents)

# for sentence in sentences:
#     print("SENTENCE:", sentence)


# Print tokens

i = 0

for sentence in sentences:
    print("SENTENCE N.", i)
    i = i+1
    
    for token in sentence:
        print(token,"\t", token.lemma_,"\t", token.pos_)

    print()


# # Print morphological analysis

# for sentence in sentences:
#     print("SENTENCE N.", i)
#     i = i+1
    
#     for token in sentence:
#         print(token,"\t", token.lemma_,"\t", token.morph)

#     print()


# # Print dependency parsing

# for sentence in sentences:
#     print("SENTENCE N.", i)
#     i = i+1
    
#     for token in sentence:
#         print(token.i, "\t", token,"\t", token.head.i,"\t", token.dep_)

#     print()



# # Save syntactic trees to a file

# from spacy import displacy
# from pathlib import Path

# #svg = displacy.render(sentences, style="dep", jupyter=False)
# for i, sent in enumerate(sentences):
#     svg = displacy.render(sent, style="dep", jupyter=False)
    
#     filepath = Path(f"dependency_plots_{i}.svg")
#     filepath.open("w", encoding="utf-8").write(svg)