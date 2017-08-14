% ˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜
function F = kepler_H(e, M)


error = 1.e-8;
%...Starting value for F:
F = M;

ratio = 1;
while abs(ratio) > error
ratio = (e*sinh(F) - F - M)/(e*cosh(F) - 1);
F = F - ratio;
end
% ˜˜