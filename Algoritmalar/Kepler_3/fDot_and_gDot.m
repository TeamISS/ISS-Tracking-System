% ˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
function [fdot, gdot] = fDot_and_gDot(x, r, ro, a)
global mu
z = a*x^2;
%...Equation 3.66c:
fdot = sqrt(mu)/r/ro*(z*stumpS(z) - 1)*x;
%...Equation 3.66d:
gdot = 1 - x^2/r*stumpC(z);
% ˜