import re
import utils
text = utils.read_file("raw.txt")
#task1
# pattern = 'аб*'
# print(re.findall(pattern, text))
#task2
# pattern = 'аб{2,3}'
# print(re.findall(pattern,text))
#task3
# pattern = '[а-я]+_[а-я]*'
# print(re.findall(pattern, text))
#task4
# pattern = '[А-Я]+[а-я]*'
# print(re.findall(pattern,text))
#task5
# pattern = r'а.*б'
# print(re.findall(pattern,text))
#task6
# print(re.sub("[ ,.]", ':',text))
# #task7
# pattern = r'[А-Я][^А-Я]*' # ^ Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
# print(re.findall(pattern, text))
#task8
# pattern = r'[А-Я][а-я]*'
# willchange = re.findall(pattern,text)
# print(' '.join(willchange))
#task9
# def snake_to_camel(str):
#     return re.sub(r'(?!^)_([a-zA-z])', lambda m: m.group(1).upper(), str)
#
# snake_str = 'hello_iam_Arnur'
# camel_str = snake_to_camel(snake_str)
# print("tomakesure")
# print(camel_str)
#task10
def camel_to_snake(str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', str).lower()
camel_str = "HeyArnurIsThisYou"
snake_str = camel_to_snake(camel_str)
print("iwantcheck")
print(snake_str)
