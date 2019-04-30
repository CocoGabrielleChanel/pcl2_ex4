#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Programmiertechniken in der Computerlinguistik II
# Übung 4 - Aufgabe 1.1
# Chanel Caratti

from typing import BinaryIO
import json
import bz2

#use RC_2012-6.bz2 (2GB)

def mk_meme_corpus(infile_path: str, outfile_path: str, min_score: int, min_len: int, max_len: int):
    """
    to read comments without all its meta-information
    one comment per line in 3 categories
    """
    my_infile = bz2.open(infile_path, 'rt')
    my_outfile = bz2.open(outfile_path, 'wt', encoding='utf8')
    used_comments = set()                                     # set: for uniqueness (without duplicates)
    for line in my_infile:
        a_comment = json.loads(line)                            # because of the json format
        my_text = a_comment['body']                             # to get the "comment" itself
        my_score = a_comment['score']                           # to get the "score"
        my_len = len(my_text)                                   # to get length of comment
        if min_score<my_score and min_len<my_len and max_len>my_len:
            hash_comment = hash(my_text)                        # hash: to store them
            if hash_comment not in used_comments:
                used_comments.add(hash_comment)
                my_outfile.write(my_text)                       # to write the "comment" itself into the ny_outfile

mk_meme_corpus('RC_2012-06.bz2', 'mk_meme_corpus.txt.gz', 100, 1, 50)   #functioncall