
clear all

contador=1

letra=['A'; 'B';'C';'D'; 'E';'F';'G';'H';'I';'J';'K';'L';'M';'N';...
       'O';'P';'Q';'R';'S';'T';'U';'V';'W';'X';'Y';'Z']
   n=3
diccionario=zeros(length(letra)*n,8)
for i=1:length(letra);
letra(i)
        for numero=1:n
            imagen=strcat(letra(i),num2str(numero),'.jpg')
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
                    diccionario(contador,:)=[M double(letra(i))]
                    contador=contador+1
        end
end

% % 
%%save('manos.mat','diccionario')