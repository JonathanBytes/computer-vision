def imagebinarize(image,metod=='otsu',sensitivity=='0.9'):
    if metod == 'otsu':
        T=otsu(image)
    if metod == 'bradley':
        T=bradly(image,sensitivity)
    return T
