def makeMask(ra,rb,ga,gb,ba,bb,img):
    r,g,b = imsplit(img)
    MaskYr = (r>=ra) & (r<=rb)
    MaskYg = (g>=ga) & (g<=gb)
    MaskYb = (b>=ba) & (b<=bb)
