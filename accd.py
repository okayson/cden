#!/usr/bin/python3

import sys


# ----------------------------------------
class Candidates():
    def query(self, directory):
        if directory == '':
            history = CDHistory()
            results = history.query()
            test(history) # FIXME
        elif directory == '.':
            follower = CDFollower()
            results = follower.query()
        else:
            results = [directory]

        return results

# ----------------------------------------
class CDHistory():
    def __init__(self):
        self.__directories= list()

    def query(self):
        self.load()
        return self.__directories

    def register(self, directory):
        self.__directories.append(directory)

    def load(self):
        try:
            with open('./.accd_history','rt') as fin:
                # FIXME: 改行がうざい
                self.__directories = [directory[:-1] for directory in fin.readline()]
                # self.__directories = [directory[] for directory in fin.readline()]
        except IOError:
            pass

    def store(self):
        with open('./.accd_history','at') as fout:
            for directory in self.__directories:
                # print(directory, file=fout)
                fout.write(directory+'\n')

    def __str__(self):
        return str(self.__directories)

# ----------------------------------------
class CDFollower():
    def __init__(self,depth=256):
        self.__depth = depth

    def query(self):
        return []

    def register(self, directory):
        pass

    def __str__(self):
        return str(self.depth)

# ----------------------------------------
def main():
    directory = ''
    if len(sys.argv) != 1:
        directory = sys.argv[1]

    candidates = Candidates()
    candidate = candidates.query(directory)
    # TBD: fuzzy-find, cd, register
    print(candidate)

def test(history):
    history.register('/root/hoge')
    history.register('/root/sample/hoge')
    history.store()
    # for h in history.query():
    #     print(h)
    
    
if __name__ == "__main__":

    main()

