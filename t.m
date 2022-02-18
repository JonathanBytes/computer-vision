RGB(:,:,1)=[0, 255, 255;
            255, 128, 0;
            255, 0, 0]
RGB(:,:,2)=[255, 255, 0;
                    0, 128, 255;
                        255, 0, 0]
RGB(:,:,3)=[255, 255, 0;
                        255, 128, 0;
                        0, 0, 255]

figure(1)
# imshow(RGB/255,'initialmagnification','fit')

rgb=uint8(RGB)
imshow(rgb,'initialmagnification','fit')