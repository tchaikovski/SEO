import string
from collections import Counter
import pandas as pd

seo_list = ['seo1.txt', 'seo2.txt', 'seo3.txt']
num = 0


def fun_counter(x):
    cnt = Counter(x)
    return dict(cnt)


# TODO: нужно убрать дубли кода


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
    count_print2 = fun_counter(list_content2)

with open("seo3.txt", "r") as file3:
    content = file3.read()
    punctuat = str.maketrans(dict.fromkeys(string.punctuation))
    content = content.translate(punctuat)
    list_content3 = content.split()
    list_content3 = [name.lower() for name in list_content3]
    count_print3 = fun_counter(list_content3)

result12 = list(set(list_content1) & set(list_content2))
result123 = list(set(result12) & set(list_content3))

# print(f"Пересечение списка 1-2  : {result12}")
# print(f"Пересечение списка 1-2-3: {result123}")

result2 = [x for x in list_content1 + list_content2 if x not in list_content1 or x not in list_content2]
result21 = [x for x in list_content1 + list_content2 + list_content3 if
            x not in list_content1 or x not in list_content2]

# print(f"Разница списков 1-2   : {result2}")
# print(f"Разница списков 1-2-3 : {result21}")

# print(count_print1)
# print(count_print2)
# print(count_print3)
# {'закажите': 1, 'дома': 1, 'из': 1, 'бруса': 1, 'под': 1, 'ключ': 1, 'недорого': 1, 'в': 1, 'санктпетербурге': 1, 'и': 1, 'ленинградской': 1, 'области': 1, 'строительная': 1, 'компания': 1, 'владимир': 1, 'строй': 1}

count_print10ex = []
count_print11ex = []
for key in count_print1:
    val = count_print1[key]
    y1 = [key]
    y2 = [val]
    count_print10ex += y1
    count_print11ex += y2

# print(count_print1)
print(count_print10ex)
print(count_print11ex)


count_print20ex = []
count_print21ex = []
for key in count_print2:
    val = count_print2[key]
    y1 = [key]
    y2 = [val]
    count_print20ex += y1
    count_print21ex += y2
print(count_print20ex)
print(count_print21ex)

count_print30ex = []
count_print31ex = []
for key in count_print3:
    val = count_print3[key]
    y1 = [key]
    y2 = [val]
    count_print30ex += y1
    count_print31ex += y2
print(count_print30ex)
print(count_print31ex)


a = {
    'Seo1': list_content1,
    'Seo2': list_content2,
    'Seo3': list_content3,
    'Пересечение списка 1-2': result12,
    'Пересечение списка 1-2-3': result123,
    'Разница списков 1-2': result2,
    'Разница списков 1-2-3': result21,
    "Слова конкурент 1": count_print10ex,
    "\"!1\"": count_print11ex,
    "Слова конкурент 2": count_print20ex,
    "\"!2\"": count_print21ex,
    "Слова конкурент 3": count_print30ex,
    "\"!3\"": count_print31ex,

}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
df.to_excel('teamsFinal.xlsx')

