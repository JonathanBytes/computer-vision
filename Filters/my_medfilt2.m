function T=my_medfilt2(Gris,V)

n=V(1);
m=V(2);


iniF=(n+1)/2;
iniC=(m+1)/2;
finF=iniF-1;
finC=iniC-1;
Ipad=padarray(Gris,[finF finC],'replicate');
[F C]=size(Ipad);
T=zeros(F,C);
for i=iniF:F-finF
    for j=iniC:C-finC
        V=Ipad(i-finF:i+finF,j-finC:j+finC);
        Orden=sort(V(:));
        T(i,j)=Orden((n*m+1)/2);    
    end
end
T=uint8(T);
T=T(iniF:F-finF,iniC:C-finC);
end