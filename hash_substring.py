# python3

def read_input():
    text = input()
    if(text[0] == "I"):
        pattern = input()
        text = input()
        
    else:
        if(text[0] == "F"):
            #textDalits = []
            text = input()
            fails = open(text)
            text = fails.read()
            textDalits = text.split("\n")
            pattern = textDalits[0]
            text = textDalits[1]


    return (pattern, text)
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    pattern_len = len(pattern)
    text_len = len(text)
    
    pattern_hash = hash(pattern)
    text_hashes = [hash(text[i:i+pattern_len]) for i in range(text_len - pattern_len + 1)]
    
    positions = []
    for i in range(text_len - pattern_len + 1):
        if (pattern_hash == text_hashes[i] and pattern == text[i:i + pattern_len]):
            positions.append(i)

    return positions

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

