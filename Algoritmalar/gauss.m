function [r, v, r_old, v_old] =gauss (Rho1, Rho2, Rho3, R1, R2, R3, t1, t2, t3)
global mu
tau1 = t1 - t2;
tau3 = t3 - t2;
tau = tau3 - tau1;
p1 = cross(Rho2,Rho3);
p2 = cross(Rho1,Rho3);
p3 = cross(Rho1,Rho2);
Do = dot(Rho1,p1);
D = [[dot(R1,p1) dot(R1,p2) dot(R1,p3)]
[dot(R2,p1) dot(R2,p2) dot(R2,p3)]
[dot(R3,p1) dot(R3,p2) dot(R3,p3)]];
E = dot(R2,Rho2);
A = 1/Do*(-D(1,2)*tau3/tau + D(2,2) + D(3,2)*tau1/tau);
B = 1/6/Do*(D(1,2)*(tau3^2 - tau^2)*tau3/tau+ D(3,2)*(tau^2 - tau1^2)*tau1/tau);
a = -(A^2 + 2*A*E + norm(R2)^2);
b = -2*mu*B*(A + E);
c = -(mu*B)^2;
Roots = roots([1 0 a 0 0 b 0 0 c]);
x = posroot(Roots);
f1 = 1 - 1/2*mu*tau1^2/x^3;
f3 = 1 - 1/2*mu*tau3^2/x^3;
g1 = tau1 - 1/6*mu*(tau1/x)^3;
g3 = tau3 - 1/6*mu*(tau3/x)^3;
rho2 = A + mu*B/x^3;
rho1 = 1/Do*((6*(D(3,1)*tau1/tau3 + D(2,1)*tau/tau3)*x^3+ mu*D(3,1)*(tau^2 - tau1^2)*tau1/tau3)/(6*x^3 + mu*(tau^2 - tau3^2)) - D(1,1));
rho3 = 1/Do*((6*(D(1,3)*tau3/tau1 - D(2,3)*tau/tau1)*x^3+ mu*D(1,3)*(tau^2 - tau3^2)*tau3/tau1)/(6*x^3 + mu*(tau^2 - tau3^2)) - D(3,3));
r1 = R1 + rho1*Rho1;
r2 = R2 + rho2*Rho2;
r3 = R3 + rho3*Rho3;
v2 = (-f3*r1 + f1*r3)/(f1*g3 - f3*g1);
r_old = r2;
v_old = v2;
rho1_old = rho1; rho2_old = rho2; rho3_old = rho3;
diff1 = 1; diff2 = 1; diff3 = 1;
n =0;
nmax = 1000;
tol = 1.e-8;
while ((diff1 > tol) && (diff2 > tol) && (diff3 > tol))&& (n < nmax)
n = n+1;
ro = norm(r2);
vo = norm(v2);
vro = dot(v2,r2)/ro;
a = 2/ro - vo^2/mu;
x1 = kepler_U(tau1, ro, vro, a);
x3 = kepler_U(tau3, ro, vro, a);
[ff1, gg1] = f_and_g(x1, tau1, ro, a);
[ff3, gg3] = f_and_g(x3, tau3, ro, a);
f1 = (f1 + ff1)/2;
f3 = (f3 + ff3)/2;
g1 = (g1 + gg1)/2;
g3 = (g3 + gg3)/2;
c1 = g3/(f1*g3 - f3*g1);
c3 = -g1/(f1*g3 - f3*g1);
rho1 = 1/Do*( -D(1,1) + 1/c1*D(2,1) - c3/c1*D(3,1));
rho2 = 1/Do*( -c1*D(1,2) + D(2,2) - c3*D(3,2));
rho3 = 1/Do*(-c1/c3*D(1,3) + 1/c3*D(2,3) - D(3,3));
r1 = R1 + rho1*Rho1;
r2 = R2 + rho2*Rho2;
r3 = R3 + rho3*Rho3;
v2 = (-f3*r1 + f1*r3)/(f1*g3 - f3*g1);
diff1 = abs(rho1 - rho1_old);
diff2 = abs(rho2 - rho2_old);
diff3 = abs(rho3 - rho3_old);
rho1_old = rho1; rho2_old = rho2; rho3_old = rho3;
end
fprintf('\n( **Number of Gauss improvement iterations')
fprintf(' = %g)\n\n', n)
if n >= nmax
fprintf('\n\n **Number of iterations exceeds %g \n\n ', nmax);
end
r = r2;
v = v2;
return

function x = posroot(Roots)

posroots = Roots(Roots>0 & imag(Roots));
npositive = length(posroots);

if npositive == 0
    fprintf('\n\n ** There are no positive roots. \n\n')
return
end

if npositive == 1
x = posroots;
else
fprintf('\n\n ** There are two or more positive roots.\n')
for i = 1:npositive
fprintf('\n root #%g = %g', i, posroots(i))
end
fprintf('\n\n Make a choice:\n')
nchoice = 0;
while nchoice < 1 || nchoice > npositive
nchoice = input(' Use root #? ');
end
x = posroots(nchoice);
fprintf('\n We will use %g .\n', x)
end
return
