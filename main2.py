import string
from collections import Counter
from itertools import count
import pandas as pd
from openpyxl.workbook import Workbook

seo_list = ['seo1.txt', 'seo3.txt']
num = 0


def fun_counter(x):
    cnt = Counter(x)
    return dict(cnt)


with open("seo1.txt", "r") as file1:
    content = file1.read()
    punctuat = str.maketrans(dict.fromkeys(string.punctuation))
    content = content.translate(punctuat)
    list_content1 = content.split()
    list_content1 = [name.lower() for name in list_content1]

    # print(list_content1)
    count_print1 = fun_counter(list_content1)
    # print(f"Текст в seo1 :{count_print}")

with open("seo2.txt", "r") as file2:
    content = file2.read()
    punctuat = str.maketrans(dict.fromkeys(string.punctuation))
    content = content.translate(punctuat)
    list_content2 = content.split()
    list_content2 = [name.lower() for name in list_content2]

    # print(list_content2)
    count_print2 = fun_counter(list_content2)
    # print(f"Текст в seo2 :{count_print}")

with open("seo3.txt", "r") as file3:
    content = file3.read()
    punctuat = str.maketrans(dict.fromkeys(string.punctuation))
    content = content.translate(punctuat)
    list_content3 = content.split()
    list_content3 = [name.lower() for name in list_content3]
    count_print3 = fun_counter(list_content3)

# Ans = ['1', '2', '3', '4']
# Word = ['2', '4']
# result = list(set(Ans) & set(Word))
# print(result)
# result = list(set(Ans + Word))
# print(result)
#
# result = list(set(Ans) ^ set(Word))
# print(result)
#
# result = list(set(Ans) - set(Word))
# print(result)


result12 = list(set(list_content1) & set(list_content2))
result123 = list(set(result12) & set(list_content3))
# print(f"Пересечение списка 1-2: {result}")
# result = list(set(list_content2) & set(list_content3))
# print(f"Пересечение списка 2-3 : {result}")
# result1 = list(set(list_content1) & set(list_content2) & set(list_content3))
print(f"Пересечение списка 1-2: {result12}")
print(f"Пересечение списка 1-2-3: {result123}")

result2 = list(set(list_content1) - set(list_content2))
# result2 = list(set(list_content1 + list_content2 + list_content3))
print(f"Разница списков: {result2}")

print(count_print1)

a = {
    'Seo1': list_content1,
    'Seo2': list_content2,
    # 'Seo3': list_content3,
    'Разница слов1-2': result12,
    'Разница слов1-2-3': result123,
    'Пересечение слов': result2,

}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
# df.to_excel('teamsFinal.xlsx')

#
# def print_hi(name):
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# if __name__ == '__main__':
#     print_hi('')
