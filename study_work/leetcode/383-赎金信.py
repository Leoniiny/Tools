# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
from collections import Counter

string1 = "qqqaaaa"
string2 = "qqqaaaaweqweqw"
dic1 = Counter(string1)
dic2 = Counter(string2)

print(dic1-dic2 == Counter())
print(Counter())