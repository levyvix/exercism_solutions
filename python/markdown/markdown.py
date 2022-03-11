import re


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = f'<h6>{i[7:]}</h6>'
        elif re.match('##### (.*)', i) is not None:
            i = f'<h5>{i[6:]}</h5>'
        elif re.match('#### (.*)', i) is not None:
            i = f'<h4>{i[5:]}</h4>'
        elif re.match('### (.*)', i) is not None:
            i = f'<h3>{i[4:]}</h3>'
        elif re.match('## (.*)', i) is not None:
            i = f'<h2>{i[3:]}</h2>'
        elif re.match('# (.*)', i) is not None:
            i = f'<h1>{i[2:]}</h1>'
        m = re.match(r'\* (.*)', i)
        if m:
            is_italic = False
            curr = m.group(1)
            is_bold = False
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            if not in_list:
                in_list = True
                if m1:
                    curr = ((f'{m1.group(1)}<strong>' + m1.group(2)) + '</strong>') + m1.group(3)
                    is_bold = True
                if m1 := re.match('(.*)_(.*)_(.*)', curr):
                    curr = (f'{m1.group(1)}<em>{m1.group(2)}' + '</em>') + m1.group(3)
                    is_italic = True
                i = f'<ul><li>{curr}</li>'
            else:
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = ((f'{m1.group(1)}<strong>' + m1.group(2)) + '</strong>') + m1.group(3)
                if is_italic:
                    curr = (f'{m1.group(1)}<em>{m1.group(2)}' + '</em>') + m1.group(3)
                i = f'<li>{curr}</li>'
        elif in_list:
            in_list_append = True
            in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = f'<p>{i}</p>'
        if m := re.match('(.*)__(.*)__(.*)', i):
            i = f'{m.group(1)}<strong>{m.group(2)}</strong>{m.group(3)}'
        if m := re.match('(.*)_(.*)_(.*)', i):
            i = f'{m.group(1)}<em>{m.group(2)}</em>{m.group(3)}'
        if in_list_append:
            i = f'</ul>{i}'
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
