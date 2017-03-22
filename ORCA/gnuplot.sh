#!/usr/bin/gnuplot -persist

set grid

#plot "bonds.dat" using ($2*2):(($3-$2)*sqrt(3)) with linespoints notitle,\
#     "bonds.dat" using ($2*2):(($3-$2)*sqrt(3)):1 with labels offset -6.0,-0.5 font "arial,8" notitle,\
#     "equlibrium.dat" using 2:3:4:5 with xyerrorbars notitle,\
#     "equlibrium.dat" using 2:3:1 with labels offset -6.0,-0.5 font "arial,8" notitle

plot "T-bonds.dat" using ($2*2):($3*2) with linespoints notitle,\
     "T-bonds.dat" using ($2*2):($3*2):1 with labels offset -6.0,-0.5 font "arial,8" notitle

#plot "energy.dat" using 2:3 with linespoints notitle,\
#     "energy.dat" using 2:3:1 with labels offset -6.0,-0.5 font "arial,8" notitle
