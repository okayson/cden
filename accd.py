#!/usr/bin/python3

import sys
import subprocess

# ----------------------------------------
class Candidates():
    def query(self, directory):
        if directory == '':
            history = CDHistory()
            results = history.query()
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
                self.__directories = [directory.rstrip() for directory in fin]
        except IOError:
            pass

    def store(self):
        pass
        # with open('./.accd_history','at') as fout:
        #     for directory in self.__directories:
        #         # print(directory, file=fout)
        #         fout.write(directory+'\n')

    def __str__(self):
        return str(self.__directories)

# ----------------------------------------
class CDFollower():
    def __init__(self,depth=256):
        self.__depth = depth

    def query(self):
        directories = subprocess.getoutput("find ./ -path '*/\.*' -name .git -prune -o -type d -print 2> /dev/null")

        return directories.split('\n')

    def register(self, directory):
        pass

    def __str__(self):
        return str(self.depth)

# ----------------------------------------
def main():
    arg = ''
    if len(sys.argv) != 1:
        arg = sys.argv[1]

    candidates = Candidates()
    directories = candidates.query(arg)
    # TBD: fuzzy-find, cd, register
    for directory in directories:
        print(directory)
    # ret = subprocess.getstatusoutput(['fzf',candidate])
    # ret = subprocess.getstatusoutput('ls | fzf')
    # print(ret)

# ----------------------------------------
if __name__ == "__main__":

    main()

