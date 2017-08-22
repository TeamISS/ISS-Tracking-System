function [V2, ierr] = gibbs(R1, R2, R3)

global mu
tol = 1e-4;
ierr = 0;r1 = norm(R1);
r2 = norm(R2);
r3 = norm(R3);

c12 = cross(R1,R2);
c23 = cross(R2,R3);
c31 = cross(R3,R1);

if abs(dot(R1,c23)/r1/norm(c23)) > tol
ierr = 1;
end
N = r1*c23 + r2*c31 + r3*c12;

D = c12 + c23 + c31;

S = R1*(r2 - r3) + R2*(r3 - r1) + R3*(r1 - r2);

V2 = sqrt(mu/norm(N)/norm(D))*(cross(D,R2)/r2 + S);
