import pickle, re

with open('../resources/as_wordFreq.pickle', 'rb') as f:
    word_freq = pickle.load(f)

    
def load_wordfq(word_freq):
    avail_word = set(word_freq.keys())
    
    def query_freq(string):
        if string not in avail_word:
            return(0)
        else:
            return(word_freq[string])
    
    return(query_freq)


def load_is_ancient():
    pat = re.compile(r'^《(.+?)》')

    def is_ancient(quote_str):
        nonlocal pat
        matched = pat.search(quote_str)

        if matched is None:
            return(False)
        else:
            return(True)
    
    return(is_ancient)


def load_parse_examples():
    pat = re.compile(r'「(.+?)」')
    
    def parse_examples(example_str):
        nonlocal pat
        matched = pat.findall(example_str)
        return(matched)

    return(parse_examples)


## Initialize functions
query_as4_freq = load_wordfq(word_freq)
is_classic = load_is_ancient()
get_examplar_words = load_parse_examples()