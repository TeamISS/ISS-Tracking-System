function [f, g] = f_and_g(x, t, ro, a)
% ˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
%
% This function calculates the Lagrange f and g coefficients.
%
% mu - the gravitational parameter (kmˆ3/sˆ2)
% a - reciprocal of the semimajor axis (1/km)
% ro - the radial position at time t (km)
% t - the time elapsed since t (s)
% x - the universal anomaly after time t (kmˆ0.5)
% f - the Lagrange f coefficient (dimensionless)
% g - the Lagrange g coefficient (s)
%
% User M-functions required: stumpC, stumpS
% ------------------------------------------------------------
global mu
z = a*xˆ2;
%...Equation 3.66a:
f = 1 - xˆ2/ro*stumpC(z);
%...Equation 3.66b:
g = t - 1/sqrt(mu)*xˆ3*stumpS(z);
% ˜˜˜