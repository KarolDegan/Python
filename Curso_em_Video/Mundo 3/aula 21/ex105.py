def notas(*num, situação = False):
    dic = {}
    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    dic['media'] = sum(num)/len(num)
    if situação:
        if dic['media'] >=7:
            dic['situação'] = 'Boa'
        elif dic['media'] >=5:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'
    return dic


resp = notas(5.5, 2.5, 9, 8.5, situação=True)
print(resp)