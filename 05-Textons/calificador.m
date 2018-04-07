clear all
clc
label = [];
load('otros/KNC.mat')
load('otros/RFC.mat')
for n = 1:25
    a = ones(1,10);
    b = a*n-1;
    label = [label b];
end
confus = confusionmat(r,label);
confus1 = confusionmat(s,label);
figure
imagesc(confus)
title(sprintf('Confusion matrix (%.2f %% accuracy)',100 * mean(diag(confus)/10) ))
figure
imagesc(confus1)
title(sprintf('Confusion matrix (%.2f %% accuracy)',100 * mean(diag(confus1)/10) ))

