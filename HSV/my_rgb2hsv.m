function [ H,S,V ] = my_rgb2hsv( I )

r=double(I(:,:,1))/255;
g=double(I(:,:,2))/255;
b=double(I(:,:,3))/255;

[N M L]=size(I);
Cmax=zeros(N,M);
d=zeros(N,M);
H=zeros(N,M);
S=zeros(N,M);
V=zeros(N,M);
for i=1:N
   for j=1:M
       maximo=max(max(r(i,j),g(i,j)),b(i,j));
       minimo=min(min(r(i,j),g(i,j)),b(i,j));
       Cmax(i,j)=maximo;
       Cmin(i,j)=minimo;
       d(i,j)=maximo-minimo;
 
%para H-----------
       if d(i,j)==0 
           H(i,j)=0;
       end
       
       switch maximo
           case r(i,j)
               H(i,j)=60*mod((g(i,j)-b(i,j))/d(i,j),6);
               
           case g(i,j)
               H(i,j)=60*((g(i,j)-b(i,j))/d(i,j)+2);
                    
           case b(i,j)
               H(i,j)=60*((g(i,j)-b(i,j))/d(i,j)+4);
       end
       
  %Fin H-----------------
       
       
  %Para S----------------     
       if maximo==0
           S(i,j)=0;
       else
           S(i,j)=d(i,j)/maximo;
       end
           
  %Fin S---------------    
  
  %Para V--------------
  V(i,j)=maximo;
  
  %fin V---------------
   end
    
end
H=H/360;

end

