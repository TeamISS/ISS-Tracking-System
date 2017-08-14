% 
% Example_3_05
% 
%
% This program uses Algorithm 3.2 and the data of
% Example 3.5 to solve Keplers equation for the hyperbola.
%
% e - eccentricity
% M - hyperbolic mean anomaly (dimensionless)
% F - hyperbolic eccentric anomaly (dimensionless)
%
% User M-function required: kepler_H
% ------------------------------------------------------------
clear
%...Input data for Example 3.5:
e = 2.7696;
M = 40.69;
%...
%...Pass the input data to the function kepler_H, which returns F:
F = kepler_H(e, M);
%...Echo the input data and output to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 3.5\n')
fprintf('\n Eccentricity = %g',e)
fprintf('\n Hyperbolic mean anomaly = %g\n',M)
fprintf('\n Hyperbolic eccentric anomaly = %g',F)
fprintf('\n-----------------------------------------------\n')
% 