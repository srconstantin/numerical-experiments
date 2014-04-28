function [x y] = uniform_in_disc(n, radius)
rtheta = rand(n, 2);
rtheta(:, 1) = rtheta(:, 1) .* discradius;
rtheta(:, 2) = rtheta(:, 2) .* (2 * pi)
[x, y] = pol2cart(rtheta(:, 2), rtheta(:, 1));
scatter(x, y);
