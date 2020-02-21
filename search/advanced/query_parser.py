import search

from parglare import Parser, Grammar


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __str__(self):
        return str(self.value)


def parse(input_query: str):
    """
    Method uses parglare to define grammar and creates parse_tree

    :param input_query: advanced input query
    :return: None if query isn't valid with grammar or populated parse_tree
    """
    input_query = search.get_correct_query(input_query)
    grammar = r"""
    E: E '||' E  {left, 1}
     | E E {left, 1}
     | E '&&' E  {left, 2}
     | '!' EE
     | '(' E ')'
     | string;
    EE: string
     | '(' E ')';
    
    terminals
    string: /[^&!|() ]+/;
    """
    actions = {
        "E": [lambda _, n: Node('||', [n[0], n[2]]),
              lambda _, n: Node('||', [n[0], n[1]]),
              lambda _, n: Node('&&', [n[0], n[2]]),
              lambda _, n: Node('!', [n[1]]),
              lambda _, n: Node('()', [n[1]]),
              lambda _, n: Node(n[0])],
        "EE": [lambda _, n: Node(n[0]),
               lambda _, n: Node('()', [n[1]])],
        "string": lambda _, value: Node(value.lower()),
    }
    g = Grammar.from_string(grammar)
    parser = Parser(g, actions=actions)
    try:
        result = parser.parse(input_query)
    except:
        return None
    else:
        return result
