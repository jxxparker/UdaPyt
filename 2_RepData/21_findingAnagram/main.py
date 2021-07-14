def find_anagrams(letters, words):
    # Create a dictionary mapping the canonical representation of a word to all anagrams of those letters.
    lookup = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in lookup:
            lookup[key] = set()
        lookup[key].add(word)

    # Search the lookup table for the queried letters.
    search = ''.join((sorted(letters)))
    return lookup.get(search, set())


    