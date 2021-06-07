import textwrap

width = int(input('Enter the width : '))

with open('file.txt', 'r') as file:
    data = file.read().replace('\n', '')

wrapper = textwrap.TextWrapper(width)
word_list = wrapper.wrap(data)


for item in word_list:
    print(item)