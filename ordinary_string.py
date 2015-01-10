def ordinary_number(first,last):
    product = list()
    while first <= last:
        if first in [11,12,13]:
            product.append(str(first)+'th')
        else:
            if str(first)[-1:] == '1':
                product.append(str(first)+'st')
            elif str(first)[-1:] == '2':
                product.append(str(first)+'nd')
            elif str(first)[-1:] == '3':
                product.append(str(first)+'rd')
            else:
                product.append(str(first)+'th')
        first = first + 1
    return product
    