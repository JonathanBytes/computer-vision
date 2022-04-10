r = normrnd(50,10,[1,500]);
hist(d)
hist(d,50)

[filas, cols] = size(I);

noise = normrnd(0,20,[filas,cols]); % 0 = media ; 20 = desviación estandar
Ir = uint8(double(r) + noise);

figure()
histogram(noise(:),50)

figure()
plor(r(1000,:))
hold on
