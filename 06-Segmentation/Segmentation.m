clc; clear
Dir = 'BSDS_tiny\Images';
Dir1 = 'resultados';
addpath(Dir) %Ruta del directorio
Images = dir(Dir); %Se genera una estructura con las imagnes
Images = Images(3:end); %Ajusta la estructura
L=length(Images); % Se establece el numero de imagenes
featureSpace = {'rgb', 'lab', 'hsv', 'rgb+xy', 'lab+xy', 'hsv+xy'};
clusteringMethod = {'kmeans', 'gmm', 'watershed','hierarchical'};
numberOfClusters = [3 5 8];

%%
for i = 1:L
    a = Images(i).name;
    b = imread(a);
    for l = 1:length(numberOfClusters)
        results = [];
        for j = 1:length(clusteringMethod)
            for k = 1:length(featureSpace)
            segmentation = segmentByClustering( b, featureSpace(k), clusteringMethod(j), numberOfClusters(l));
            results = [results, segmentation];
            k
            end
            j
        end
        l
        save(strcat('resultados/','cluster',num2str(numberOfClusters(l)),'/',strrep(a,'.jpg','.mat')), 'results')
    end
    i
end