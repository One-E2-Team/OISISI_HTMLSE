import parse


if __name__ == '__main__':
    top_dir = input("Unijeti putanju do seta podataka (ENTER -> test-skup): ")
    if top_dir == '':
        top_dir = 'test-skup'
    ret = parse.get_html_documents_list(top_dir)
    for x in ret:
        print(x)
