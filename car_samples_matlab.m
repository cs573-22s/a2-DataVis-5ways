close all;
clear all;

T = readtable('cars-sample.csv');

plot = gscatter(T.Weight,T.MPG,T.Manufacturer);
hold on
plot2 = scatter(T.Weight,T.MPG,T.Weight/25, "white", "filled");
plot2.MarkerFaceAlpha = 0.5;
plot2.MarkerEdgeColor = 'k';