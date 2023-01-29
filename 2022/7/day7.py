with open("day7.txt", "r") as file:
    term_outputs = file.readlines()


class Dir:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.size = 0
        self.files = {}

    def add_child(self, child):
        self.children.append(child)

    def add_file(self, file_name, file_size):
        self.files[file_name] = file_size


start = Dir('/')
def build_filesystem(term_outputs, start):
    for output in term_outputs:
        output = output.strip('\n')
        terms = output.split(' ')
        if terms[0] == '$':
            if terms[1] == 'cd':
                if terms[2] == "/":
                    curr_dir = start
                elif terms[2] == "..":
                    curr_dir = curr_dir.parent
                else:
                    temp_dir = [
                        child for child in curr_dir.children \
                            if child.name == terms[2]
                    ][0]
                    temp_dir.parent = curr_dir
                    curr_dir = temp_dir
        elif terms[0] == 'dir':
            curr_dir.add_child(Dir(terms[1]))
        else:
            curr_dir.add_file(terms[1], terms[0])


size_sum = 0
def find_dirs_sizes(dirs, size_limit):
    global size_sum
    if dirs.children == []:
        if dirs.files == {}:
            dirs.size = 0
            return
        else:
            for value in dirs.files.values():
                dirs.size += int(value)
            if dirs.size <= size_limit:
                size_sum += dirs.size
            return
    elif dirs.files == {}:
        child_sizes = 0
        for child in dirs.children:
            find_dirs_sizes(child, size_limit)
            child_sizes += child.size
        dirs.size = child_sizes
        if child_sizes <= size_limit:
            size_sum += child_sizes
        return
    else:
        child_sizes = 0
        for child in dirs.children:
            find_dirs_sizes(child, size_limit)
            child_sizes += child.size
        file_size = 0
        for value in dirs.files.values():
            file_size += int(value)
        child_sizes += file_size
        dirs.size = child_sizes
        if child_sizes <= size_limit:
            size_sum += child_sizes
        return


build_filesystem(term_outputs, start)
find_dirs_sizes(start, 100000)
print(size_sum)
min_space = start.size - (70000000 - 30000000)
mins = 1000000000


def find_min_space_dir(dirs):
    global mins
    global min_space
    if dirs.children == []:
        if dirs.size > min_space:
            if dirs.size < mins:
                mins = dirs.size
        return
    else:
        for child in dirs.children:
            find_min_space_dir(child)
            if child.size > min_space:
                if child.size < mins:
                    mins = child.size
        return


find_min_space_dir(start)
print(mins)
