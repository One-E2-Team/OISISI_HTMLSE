import parse


if __name__ == '__main__':
    top_dir = input("Unijeti putanju do seta podataka (ENTER -> test-skup): ")
    if top_dir == '':
        top_dir = 'test-skup'
    data = parse.PopulateStructures(top_dir)  # populated data how stored in data.set and data.graph (TODO)

