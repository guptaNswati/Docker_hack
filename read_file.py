#!/usr/bin/python3
import re
"""
Read dockerfile created by dummper and tokenize it.
"""

def read_lines(filename=""):
    install_dic = {}
    srch_str = "install"
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.find(srch_str) is not -1:
                line = re.split(r'apt-get install -y', line)
                line = line[1:]
                for word in line:
                    word = str(word).split('&&')
                    word = str(word[0]).split(' ')
                    if len(word) > 1:
                        for sub_words in word:
                            if sub_words is not None:
                                install_dic[sub_words] = install_dic.get(sub_words, 0) + 1

        for key in install_dic:
            print(key, install_dic[key])

if __name__ == "__main__":
    read_lines("/tmp/test")
