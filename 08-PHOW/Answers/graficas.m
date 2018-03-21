load('baseline-result.mat')
imagesc(confus) ;
title(sprintf('Confusion matrix (%.2f %% accuracy)',100 * mean(diag(confus)/conf.numTest) )) ;
