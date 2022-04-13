function T=my_modfilt(Gris,W)

n=W(1);
m=W(2);


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
        Moda=mode(V(:));
        T(i,j)=Moda;
    end
end
T=uint8(T);
T=T(iniF:F-finF,iniC:C-finC);
end
