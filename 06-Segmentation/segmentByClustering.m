function segmentation = segmentByClustering( rgbImage, featureSpace, clusteringMethod, numberOfClusters )

rgbImage1 = double(rgbImage);
s = size(rgbImage1);

if (strcmp(featureSpace,'rgb')==1)
    mx = max(max(max(rgbImage1)));
    im = rgbImage1./mx;
    
elseif (strcmp(featureSpace,'hsv')==1)
    im = rgb2hsv(rgbImage1);
    
elseif (strcmp(featureSpace,'lab')==1)
    im = rgb2lab(rgbImage1);
    mn = min(min(min(im)));
    mx = max(max(max(im)));
    im = (im+abs(mn))/(abs(mx)+abs(mn));
    
elseif (strcmp(featureSpace,'rgb+xy')==1)
    mx = max(max(max(rgbImage1)));
    im = rgbImage1./mx;
    [x,y] = meshgrid(1:s(2),1:s(1));
    x = x./max(max(x));
    y = y./max(max(y));
    im = cat(3,im,x,y);
    
elseif (strcmp(featureSpace,'hsv+xy')==1)
    im = rgb2hsv(rgbImage1);
    [x,y] = meshgrid(1:s(2),1:s(1));
    x = x./max(max(x));
    y = y./max(max(y));
    im = cat(3,im,x,y);
    
elseif (strcmp(featureSpace,'lab+xy')==1)
    im = rgb2lab(rgbImage1);
    mn = min(min(min(im)));
    mx = max(max(max(im)));
    im = (im+abs(mn))/(abs(mx)+abs(mn));
    [x,y] = meshgrid(1:s(2),1:s(1));
    x = x./max(max(x));
    y = y./max(max(y));
    im = cat(3,im,x,y);
end

[~,~,dim] = size(im);
D = double(reshape(im,[],dim));

if (strcmpi(clusteringMethod,'kmeans')==1)
    [map, ~] = kmeans(D,numberOfClusters); 
    segmentation = reshape(map,s(1),s(2));
    
elseif (strcmpi(clusteringMethod,'gmm')==1)
    gm = fitgmdist(D,numberOfClusters,'SharedCovariance',true); 
    idx = cluster(gm,D); 
    segmentation = reshape(idx,s(1),s(2));

elseif (strcmpi(clusteringMethod,'watershed')==1)
    ws = watershed(im);
    ws = uint8(ws);
    segmentation = (rgb2gray(ws(:,:,1:3))/255);
    
elseif (strcmpi(clusteringMethod,'hierarchical')==1)
    if (strcmp(featureSpace,'rgb')==1)
        im = rgbImage;
    end
    h = numberOfClusters;
    str = strel('disk',1);
    dilate = imdilate(im,str);
    rode = imerode(im,str);
    gradient = dilate-rode;
    marker = imextendedmin(gradient, h);
    new_grad = imimposemin(gradient, marker);
    ws = watershed(new_grad);
    nws = uint8(ws);
    segmentation = (rgb2gray(nws(:,:,1:3))/255);
  
end
end

