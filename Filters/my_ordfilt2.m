function T=my_ordfilt2(Gris,Termino,K)

[n,m]=size(K)

iniF=(n+1)/2;
iniC=(m+1)/2;
finF=iniF-1;
finC=iniC-1;
Ipad=padarray(Gris,[finF finC],'replicate');
[F C]=size(Ipad);
T=zeros(F,C);
for i=iniF:F-finF
    for j=iniC:C-finC
        V=double(Ipad(i-finF:i+finF,j-finC:j+finC)).*double(K);
        Orden=sort(V(:));
        T(i,j)=Orden(Termino);
    end
end
T=uint8(T);
T=T(iniF:F-finF,iniC:C-finC);
end
