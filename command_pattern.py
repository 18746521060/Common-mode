#!/usr/bin/python3

# 重命名文件，创建文件，读取文件及撤销等。

import os

verbose = True


def del_file(path):
    assert os.path.isfile(path), "path must be a real file"
    if verbose:
        print("Delete the file {}".format(path))
    os.remove(path)


class RenameFile:
    def rename(self, oldname, newname):
        assert os.path.isfile(oldname), "the oldname musts existe"
        self.oldname = oldname
        self.newname = newname
        if verbose:
            print("the {} file rename {}".format(oldname, newname))
        os.rename(oldname, newname)

    def undo(self):
        assert os.path.isfile(self.newname), "the newname musts existe"
        if verbose:
            print("the {} file unrename {}".format(self.newname, self.oldname))
        os.rename(self.newname, self.oldname)


class CreateFile:
    def create_file(self, path):
        assert not os.path.exists(path), "the file is existe"
        self.path = path
        if verbose:
            print("Create the file {}".format(path))
        with open(path, "w") as f:
            f.write("")

    def undo(self):
        del_file(self.path)


class ReadFile:
    def read_file(self, file=None):
        assert file or self.file, "the file must existe"
        read_file = file if file else self.file
        with open(read_file, "r") as f:
            print(f.read())

    def write_file(self, file, data):
        assert os.path.isfile(file), "the file {} must existe".format(file)
        assert data, "data is not None"
        self.file = file
        if verbose:
            print("Writing {} to {}".format(data, self.file))
        if isinstance(data, bytes):
            with open(self.file, "wb") as f:
                f.write(data)
        if isinstance(data, str):
            with open(self.file, "w") as f:
                f.write(data)


def main():
    oldname = "old.txt"
    newname = "new.txt"

    rename = RenameFile()

    create_file = CreateFile()

    read_file = ReadFile()

    create_file.create_file(oldname)

    rename.rename(oldname, newname)

    read_file.write_file(newname, "hello world")

    read_file.read_file()
    
    rename.undo()
    create_file.undo()

if __name__ == "__main__":
    main()
