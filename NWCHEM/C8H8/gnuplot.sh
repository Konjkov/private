#!/usr/bin/gnuplot -persist

set grid

plot "bonds.dat" using 2:3 with linespoints notitle, '' using 2:3:1 with labels offset -6.0,-0.5 font "arial,8" notitle
