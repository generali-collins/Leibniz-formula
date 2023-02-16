#Collins Wanga

def leibniz ( terms):
    acc = 0
    num = 4
    den = 1
    for aterm in range (terms):
        nexterm = num/den*(-1)**aterm
        acc = acc +nexterm
        den = den + 2
    return acc

leibniz = leibniz(15)
print(leibniz)


