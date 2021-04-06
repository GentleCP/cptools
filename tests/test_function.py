#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-----------------File Info-----------------------
            Name: test_function.py
            Description:
            Author: GentleCP
            Email: 574881148@qq.com
            WebSite: https://www.gentlecp.com
            Create Date: 2021/4/6 
-----------------End-----------------------------
"""
import pytest
from cptools import function

def test_is_unique():
    assert function.is_unique([1,2,3]) == True
    assert function.is_unique([1,2,2]) == False

def test_chunk_list():
    assert list(function.chunk_list([1,2,3,4,5], 2)) == [[1,2], [3,4], [5]]

def test_flatten_seq():
    assert list(function.flatten_seq([[1,2],[[3,4]],5])) == [1,2,3,4,5]

if __name__ == '__main__':
    pytest.main()