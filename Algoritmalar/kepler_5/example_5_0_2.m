-----------------------------------------------------------
clear
global mu
deg = pi/180;
mu = 398600;
r1 = [ 5000 10000 2100];
r2 = [-14600 2500 7000];
dt = 3600;
string = 'pro';
%...
%...Algorithm 5.2:
[v1, v2] = lambert(r1, r2, dt, string);
%...Algorithm 4.1 (using r1 and v1):
coe = coe_from_sv(r1, v1);
%...Save the initial true anomaly:
TA1 = coe(6);
%...Algorithm 4.1 (using r2 and v2):
coe = coe_from_sv(r2, v2);
%...Save the final true anomaly:
TA2 = coe(6);
%...Echo the input data and output the results to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 5.2: Lambert''s Problem\n')
fprintf('\n\n Input data:\n');
fprintf('\n Gravitational parameter (km3/s2) = %g\n', mu)
fprintf('\n r1 (km) = [%g %g %g]', ...
r1(1), r1(2), r1(3))
fprintf('\n r2 (km) = [%g %g %g]', ...
r2(1), r2(2), r2(3))
fprintf('\n Elapsed time (s) = %g', dt);
fprintf('\n\n Solution:\n')
fprintf('\n v1 (km/s) = [%g %g %g]', ...
v1(1), v1(2), v1(3))
fprintf('\n v2 (km/s) = [%g %g %g]', ...
v2(1), v2(2), v2(3))
fprintf('\n\n Orbital elements:')
fprintf('\n Angular momentum (km2/s) = %g', coe(1))
fprintf('\n Eccentricity = %g', coe(2))
fprintf('\n Inclination (deg) = %g', coe(4)/deg)
fprintf('\n RA of ascending node (deg) = %g', coe(3)/deg)
fprintf('\n Argument of perigee (deg) = %g', coe(5)/deg)
fprintf('\n True anomaly initial (deg) = %g', TA1/deg)
fprintf('\n True anomaly final (deg) = %g', TA2/deg)
fprintf('\n Semimajor axis (km) = %g', coe(7))
fprintf('\n Periapse radius (km) = %g', ...
coe(1)2/mu/(1 + coe(2)))
if coe(2)<1
T = 2*pi/sqrt(mu)*coe(7)1.5;
fprintf('\n Period:')
fprintf('\n Seconds = %g', T)
fprintf('\n Minutes = %g', T/60)
fprintf('\n Hours = %g', T/3600)
fprintf('\n Days = %g', T/24/3600)
end
fprintf('\n-----------------------------------------------\n')
% 
