#Enter you text in english and see result

ABC = {'a' : '·-',
                   'b' : '-···',
                   'c' : '-·-·',
                   'd' : '-··',
                   'e' : '·',
                   'f' : '··-·',
                   'g' : '--·',
                   'h' : '····',
                   'i' : '··',
                   'j' : '·---',
                   'k' : '-·-',
                   'l' : '·-··',
                   'm' : '--',
                   'n' : '-·',
                   'o' : '---',
                   'p' : '·--·',
                   'q' : '--·-',
                   'r' : '·-·',
                   's' : '···',
                   't' : '-',
                   'u' : '··-',
                   'v' : '···-',
                   'w' : '·--',
                   'x' : '-··-',
                   'y' : '-·--',
                   'z' : '--··',}


other = { '1' : '·----',
                '2' : '··---',
                '3' : '···--',
                '4' : '····-',
                '5' : '·····',
                '6' : '-····',
                '7' : '--···',
                '8' : '---··',
                '9' : '----·',
                '0' : '-----',
                '.' : '······',
                ',' : '·-·-·-',
                ':' : '---···',
                ';' : '-·-·-·',
                '(' : '-·--·-',
                "'" : '·----·',
                '"' : '·-··-·',
                '-' : '-····-',
                '/' : '-··-·',
                '_' : '··--·-',
                '?' : '··--··',
                '!' : '--··--',
                '+' : '·-·-·',
                'SOS' : '···---···',
                '@' : '·--·-·',
                }



y=("Morze code>>> ");

text = input("Enter your text>>> ").lower()

text = list(text)
morze = ''
for keys in text:
    if keys in ABC:
        morze = morze + ABC.get(keys) + " "
    elif keys in other:
        morze = morze + other.get(keys) + " "


print(y + morze)
