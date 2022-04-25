function T=adaptthresh(r,V,Pb)
    padn=(V(1)-1)/2;
    padm=(V(2)-1)/2;
    padr=double(padarray(r,[padn padm],'replicate'));
    [filas,cols]=size(r);
    T=zeros(filas, cols);
    
    iniF=(V(1)+1)/2;
    iniC=(V(2)+1)/2;
    FinF=iniF-1;
    FinC=iniC-1;
    
    for i=iniF:cols-FinC
        for j =iniC:cols-FinC
            W=padr(i-FinF:i+FinF,j-FinC:j+FinC);
            T(i,j)=mean(W(:))*(1-Pb/100); % Bradley
        end
    end
    % T=T(iniF:filas-FinF,iniC:cols-FinC);
end
