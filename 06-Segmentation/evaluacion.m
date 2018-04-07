clc; clear

Dir = 'resultados/cluster8/';
Dir1 = 'ground_truth/';
addpath(Dir) %Ruta del directorio
addpath(Dir1) %Ruta del directorio
results = dir(Dir); %Se genera una estructura con las imagenes
results = results(3:end); %Ajusta la estructura
L = length(results);
%


for n = 1:24
    
    names1 = [];
    indice1 = [];
    
    for i = 1:L
        a = results(i).name;
        
        gt = load(strcat(Dir1,a));
        
        names = [];
        indice = [];
        
        m = n - 1;
        
        % Load segmentation from third human
        for j = 1:5
            segm = double(gt.groundTruth{j}.Segmentation);
            [f, c] = size(segm);
            
            if f == 321
                gt1=load(strcat(Dir,a));
                segm1=double(gt1.results(:,(481*m+1):(481*n)));
                r = max(jaccard(segm,segm1));
            elseif f == 481
                gt1=load(strcat(Dir,a));
                segm1=double(gt1.results(:,(321*m+1):(321*n)));
                r = max(jaccard(segm,segm1));
            end
            % Load segmentation from third human
            % segm=gt.groundTruth{3}.Segmentation;
            names = [names str2num(strrep(a,'.mat',''))];
            indice = [indice r];
        end
        names1 = [names1; names];
        indice1 = [indice1; indice];
    end
    %
    save(strcat('names',num2str(n),'.mat'), 'names1')
    save(strcat('indices',num2str(n),'.mat'), 'indice1')
end