function [p, V, D] = annuluslaplacian(n, r1, r2, seed)
%best to let n be under 3000
%r1, r2 are radius sizes.

a = [0, 0];
[p, seed] = uniform_in_annulus(a, r1, r2, n, seed);

scatter(p(1, :), p(2, :))

distances = squareform(pdist(p'));

cutoff = 0.9 * max(sort(reshape(distances, n*n, 1)));

laplacian = zeros(n, n);

for i = 1:n
    for j = 1:n
        if (distances(i, j)) > cutoff
            laplacian(i, j) = -1;
            laplacian(i, i) = laplacian(i, i)+1;
        end
    end
end

[V, D] = eigs(laplacian);
