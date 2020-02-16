class Trie:

    class TrieNode:
        def __init__(self, letter):
            self.letter = letter
            self.is_end = False
            self.children = {}
            self.parent = None
            self.docs = {}

    def __init__(self):
        self.root = Trie.TrieNode("*")

    def word_exists(self, word):
        if word == "":
            return {}
        word = word.lower()
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                return False
            current_node = current_node.children[letter]

        if current_node.is_end:
            return current_node.docs
        else:
            return False

    def add_node(self, word, path):
        if word == "":
            return
        word = word.lower()
        ret = self.word_exists(word)
        if not ret:
            flag = True
        else:
            if path not in ret.keys():
                flag = True
            else:
                flag = False
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                adding = Trie.TrieNode(letter)
                adding.parent = current_node
                current_node.children[letter] = adding
            current_node = current_node.children[letter]
        current_node.is_end = True
        if flag:
            current_node.docs[path] = 1
        else:
            current_node.docs[path] += 1

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
                    node = Trie.TrieNode(letter)
                    node.parent = root
                    if root.children[letter].is_end:
                        temp = ""
                        temp = temp + Trie.__get_all_letters(node) + letter
                        print(temp)
                    self.print_words(root.children[letter])

    @classmethod
    def __get_all_letters(cls, node: TrieNode):
        ret = ''
        while node.parent.letter != '*':
            ret = ret + node.parent.letter
            node = node.parent
        return ret[::-1]
