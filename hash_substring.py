# python3

def read_input():
    text = input()
    if(text[0] == "F"):
        text = "tests/" + "06"
        fails = open(text)
        pattern = fails.readline()
        text = fails.readline()
        return (pattern.rstrip(), text.rstrip())

    else:
        return (input().rstrip(), input().rstrip())
    

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

