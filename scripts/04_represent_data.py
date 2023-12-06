def represent(document):

    number_of_tokens = len(document)

    alpha = []
    for token in document:
        lemma = token[2]
        if all (c.isalpha() for c in lemma):
            alpha.append(1)
        else:
            alpha.append(0)

    token_lengths = []
    for token in document:
        form = token[1]
        token_lengths.append(len(form))

    frequencies = []
    for token in document:
        lemma = token[2]
        if lemma in vocabulary:
            frequencies.append(vocabulary[lemma])

    bag_of_words = []
    for token in document:
        lemma = token[2]
        if lemma in vocabulary_list:
            bag_of_words.append(vocabulary_list[lemma])

    return number_of_tokens, alpha, token_lengths, frequencies, bag_of_words


def build_representation(filename):
    with open(f"TransformedData/{filename}_parsed.txt") as fin, \
        open(f"TransformedData/{filename}_repr.txt", "w") as fout:

        doc = []
        doc_id = None
        doc_label = None

        for line in fin:
            line = line.strip().split("\t")

            if line[0] == "# NEW DOCUMENT:":
                number_of_tokens, alpha, token_lengths, frequencies, bag_of_words = represent(doc)


                if len(doc) > 0:
                    print(f"# NEW DOCUMENT:\t{doc_id}\t{doc_label}", file=fout)
                    print("n_tokens\t", number_of_tokens, file=fout)
                    print("alpha\t", " ".join(str(x) for x in alpha), file=fout)
                    print("frequencies\t", " ".join(str(x) for x in frequencies), file=fout)
                    print("token_lengths\t", " ".join(str(x) for x in token_lengths), file=fout)
                    print("bag_of_words\t", " ".join(str(x) for x in bag_of_words), file=fout)
                    print("", file=fout)

                doc_id = line[1]
                doc_label = line[3]
                doc = []

            else:
                if len(line)>1:
                    doc.append(line)

        number_of_tokens, alpha, token_lengths, frequencies, bag_of_words = represent(doc)
        if len(doc) > 0:
            print(f"# NEW DOCUMENT:\t{doc_id}\t{doc_label}", file=fout)
            print("n_tokens\t", number_of_tokens, file=fout)
            print("alpha\t", " ".join(str(x) for x in alpha), file=fout)
            print("frequencies\t", " ".join(str(x) for x in frequencies), file=fout)
            print("token_lengths\t", " ".join(str(x) for x in token_lengths), file=fout)
            print("bag_of_words\t", " ".join(str(x) for x in bag_of_words), file=fout)
            print("", file=fout)



vocabulary = {}
with open("TransformedData/training_parsed.txt") as fin:

    for line in fin:
        if not line.startswith("# NEW"):
            line = line.strip().split("\t")
            if len(line)>1:
                lemma = line[2]
                if not lemma in vocabulary:
                    vocabulary[lemma] = 0
                else:
                    vocabulary[lemma] += 1

#lemmas = [x for x in vocabulary.keys() if vocabulary[x]>2]

vocabulary_list = dict(zip(vocabulary.keys(), range(len(vocabulary))))

with open("TransformedData/vocabulary_one_hot.txt", "w") as fout:
    for item, item_id in vocabulary_list.items():
        print(f"{item_id}\t{vocabulary[item]}\t{item}", file=fout)

build_representation("training")
build_representation("test")