def write_to_txt(path, txt):
    with open(path, 'a') as file:
        file.write(txt + "\n")
