function [ r,g,b ] = my_hsv2rgb( hsv)

F=1;
[N M L]=size(hsv);
X=zeros(N,M);
m=zeros(N,M);
R=zeros(N,M);
G=zeros(N,M);
B=zeros(N,M);
v=hsv(:,:,3);
s=hsv(:,:,2);
h=hsv(:,:,1)*360;
for i=1:N
   for j=1:M
     C(i,j)=v(i,j)*s(i,j);
     X(i,j)=C(i,j)*(1-abs(mod(h(i,j)/60,2)-1));
     m(i,j)=v(i,j)-C(i,j);
 

       
      
          if  h(i,j)>=0 && h(i,j)<60/F
              R(i,j)=C(i,j);
              G(i,j)=X(i,j);
              B(i,j)=0; 
          elseif h(i,j)>=60/F && h(i,j)<120/F
              R(i,j)=X(i,j);
              G(i,j)=C(i,j);
              B(i,j)=0;
                    
          elseif h(i,j)>=120/F && h(i,j)<180/F
               R(i,j)=0;
              G(i,j)=C(i,j);
              B(i,j)=X(i,j);              

               
          elseif h(i,j)>=180/F && h(i,j)<240/F     
              R(i,j)=0;
              G(i,j)=X(i,j);
              B(i,j)=C(i,j);
               
                
          elseif h(i,j)>=240/F && h(i,j)<300/F
               R(i,j)=X(i,j);
              G(i,j)=0;
              B(i,j)=C(i,j);
                     
          elseif h(i,j)>=300/F && h(i,j)<360/F
               R(i,j)=C(i,j);
              G(i,j)=0;
              B(i,j)=X(i,j);
            
       end
       
  %Fin -------------------
       
       
    
  

   end
    
end

r=(R+m)*255;
g=(G+m)*255;
b=(B+m)*255;


end

