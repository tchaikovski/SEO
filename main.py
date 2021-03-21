import string
from collections import Counter
from itertools import count

import pandas
import pandas as pd


seo_list = ['seo1.txt', 'seo2.txt', 'seo3.txt']
num = 0


def fun_counter(x):
    cnt = Counter(x)
    return dict(cnt)


def func_num(st):
    with open(st, "r") as file:
        content = file.read()
        punctuat = str.maketrans(dict.fromkeys(string.punctuation))
        content = content.translate(punctuat)
        list_content = content.split()
        # print(list_content)
        count_print = fun_counter(list_content)
        # print(f"Текст в seo {num} :{count_print}")
        return count_print


def func_words(st):
    with open(st, "r") as file:
        content = file.read()
        punctuat = str.maketrans(dict.fromkeys(string.punctuation))
        content = content.translate(punctuat)
        list_content = content.split()

        return list_content


for seo_file in seo_list:
    num += 1
    # print(func_num(seo_file))


df = pandas.DataFrame(
    {
        'SEO1': [],
        'SEO2': [],
        'SEO3': [],
        'SEO4': [],
    }
)

df.to_excel('teams1.xlsx')
