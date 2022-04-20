def imagebinarize(image,method=='otsu',sensitivity=='0.9'):
    if method == 'otsu':
        T=graythresh(image)
    if method == 'bradley':
        T=bradly(image,sensitivity)
    return T
