import spacy

nlp_pipeline = spacy.load("it_core_news_sm")

with open("TransformedData/training_post_re.txt") as fin, \
    open("TransformedData/training_parsed.txt", "w") as fout:
    for line in fin:
        if line.startswith("# NEW"):
            line = line.strip()
            print(line, file=fout)
        else:
            parsed_text = nlp_pipeline(line.strip())
            for sentence in parsed_text.sents:
                for token in sentence:
                    print(f"{token.i}\t{token}\t{token.lemma_}\t{token.pos_}\t{token.morph}\t{token.dep_}\t{token.head.i}", file=fout)
                print("", file=fout)


with open("TransformedData/test_post_re.txt") as fin, \
    open("TransformedData/test_parsed.txt", "w") as fout:
    for line in fin:
        if line.startswith("# NEW"):
            line = line.strip()
            print(line, file=fout)
        else:
            parsed_text = nlp_pipeline(line.strip())
            for sentence in parsed_text.sents:
                for token in sentence:
                    print(f"{token.i}\t{token}\t{token.lemma_}\t{token.pos_}\t{token.morph}\t{token.dep_}\t{token.head.i}", file=fout)
                print("", file=fout)