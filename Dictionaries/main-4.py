'''CS2420 Project 7. Luis Gago. I certify that I wrote all of the following code myself.'''

from hashmap import HashMap

def clean_line(raw_line):
    '''removes all punctuation from input string and returns a
    list of all words which have a length greater than one'''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)): # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():
    '''main driver to read AliceInWonderland and insert all words into HashMap'''
    hm = HashMap()
    with open("AliceInWonderland.txt") as input_file:
        for line in input_file:
            words = clean_line(line)
            for word in words:
                # print(word, type(word)) #Strings are being returned here.
                hm.set(word, (hm.get(word, 0) + 1))
    print("The most common words are:")

    new_list = []
    for items in hm.buckets:
        if items is not None:
            new_list.append(items)
    new_list.sort(key = lambda x: x[1], reverse =True)
    for items in new_list[:15]:
        print(items[0], items[1])

if __name__ == "__main__":
    main()
