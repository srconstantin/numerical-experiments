%This gives affinities between functions on the circle.
function [affinity] = expaffinity(m, n)
N = 10;
affinity = 0;
%N is the number of scales;
if m ~= n
    for k = 1:N
        for l = 1:2^k
            affinity = affinity + abs(1/(2^k) * 1/(m-n)* (sin(2*(m-n)*l * pi/2^k) - sin(2*(m-n)*(l-1)*pi/2^k)));
        end
    end
affinity = affinity / (pi * (1-0.5^(N+1)));
else
    affinity = 1;
end
