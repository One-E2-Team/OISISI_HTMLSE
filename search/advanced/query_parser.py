from parglare import Parser, Grammar
if __name__ == '__main__':

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
    string: /\w+/;
    """

    actions = {
        "E": [lambda _, n: n[0] + "||" + n[2],
              lambda _, n: n[0] + "||" + n[1],
              lambda _, n: n[0] + " && " + n[2],
              lambda _, n: '!' + n[1],
              lambda _, n: '(' + n[1] + ')',
              lambda _, n: n[0]],
        "EE": [lambda _, n: n[0],
               lambda _, n: "(" + n[1] + ")"],
        "string": lambda _, value: str(value).lower(),
    }

    g = Grammar.from_string(grammar)
    parser = Parser(g, debug=False, actions=actions)

    result = parser.parse("dont||LOOK|| this")

    print("Result = ", result)
