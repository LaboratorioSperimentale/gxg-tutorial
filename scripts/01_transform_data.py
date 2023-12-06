training_files = ["Data/Training/GxG_Twitter.txt", "Data/Training/GxG_YouTube.txt"]

with open("TransformedData/training.txt", "w") as fout:

    for filename in training_files:
        with open(filename) as fin:
            for line in fin:
                if line.startswith("<d"):
                    linesplit = line.strip().split('"')
                    doc_id, genre, gender = linesplit[1], linesplit[3], linesplit[5]

                    print(f"# NEW DOCUMENT:\t{doc_id}\t{genre}\t{gender}", file=fout)
                    doc = []
                elif line.startswith("</"):
                    print("\n".join(doc), file=fout)
                    print("", file=fout)

                else:
                    line = line.strip()
                    doc.append(line)


test_files = ["Data/Test/GxG_Twitter.txt", "Data/Test/GxG_YouTube.txt"]

with open("TransformedData/test.txt", "w") as fout:
    for filename in test_files:
        with open(filename) as fin:

            for line in fin:
                if line.startswith("<d"):
                    linesplit = line.strip().split('"')
                    doc_id, genre, gender = linesplit[1], linesplit[3], linesplit[5]

                    print(f"# NEW DOCUMENT:\t{doc_id}\t{genre}\t{gender}", file=fout)
                    doc = []
                elif line.startswith("</"):
                    print("\n".join(doc), file=fout)
                    print("", file=fout)

                else:
                    line = line.strip()
                    doc.append(line)