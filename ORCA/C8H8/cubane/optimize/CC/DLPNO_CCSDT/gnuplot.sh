#!/usr/bin/gnuplot -persist

set grid

f(x,y) = Cxx*(x-a)**2 + Cyy*(y-b)**2 + Cxy*(x-a)*(y-b) + E
Cxx=100.0; Cyy=10.0; Cxy=-10.0; a=0.782; b=1.409; E=-308.9

fit f(x,y) "scan.dat" using 1:2:3:(1) via Cxx, Cyy, Cxy, a, b, E

splot "scan.dat" using 1:2:3 with linespoints, f(x,y)
