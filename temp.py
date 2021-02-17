CHARS = """۹۳۲۱۸۰۴۵۷ٖ٦)ٍٰﷺا⸮-ٴ/۔ہ>(<ً:ً"ّ؛]%[}!{،آڙؤۓءۀڈرةذوےزئڑدںبتسعغنیموھفشقصخلآطگکضجظحثٹپچ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ…#"+"""

CHAR2LABEL = {char: i + 1 for i, char in enumerate(CHARS)}

# print(CHAR2LABEL)

import io, os

# n = set()

# files = []
count = 0

for filename in os.listdir('data/UPTI/groundtruth'):
    if filename.endswith('.txt'):
        name = filename.split('.')[0] + ".png"
        filename = os.path.join('data/UPTI/groundtruth',filename)
        with io.open(filename, 'r', encoding='utf8') as f:
            text = f.read()
            text = text.strip()
            text = text.strip('\n')
            text = text.replace(' ','')
            valid = True
            for c in text:
                if (c == '\n') :
                    continue
                if c not in CHAR2LABEL:
                    count -= 1
                    valid = False
                    break
            if valid:
                pth = os.path.join('line_undegraded',name)
                with open('data/UPTI/train.txt','a') as the_file:
                    the_file.write(pth+"\n")

print(count)

# import os, io

# paths_file = 'train.txt'
# root_dir = 'data/UPTI'

# paths = []
# texts = []



#     # return paths, texts

# print(paths[10])

# print(texts[10])