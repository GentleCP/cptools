#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
-----------------File Info-----------------------
            Name: function.py
            Description: save code that frequently used
            Author: GentleCP
            Email: 574881148@qq.com
            WebSite: https://www.gentlecp.com
            Create Date: 3/24/2021 
-----------------End-----------------------------
"""
from math import ceil

def is_unique(seq):
    '''
    judge whether a giving sequence has repeating elements or not
    Args:
        seq: sequence like list, tuple and so on.

    Returns: True if unique and False if not unique

    '''
    return len(seq) == len(set(seq))

def chunk_list(lst: list, size: int):
    '''
    split a list into num chunks by specifying the chunk size
    e.g. [1,2,3,4,5] -> [[1,2], [3,4], [5]]
    Args:
        lst: [1,2,3,4,5]
        size: 3

    Returns: chunk_list, e.g. [[1,2], [3,4], [5]]

    '''
    return map(lambda x: lst[x * size: x * size + size], list(range(0, ceil(len(lst) / size))))


def flatten_seq(seq):
    '''
    flatten a deep sequence into a single one
    e.g. [[1,2],[[3,4]],5] -> [1,2,3,4,5]
    Args:
        seq: sequence, could be list or tuple...
    Returns:

    '''
    for item in seq:
        try:
            for subitem in flatten_seq(item):
                yield subitem
        except TypeError:
            yield item


