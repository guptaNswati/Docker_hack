#!/usr/bin/python3
import re
from collections import OrderedDict
import codecs
from meaningful_info import meaningful_info
import os
"""
Read dockerfile created by dummper and tokenize it.
"""

def read_lines(filename="", install_dic = {}):
    local_dic = {}
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
                            sub_words = sub_words.replace("\\t", "")
                            if sub_words[0] == "-":
                                continue
                            if sub_words is not None:
                                install_dic[sub_words] = install_dic.get(sub_words, 0) + 1
                                local_dic[sub_words] = local_dic.get(sub_words, 0) + 1
                                local_dic = OrderedDict(local_dic)

        for key in local_dic:
            print(key, local_dic[key])

        return (install_dic)

if __name__ == "__main__":
    converted_files = os.listdir("./converted")
    install_dic = {}
    for converted in converted_files:
        install_dic = read_lines("./converted/" + converted, install_dic)
    meaningful_info(install_dic)
