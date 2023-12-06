from nltk.corpus import wordnet as wn
import random


def contains(s, chars):
    for c in chars:
            for c2 in s:
                if c2 == c:
                    return True
    return False
def _syllables(word):
    syllable_count = 0
    vowels = 'aeiouy'
    if word[0] in vowels:
        syllable_count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllable_count += 1
    if word.endswith('e'):
        syllable_count -= 1
    if word.endswith('le') and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1
    if syllable_count == 0:
        syllable_count += 1
    return syllable_count
def random_partition(n, num_parts):
    if n <= 0:
        return []
    if num_parts == 1:
        return [n]
    part = random.randint(1, n - num_parts + 1)
    return [part] + random_partition(n - part, num_parts - 1)

def sentence_structure_partition(scount, sentence_structure):
    if scount <= 0:
        return []
    if len(sentence_structure) == 1:
        return [scount]
    if not is_variable_word(sentence_structure[0]):
        return [_syllables(sentence_structure[0])] + sentence_structure_partition(scount - _syllables(sentence_structure[0]), sentence_structure[1:])
    else:
        part = random.randint(1, scount - len(sentence_structure) + 1)
        return [part] + sentence_structure_partition(scount - part, sentence_structure[1:])

def get_random_entry(array):
    return array[random.randint(0, len(array) - 1)]

def is_variable_word(w):
    return w == "{noun}" or w == "{verb}" or w == "{adjective}" or w == "{adverb}" or w == "{conjunction}"

def pick_random_word(type, scount):
    if type == "{noun}":
        return get_random_entry(nouns[scount])
    elif type == "{verb}":
        return get_random_entry(verbs[scount]) + "s"
    elif type == "{adjective}":
        return get_random_entry(adjectives[scount])
    elif type == "{adverb}":
        return get_random_entry(adverbs[scount])
    elif type == "{conjunction}":
        return get_random_entry(conjunctions[scount])
    else:
        return type

def make_line(scount, sentence_structure):
    line = ""
    partition = sentence_structure_partition(scount, sentence_structure)
    for i in range(0, len(sentence_structure)):
        line += pick_random_word(sentence_structure[i], partition[i]) + " "
    return line

def haiku():
    structure1 = get_random_entry(sentence_structures[random.randint(3, 5)])
    structure2 = get_random_entry(sentence_structures[random.randint(3, 7)])
    structure3 = get_random_entry(sentence_structures[random.randint(3, 5)])
    return make_line(5, structure1) + "\n" + make_line(7, structure2) + "\n" + make_line(5, structure3)


noun_list = [word for synset in wn.all_synsets(wn.NOUN) for word in synset.lemma_names()]
verb_list = [word for synset in wn.all_synsets(wn.VERB) for word in synset.lemma_names()]
adjective_list = [word for synset in wn.all_synsets(wn.ADJ) for word in synset.lemma_names()]
adverb_list = [word for synset in wn.all_synsets(wn.ADV) for word in synset.lemma_names()]

nouns = {1: [word for word in noun_list if _syllables(word) == 1 and not contains(word, ['_', '.'])],
         2: [word for word in noun_list if _syllables(word) == 2 and not contains(word, ['_', '.'])],
         3: [word for word in noun_list if _syllables(word) == 3 and not contains(word, ['_', '.'])],
         4: [word for word in noun_list if _syllables(word) == 4 and not contains(word, ['_', '.'])],
         5: [word for word in noun_list if _syllables(word) == 5 and not contains(word, ['_', '.'])],
         6: [word for word in noun_list if _syllables(word) == 6 and not contains(word, ['_', '.'])]}
verbs = {1: [word for word in verb_list if _syllables(word) == 1 and not contains(word, ['_', '.'])],
         2: [word for word in verb_list if _syllables(word) == 2 and not contains(word, ['_', '.'])],
         3: [word for word in verb_list if _syllables(word) == 3 and not contains(word, ['_', '.'])],
         4: [word for word in verb_list if _syllables(word) == 4 and not contains(word, ['_', '.'])],
         5: [word for word in verb_list if _syllables(word) == 5 and not contains(word, ['_', '.'])],
         6: [word for word in verb_list if _syllables(word) == 6 and not contains(word, ['_', '.'])]}
adjectives = {1: [word for word in adjective_list if _syllables(word) == 1 and not contains(word, ['_', '.'])],
              2: [word for word in adjective_list if _syllables(word) == 2 and not contains(word, ['_', '.'])],
              3: [word for word in adjective_list if _syllables(word) == 3 and not contains(word, ['_', '.'])],
              4: [word for word in adjective_list if _syllables(word) == 4 and not contains(word, ['_', '.'])],
              5: [word for word in adjective_list if _syllables(word) == 5 and not contains(word, ['_', '.'])],
              6: [word for word in adjective_list if _syllables(word) == 6 and not contains(word, ['_', '.'])]}
adverbs = {1: [word for word in adverb_list if _syllables(word) == 1 and not contains(word, ['_', '.'])],
          2: [word for word in adverb_list if _syllables(word) == 2 and not contains(word, ['_', '.'])],
          3: [word for word in adverb_list if _syllables(word) == 3 and not contains(word, ['_', '.'])],
          4: [word for word in adverb_list if _syllables(word) == 4 and not contains(word, ['_', '.'])],
          5: [word for word in adverb_list if _syllables(word) == 5 and not contains(word, ['_', '.'])],
          6: [word for word in adverb_list if _syllables(word) == 6 and not contains(word, ['_', '.'])]}
conjunctions = {1: ["and", "or", "but", "yet", "still", "as", "when", "where", "while", "if", "though"],
                2: ["because", "unless", "whereas", "although", "until", "before", "after"]}
sentence_structures = {3: [["{adjective}", "{noun}", "{verb}"], ["{adverb}", "it", "{verb}"]],
                       4: [["the", "{noun}", "is", "{adjective}"],["the", "{noun}", "{verb}", "{adverb}"]],
                       5: [["{conjunction}", "the", "{noun}", "{verb}", "{adverb}"]],
                       6: [["{conjunction}}", "the", "{adjective}", "{adjective}", "{noun}", "{verb}"],
                           ["{adjective}", "and", "{adjective}", "the", "{noun}", "{verb}"]],
                       7: [["{adverb}", "the", "{adjective}", "{noun}", "{verb}", "the", "{noun}"],
                           ["the", "{noun}", "{verb}", "{conjunction}", "the", "{noun}", "{verb}"]]
                       }

class Main:
    if __name__ == '__main__':
        print(haiku())
