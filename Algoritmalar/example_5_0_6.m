clear
%...Input data for Example 5.6:
% East longitude:
degrees = 139;
minutes = 47;
seconds = 0;
% Date:
year = 2004;
month = 3;
day = 3;
% Universal time:
hour = 4;
minute = 30;
second = 0;
%...
%...Convert negative (west) longitude to east longitude:
if degrees < 0
degrees = degrees + 360;
end
%...Express the longitudes as decimal numbers:
EL = degrees + minutes/60 + seconds/3600;
WL = 360 - EL;
%...Express universal time as a decimal number:
ut = hour + minute/60 + second/3600;
%...Algorithm 5.3:
lst = LST(year, month, day, ut, EL);
%...Echo the input data and output the results to the command window:
fprintf('---------------------------------------------------')
fprintf('\n Example 5.6: Local sidereal time calculation\n')
fprintf('\n Input data:\n');
fprintf('\n Year = %g', year)
fprintf('\n Month = %g', month)
fprintf('\n Day = %g', day)
fprintf('\n UT (hr) = %g', ut)
fprintf('\n West Longitude (deg) = %g', WL)
fprintf('\n East Longitude (deg) = %g', EL)
fprintf('\n\n');
fprintf(' Solution:')
fprintf('\n');
fprintf('\n Local Sidereal Time (deg) = %g', lst)
fprintf('\n Local Sidereal Time (hr) = %g', lst/15)
fprintf('\n-----------------------------------------------\n')
% �����