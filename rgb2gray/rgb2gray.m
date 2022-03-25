function gray=my_rgb2gray(RGB)
    [r,g,b]=my_imsplit(RGB);
    gray=uint8(r*0.299+g*0.587+b*0.114);
end
