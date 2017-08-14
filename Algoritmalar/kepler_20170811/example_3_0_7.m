clear
global mu
mu = 398600;
R0 = [ 7000 -12124 0];
V0 = [2.6679 4.6210 0];
t = 3600;
%...
%...Algorithm 3.4:
[R V] = rv_from_r0v0(R0, V0, t);
%...Echo the input data and output the results to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 3.7\n')
fprintf('\n Initial position vector (km):')
fprintf('\n r0 = (%g, %g, %g)\n', R0(1), R0(2), R0(3))
fprintf('\n Initial velocity vector (km/s):')
fprintf('\n v0 = (%g, %g, %g)', V0(1), V0(2), V0(3))
fprintf('\n\n Elapsed time = %g s\n',t)
fprintf('\n Final position vector (km):')
fprintf('\n r = (%g, %g, %g)\n', R(1), R(2), R(3))
fprintf('\n Final velocity vector (km/s):')
fprintf('\n v = (%g, %g, %g)', V(1), V(2), V(3))
fprintf('\n-----------------------------------------------\n')
% ����