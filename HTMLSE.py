from parse import Parser

if __name__ == '__main__':
    parser = Parser()
    a, b = parser.parse('test-skup/python-2.7.7-docs-html/index.html')
    print('as')
    print(a)
    print('d')
    print(b)
    print('sa')
