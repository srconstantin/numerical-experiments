theta = 2*pi*rand(N,1);
psi = 2*pi*rand(N,1);
phi = pi*rand(N, 1);
x1 = cos(phi).*exp(i*psi);
x2 = sin(phi) .* exp(i*theta);

X = [real(x1); imag(x1); real(x2); imag(x2)];
euclideanmatrix = []
for i = 1:N
    for j = 1:N
        euclideanmatrix(i, j) = exp(-norm(X(i,:)-X(j, :))/0.2);
    end
end


[V, E] = eig(euclideanmatrix);
%top eigval 280.7719, all others exponential decay


D = diag(sum(euclideanmatrix));
L = D - euclideanmatrix;
[V, E] = eig(L);
%eigenvalues  depend on cutoff

scatter3(real(x1), imag(x1), real(x2), 20, V(:, 1));
%these are spherical harmonics

complexmatrix = [];
for i = 1:1000
    for j = 1:1000
        complexmatrix(i, j) = exp(-abs(1-x1(i)*conj(x1(j))-x2(i)*conj(x2(j)))^2/0.2);
    end
end





D = diag(sum(complexmatrix));
L = D - complexmatrix;
[W, F] = eig(L);
%same basic shape


scatter3(real(x1), imag(x1), real(x2), 20, W(:, 1));
%also spherical harmonics but not the same ones

poissonmatrix = [];
for i = 1:1000
    for j = 1:1000
        poissonmatrix(i, j) = (1-0.5^2)/(1 + 0.5^2 - 2 * 0.5* X(i, :)* X(j, :)');
    end
end

%eigenvalues: 755, 213, 194, 186, 177 then a dropoff below 100


complexpoisson = []
for i = 1:1000
    for j = 1:1000
        complexpoisson(i, j) = (1-0.5^2)^2/(abs(1- 0.5* x1(i)*conj(x1(j)) - 0.5* x2(i)*conj(x2(j)))^2);
    end
end

%eigenvalues: 649, 189, 172, 166, 157, then a dropoff below 100.
