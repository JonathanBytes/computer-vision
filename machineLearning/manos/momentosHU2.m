
% % clear all
% % 
% % contador=1

% letra=['A'; 'B';'C';'D'; 'E';'F';'G';'H';'I';'J';'K';'L';'M';'N';...
%        'O';'P';'Q';'R';'S';'T';'U';'V';'W';'X';'Y';'Z']
% diccionario=zeros(length(letra)*5,8)
% for i=1:length(letra);
% letra(i)
%         for numero=1:5

%             imagen=strcat(letra(i),num2str(numero),'.jpg')

[file path]=uigetfile('+.jpg','leer letra')
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
                    letra=input('letra?')
                    diccionario(contador,:)=[M double(letra)]
                    contador=contador+1
%         end
% end
