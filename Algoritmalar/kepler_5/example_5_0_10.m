clear
global f Re wE mu
deg = pi/180;
f = 1/298.256421867;
Re = 6378.13655;
wE = 7.292115e-5;
mu = 398600.4418;
%...Input data for Example 5.10:
rho = 2551;
rhodot = 0;
A = 90;
Adot = 0.1130;
a = 30;
adot = 0.05651;
theta = 300;
phi = 60;
H = 0;
%...
%...Algorithm 5.4:
[r,v] = rv_from_observe(rho, rhodot, A, Adot, a, adot, theta, ...
phi, H);
coe = coe_from_sv(r,v);
h = coe(1);
e = coe(2);
RA = coe(3);
incl = coe(4);
w = coe(5);
TA = coe(6);
a = coe(7);
%...Equation 2.40
rp = hˆ2/mu/(1 + e);
%...Echo the input data and output the solution to
% the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 5.10')
fprintf('\n\n Input data:\n')
fprintf('\n Slant range (km) = %g', rho)
fprintf('\n Slant range rate (km/s) = %g', rhodot)
fprintf('\n Azimuth (deg) = %g', A)
fprintf('\n Azimuth rate (deg/s) = %g', Adot)
fprintf('\n Elevation (deg) = %g', a)
fprintf('\n Elevation rate (deg/s) = %g', adot)
fprintf('\n Local sidereal time (deg) = %g', theta)
fprintf('\n Latitude (deg) = %g', phi)
fprintf('\n Altitude above sea level (km) = %g', H)
fprintf('\n\n')
fprintf(' Solution:')
fprintf('\n\n State vector:\n')
fprintf('\n r (km) = [%g, %g, %g]', ...
r(1), r(2), r(3))
fprintf('\n v (km/s) = [%g, %g, %g]', ...
v(1), v(2), v(3))
fprintf('\n\n Orbital elements:\n')
fprintf('\n Angular momentum (kmˆ2/s) = %g', h)
fprintf('\n Eccentricity = %g', e)
fprintf('\n Inclination (deg) = %g', incl/deg)
fprintf('\n RA of ascending node (deg) = %g', RA/deg)
fprintf('\n Argument of perigee (deg) = %g', w/deg)
fprintf('\n True anomaly (deg) = %g\n', TA/deg)
fprintf('\n Semimajor axis (km) = %g', a)
fprintf('\n Perigee radius (km) = %g', rp)
%...If the orbit is an ellipse, output its period:
if e < 1
T = 2*pi/sqrt(mu)*aˆ1.5;
fprintf('\n Period:')
fprintf('\n Seconds = %g', T)
fprintf('\n Minutes = %g', T/60)
fprintf('\n Hours = %g', T/3600)
fprintf('\n Days = %g', T/24/3600)
end
fprintf('\n-----------------------------------------------\n')
% ˜˜˜˜˜˜˜