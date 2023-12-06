import re

for filename in ["training", "test"]:

    file_content = open(f"TransformedData/{filename}.txt").read()

    regex_hashtags = re.compile(r"#([^ ]+)\b")
    new_file, n_subs = re.subn(regex_hashtags, r"\1", file_content)

    print("replaced", n_subs, "instances of hashtags")

    regex_youtube = re.compile(r"@YouTube\b")
    new_file, n_subs = re.subn(regex_youtube, "YouTube", new_file)

    print("replaced", n_subs, "instances of YouTube")

    regex_mentions = re.compile(r"@[^ ]+\b")
    new_file, n_subs = re.subn(regex_mentions, r"nome_utente", new_file)

    print("replaced", n_subs, "instances of user mentions")

    regex_mails = re.compile(r"\b[A-z0-9\.]+@[A-z0-9\.]+\.[a-z]+\b")
    new_file, n_subs = re.subn(regex_mails, r"indirizzo mail", new_file)

    print("replaced", n_subs, "instances of emails")

    regex_links = re.compile(r"\b([A-z0-9]+[\/\.][A-z0-9]+[\/\.]?)+[A-z0-9]*\b")
    new_file, n_subs = re.subn(regex_links, r"link", new_file)
    new_file, _ = re.subn(r"https?://", "", new_file)

    print("replaced", n_subs, "instances of links")

    with open(f"TransformedData/{filename}_post_re.txt", "w") as fout:
        print(new_file, file=fout)