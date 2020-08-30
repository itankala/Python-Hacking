def get_path_to_file(file):
    split_file = file.split("/")
    split_file_length = len(split_file) - 1

    path = ""
    for i in range(0, split_file_length):
        path = path + split_file[i] + "/"
    return path


def get_filename(file):
    split_file = file.split("/")
    place = len(split_file) - 1
    return split_file[place]