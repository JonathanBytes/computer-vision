
clear all
load manos.mat
momentos=diccionario(:,1:7);
letras=diccionario(:,8);

ModelKNN= fitcknn(momentos,letras,'NumNeighbors',3, 'Distance', 'euclidean')

[file path]=uigetfile('.jpg','leer letra')
imagen=strcat(path,file)

                    I=imread(imagen);
                    [bin segmentada]=mascaramano(I);
                    figure(1)
                    subplot(1,3,1)
                    imshow(I)
                    subplot(1,3,2)
                    imshow(bin)
                    subplot(1,3,3)
                    imshow(segmentada)
        
                    M=invmoments(bin)
                 
                  prediction_KNN=char(predict(ModelKNN,M))

