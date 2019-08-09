# 1.2 Given two strings, write a method to decide if one is a permutation of the other.
def is_a_permutation(s1, s2):
    word_counts1 = dict()
    word_counts2 = dict()
    for c in s1:
        word_counts1[c] = word_counts1.get(c, 0) + 1
        
    for c in s2:
        word_counts2[c] = word_counts2.get(c, 0) + 1

    return word_counts1 == word_counts2
    
        
# list() => O(n)
# sorted() => O(n * log(n))

# Runtime of is_a_permutation => O(len(s1) * log(len(s1)) + len(s2) * log(len(s2)))
# Runtime of is_a_permutation => O(len(s1) + len(s2))

# Tests
def test_func(s1, s2):
    print(f"{s1} {s2} {is_a_permutation(s1, s2)}")  

test_func("cat", "tac")
test_func("below", "elbow")
test_func("stressed", "desserts")
test_func("word", "wrong")