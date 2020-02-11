class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.is_end = False
        self.children = {}
        self.parent = None

class Trie:
    # TODO implement Trie
    def __init__(self):
        self.root = TrieNode("*")

    def word_exists(self, word):
        if word == "":
            return True
        word = word.lower()
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
        if word == "":
            return
        word = word.lower()
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                adding = TrieNode(letter)
                adding.parent = current_node
                current_node.children[letter] = adding
            current_node = current_node.children[letter]
        current_node.is_end = True

    def __str__(self):
        if self.root.children:
            self.print_words(self.root)
            return ""
        else:
            return "Trie is empty"

    def print_words(self, root):
        if root:
            if root.children:
                for letter in root.children:
                    node = TrieNode(letter)
                    node.parent = root
                    if root.children[letter].is_end:
                        temp = ""
                        temp = temp + self.get_all_letters(node) + letter
                        print(temp)
                    self.print_words(root.children[letter])

    def get_all_letters(self, node):
        r = ""
        while node.parent.letter != '*':
            r = r + node.parent.letter
            node = node.parent
        ret = ""
        for l in reversed(r):
            ret = ret + l
        return ret