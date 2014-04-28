function [] = walshaffinity( n )

hadamardMatrix = hadamard(n);
randamard = [];
for i = 1:n
    exp = randi(n);
    randamard(i, :) = hadamardMatrix(i, :) * (-1)^exp;
end
range = 0:pi/50:2*pi;
innerproducts = zeros(20, 20);
firsthalfproducts = zeros(20, 20);
secondhalfproducts = zeros(20, 20);
q1 = zeros(20, 20)
q2 = zeros(20, 20)
q3 = zeros(20, 20)
q4 = zeros(20, 20)
for i = 1:n
    f = @(x) 0;
    for k = 1:n
    f = @(x) f(x) + randamard(i, k)*cos(k*x);
    end
    for j = 1:n
        g = @(x) 0;
        for k = 1:n
        g = @(x) g(x) + randamard(j, k)*cos(k*x);
        end
% for k = 1:length(range)
%     innerproducts(i, j) = innerproducts(i, j) + f(range(k))*g(range(k))*0.0622;
% end

% for k = 1:50
%     firsthalfproducts(i, j) = firsthalfproducts(i, j) + f(range(k))*g(range(k))*0.0622;
% end

% for k = 51:101
%     secondhalfproducts(i, j) = secondhalfproducts(i, j) + f(range(k))*g(range(k))*0.0622;
% end

for k = 1:25
    q1(i, j) = q1(i, j) + f(range(k))*g(range(k))*0.0622;
    end
end
plot(innerproducts, 'o');

end

