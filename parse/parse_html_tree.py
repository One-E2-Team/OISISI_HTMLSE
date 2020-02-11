import os
from parse.parser import Parser
import structures


def get_html_documents_list(top):
    """
    Returns paths of all html documents in specified directory's tree
    :param top: top directory path
    :return: list of paths of all html files in tree of top directory
    """

    ret = []
    for root, dirs, files in os.walk(top):
        for file in files:
            if '.htm' in file:  # takes .htm as well as .html documents
                ret.append(os.path.join(root, file))
    return ret


class PopulateStructures:
    """
    Populate word trie tree and links graph from all HTML documents in a folder (complete directory tree).
    graph and trie are attributes of this class (instances of data structures implemented in structures package)
    """

    def __init__(self, top):
        self.graph = structures.Graph(directed=True)
        self.trie = structures.Trie()
        parser = Parser()
        # document = open('data.txt', mode='w', encoding='utf-8')
        for html_file in get_html_documents_list(top):
            links, words = parser.parse(html_file)
            # TODO populate graph and trie
            # document.write(str(links) + ' ' + str(words) + '\n')
        pass