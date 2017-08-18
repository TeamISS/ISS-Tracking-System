clear
global mu
mu = 398600;
%...Input data for Example 3.6:
ro = 10000;
vro = 3.0752;
dt = 3600;
a = -19655;
%...
%...Pass the input data to the function kepler_U, which returns x
%...(Universal Kepler�s requires the reciprocal of
% semimajor axis):
x = kepler_U(dt, ro, vro, 1/a);
%...Echo the input data and output the results to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 3.6\n')
fprintf('\n Initial radial coordinate (km) = %g',ro)
fprintf('\n Initial radial velocity (km/s) = %g',vro)
fprintf('\n Elapsed time (seconds) = %g',dt)
fprintf('\n Semimajor axis (km) = %g\n',a)
fprintf('\n Universal anomaly (km�0.5) = %g',x)
fprintf('\n-----------------------------------------------\n')
% ��