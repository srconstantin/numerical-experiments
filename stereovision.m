function x = stereo(im1, im2)

[length width] = size(im1);
disparity = [];
for i = 1:floor(length/40)
    sim = [];
    for j = 1:floor(width/40)
        patch = im1(i:i+40, j:j+40);
        for k = i-5:i+5
            newpatch = im2(k:k+40, j:j+40);
            sim[k] = sum(sum(patch .* newpatch))./sqrt(sum(sum(patch .* patch))) ./ sqrt(sum(sum(newpatch .* newpatch)));
        end
    disparity(i, j) = find(sim == max(sim)) - i;
    end
end
