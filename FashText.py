import FashFonts

def fprint(text, font):
    result = []
    resultt = []

    if font == 'sharp':
        font = FashFonts.sharp_font
    elif font == 'stars':
        font = FashFonts.stars_font
    else:
        return print('Нет такого шрифта!')

    simvoli = list(text)
    itog = ''
    for i in simvoli:
        if i in font:
            result.append(font[i])

    for i in result:
        res = []
        res = i.split('\n')
        resultt.append(res)

    for i in range(8):
        for j in range(len(resultt)):
            itog += resultt[j][i]
        itog += '\n'

    return(print(itog))
