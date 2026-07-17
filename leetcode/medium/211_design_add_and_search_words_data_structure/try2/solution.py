import string


class WordDictionary:
    def __init__(self):
        # store just the full words
        self._words = set()

    def addWord(self, word: str) -> None:
        # add the exact word
        self._words.add(word)

    def search(self, word: str) -> bool:
        # if there’s no wildcard, direct lookup
        if "." not in word:
            return word in self._words

        letters = string.ascii_lowercase
        # start with one empty prefix
        candidates = [""]

        # for each position, either extend with the literal
        # or branch on all letters if it’s '.'
        for c in word:
            if c == ".":
                candidates = [prefix + l for prefix in candidates for l in letters]
            else:
                candidates = [prefix + c for prefix in candidates]

        # finally, see if any fully formed candidate is in our word-set
        return any(candidate in self._words for candidate in candidates)
