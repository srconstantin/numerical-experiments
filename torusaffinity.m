function [ affinity ] = torusaffinity(m1, m2, n1, n2 )
N = 10;
affinity = 0;
%N is the number of scales;
if m1 ~= n1 && m2 ~- n2
    for k = 1:N
        for l = 1:2^k
            for p = 1:2^k
                affinity = affinity + abs(1/(4^k) * 1/(m1-n1)* (sin(2*(m1-n1)*l * pi/2^k) - sin(2*(m1-n1)*(l-1)*pi/2^k))* 1/(m2-n2)* (sin(2*(m2-n2)*p * pi/2^k) - sin(2*(m2-n2)*(p-1) * pi/2^k)));
        end
        end
    end
    
affinity = affinity / (pi^2/3 * (1-0.25^N));
elseif m1 ~= n1 && m2 == n2
    for k = 1:N
        for l = 1:2^k
            affinity = affinity + abs(1/(4^k) * 1/2^k * 1/(m1-n1) * (sin(2*(m1-n1)*l * pi/2^k) - sin(2*(m1-n1)*(l-1)*pi/2^k)));
        end
    end

elseif m1 == n1 && m2 ~= n2
    for k = 1:N
        for p = 1:2^k
            affinity = affinity + abs(1/(4^k)* 1/2^k * 1/(m2-n2) * (sin(2*(m2-n2)*p * pi/2^k) - sin(2*(m2-n2)*(p-1) * pi/2^k)));
        end
    end
  

else
    affinity = 1;
end


end

