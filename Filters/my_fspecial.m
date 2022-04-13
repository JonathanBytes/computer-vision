function my_fspecial(tipo,T)
    switch lower(tipo) % El lower cambia todo a minúsculas
        case 'average'
            K=ones(T)/T^2;
end