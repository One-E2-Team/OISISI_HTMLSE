import os


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
