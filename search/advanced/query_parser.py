import search

from parglare import Parser, Grammar


def parse(input_query: str):
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
    string: /[^&!|()]+/;
    """
    actions = {
        "E": [lambda _, n: n[0] + '||' + n[2],
              lambda _, n: n[0] + '||' + n[1],
              lambda _, n: n[0] + '&&' + n[2],
              lambda _, n: '!' + n[1],
              lambda _, n: '(' + n[1] + ')',
              lambda _, n: n[0]],
        "EE": [lambda _, n: n[0],
               lambda _, n: '(' + n[1] + ')'],
        "string": lambda _, value: str(value).lower(),
    }
    g = Grammar.from_string(grammar)
    parser = Parser(g, actions=actions)
    try:
        result = parser.parse(input_query)
    except:
        return None
    else:
        print("Result = ", result)
        return result
