import parse

if __name__ == '__main__':
    top_dir = input("Enter path (relative or absolute) to dataset (ENTER -> test-skup): ")
    if top_dir == '':
        top_dir = 'test-skup'
    data = parse.PopulateStructures(top_dir)  # populated data how stored in data.set and data.graph
