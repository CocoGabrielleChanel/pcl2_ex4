#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Programmiertechniken in der Computerlinguistik II
# Übung 4 - Aufgabe 2
# Chanel Caratti


def longest_substrings(x: str, y: str):
    """
    creates table (m x n)
    fills with "1" if same character and if same letter adds 1 into the diagonal
    """
    x = x.lower()
    y = y.lower()
    m = len(x)
    n = len(y)
    d = [[0 for Z in range(n)] for Z in range(m)]
    for i in range(0, m):
        if x[i] == y[0]:
            d[i][0] = 1                                  
    for j in range(0, n):
        if x[0] == y[j]:
            d[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                d[i][j] = d[i-1][j-1] + 1                
    for i in range(0, m):
        s = ''
        for j in range(0, n):
            s += str(d[i][j])
            s += " "
        print(s + '\n')
    mmax_with_index = get_max(m, n, d)             
    mmax = mmax_with_index[0]
    mmax_i = mmax_with_index[1]
    my_char = get_char(mmax, mmax_i, x)
    print(mmax)
    print(my_char)

def get_max(m, n, d):
    """
    gets max: longest substring
    """       
    mmax = 0
    mmax_i = -1
    for i in range(0, m):               
        for j in range(0, n):
            if d[i][j] > mmax:
                mmax = d[i][j]
                mmax_i = i
    return[mmax, mmax_i]

def get_char(mmax, mmax_i, x):
    """
    to get the longest substring characters
    """
    my_start = mmax_i + 1 - mmax
    my_end = my_start + mmax
    my_char = x[my_start:my_end]
    return my_char

longest_substrings('Meisterklasse', 'Kleistermasse')     # function call