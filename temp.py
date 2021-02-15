CHARS = """۹۳۲۱۸۰۴۵۷ٖ٦)ٍٰﷺا⸮-ٴ/۔ہ>(<ً:ً"ّ؛]%[}!{،آڙؤۓءۀڈرةذوےزئڑدںبتسعغنیموھفشقصخلآطگکضجظحثٹپچ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ…#"+"""

CHAR2LABEL = {char: i + 1 for i, char in enumerate(CHARS)}

# print(CHAR2LABEL)

import io, os

n = set()

count = 0

for filename in os.listdir('UPTI/groundtruth'):
    if filename.endswith('.txt'):
        filename = os.path.join('UPTI/groundtruth',filename)
        with io.open(filename, 'r', encoding='utf8') as f:
            text = f.read()
            text = text.strip('\n')
            for c in text:
                if (c == ' ' or c == '\n') :
                    continue
                if c not in CHAR2LABEL:
                    count -= 1
                    break
                    # n.add(c)

print(count)
