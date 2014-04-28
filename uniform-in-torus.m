function [x, y, z] = uniform_in_torus(n, r1, r2)
angles = 2 * pi * rand(n, 2);
x = (r1 + r2 * cos(angles(:, 2))).* cos(angles(:, 1));
y = (r1 + r2 * cos(angles(:, 2))).* sin(angles(:, 1));
z = r2 * sin(angles(:, 2));
scatter3(x, y, z);
