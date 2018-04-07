clear all
clc

load('imagenet/test/3.mat')

figure
imagesc(confus)
title(sprintf('Confusion matrix (%.2f %% accuracy)',100 * mean(diag(confus)/conf.numTest) ))

