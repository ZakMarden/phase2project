def make_snippet(str):
    wordlist = str.split()
    wordnum = len(wordlist)
    if wordnum <= 5:
        return str
    else:
        wordlist = wordlist[:5]
        new_str = " ".join(wordlist)
        return new_str + "..."