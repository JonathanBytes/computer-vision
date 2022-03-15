function mystrechlim(I,Tol)
  if nargin==1
    Tol=0.01;
    endif
    h=imhist(I);
    hp=h/sum(h);
    for i=1:256
    ha(i)=sum(hp(1:i))
    if ha(i)<=Tol
        Em=i;
    endif
    if ha(i)<=(1-Tol)
        EM=i;
    endif
  end
  E=[Em,EM];
  end