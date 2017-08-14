clear
deg = pi/180;
global mu
%...Input data for Example 5.1:
mu = 398600;
r1 = [-294.32 4265.1 5986.7];
r2 = [-1365.4 3637.6 6346.8];
r3 = [-2940.3 2473.7 6555.8];
%...
%...Echo the input data to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 5.1: Gibbs Method\n')
fprintf('\n\n Input data:\n')
fprintf('\n Gravitational parameter (kmˆ3/sˆ2) = %g\n', mu)
fprintf('\n r1 (km) = [%g %g %g]', r1(1), r1(2), r1(3))
fprintf('\n r2 (km) = [%g %g %g]', r2(1), r2(2), r2(3))
fprintf('\n r3 (km) = [%g %g %g]', r3(1), r3(2), r3(3))
fprintf('\n\n');
[v2, ierr] = gibbs(r1, r2, r3);
if ierr == 1
fprintf('\n These vectors are not coplanar.\n\n')
return
end
%...Algorithm 4.1
coe = coe_from_sv(r2,v2);
h = coe(1);
e = coe(2);
RA = coe(3);
incl = coe(4);
w = coe(5);
TA = coe(6);
a = coe(7);
%...Output the results to the command window:
fprintf(' Solution:')
fprintf('\n');
fprintf('\n v2 (km/s) = [%g %g %g]', v2(1), v2(2), v2(3))
fprintf('\n\n Orbital elements:');
fprintf('\n Angular momentum (kmˆ2/s) = %g', h)
fprintf('\n Eccentricity = %g', e)
fprintf('\n Inclination (deg) = %g', incl/deg)
fprintf('\n RA of ascending node (deg) = %g', RA/deg)
fprintf('\n Argument of perigee (deg) = %g', w/deg)
fprintf('\n True anomaly (deg) = %g', TA/deg)
fprintf('\n Semimajor axis (km) = %g', a)
%...If the orbit is an ellipse, output the period:
if e < 1
T = 2*pi/sqrt(mu)*coe(7)^1.5;
fprintf('\n Period (s) = %g', T)
end
fprintf('\n-----------------------------------------------\n')
% ˜˜˜