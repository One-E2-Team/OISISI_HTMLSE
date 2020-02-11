class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.is_end = False
        self.children = {}

class Trie:
    # TODO implement Trie
    def __init__(self):
        self.root = TrieNode("*")

    def word_exists(self, word):
        if word == "":
            return True
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        if current_node.is_end:
            return True
        else:
            return False


    def add_node(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                adding = TrieNode(letter)
                current_node.children[letter] = adding
            current_node = current_node.children[letter]
        current_node.is_end = True

    def __str__(self):
        if self.root.children:
            return "Trie is not empty"
        else:
            return "Trie is empty"

if __name__ == "__main__":
    trie = Trie()
    trie.add_node("slovo")
    trie.add_node("slova")
    trie.add_node("word")
    trie.add_node("words")
    trie.add_node("slo")
    print(trie)
