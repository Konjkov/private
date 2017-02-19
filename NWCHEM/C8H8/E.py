#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt, exp, log10

#http://webbook.nist.gov/cgi/cbook.cgi?ID=C277101
#http://cccbdb.nist.gov/exp2.asp?casno=277101

Eh = 2625.5 # KJ/mol

Eh_H = -0.592039
Eh_C = -38.121621
Eh_N = -54.774096

Eh_H_atom = -0.499757
Eh_C_atom = -37.858885
Eh_N_atom = -54.617171

E_C8H8 = 622.1
E_H_atom = 216.03
E_C_atom = 711.79

Eh_C8H8 = 8*Eh_C + 8*Eh_H + E_C8H8/Eh
Eh_C8H8_atom = 8*Eh_H_atom + 8*Eh_C_atom + (E_C8H8 - E_C_atom*8 - E_H_atom*8)/Eh

R = 8.314
kT = 1.38E-23*518
h = 6.63E-34
sterical_factor = 12

ha2cm = 219474.63

ZPVE = 28211.0

# C8H8 (622.1) = 8C (711.79) + 8H(216.03*8) + dE
# C8H8 (X) = 8C (-37.78430) + 8H(-0.5) + dE

# Экспериментальные данные
# Диаппазон измерения константы разложения кубана: 503-533 K
# энергия активации Арениуса: Eact = 43.1 +- 1 kkal/mol = 180.4 КДж/моль
# Предэкспоненциальный множитель: lg(A) = 14.68 +- 0.44; A = 4.79E14
# Для мономолекулярной реакции в теории переходного состояния, 
# эти параметры выражаются через H# и S# переходного состояния следующим образом
# Eact = H# + RT
# A = kT/h * exp(S#/R) * exp(1) * sterical_factor
# Стерический фактор зависит от симметрии реагента и переходного состояния
# sterical_factor = NSYM(Oh)/NSYM(C2v) = 24/2 = 12
# kT/h = 1.38E-23*298/6.63E-34 = 6.20271493213e+12 (298K)
# kT/h = 1.38E-23*518/6.63E-34 = 1.07819004525e+13 (518K)
# S# = ln(2.36750572112) * 8.314 = (7.16 +- 8.42) Дж/моль (298K)
# S# = ln(1.332) * 8.314 = (2.38 +- 8.42) Дж/моль (518K)

print "E reagent, ZPVE       "
print "EXP                   ", Eh_C8H8_atom,  ZPVE
print "HF/SVP                ", -307.16662593, ZPVE/(0.143473*ha2cm)
print "HF/TZVP               ", -307.49141371, ZPVE/(0.143011*ha2cm)
print "HF/TZVPP              ", -307.49407724
print "HF/QZVPP              ", -307.50667389
print "DFT/B3LYP/SVP         ", -309.25671843, ZPVE/(0.133152*ha2cm)
print "DFT/B3LYP/TZVP        ", -309.56796598
print "DFT/B3LYP/TZVPP       ", -309.57046570
print "DFT/B3LYP/QZVPP       ", -309.58578847
print "MP2/cc-pVDZ           ", -308.48390107, ZPVE/(0.133401*ha2cm)
print "MP2/cc-pVTZ           ", -308.77821873
print "MP2/cc-pVQZ           ", -308.87582657
print "CCSD/cc-pVDZ          ", -308.54310625, ZPVE/(0.134072*ha2cm)
print "CCSD/cc-pVTZ          ", -308.81701939
print "CCSD(T)/cc-pVDZ       ", -308.58966794
#print "CCSD(T)/cc-pVTZ       ", -308.
print ""
print "E triplet 1           "
print "HF/SVP (ROHF)         ", -307.12942889
print "HF/SVP (UHF)          ", -307.13696576
print "HF/TZVP (UHF)         ", -307.46326746
print "DFT/B3LYP/SVP (UHF)   ", -309.19214544
print "MP2/cc-pVDZ (UHF)     ", -308.41202834
print "CCSD/cc-pVDZ (ROHF)   ", -308.47989005
print ""
print "E triplet 2           "
print "HF/SVP (UHF)          ", -307.13298580
print "DFT/B3LYP/SVP (UHF)   ", -309.19060878
print "MP2/cc-pVDZ (UHF)     ", -308.40879784
print "CCSD/cc-pVDZ (ROHF)   ", -308.47651808
print ""
print "E transition state 1  "
print "CASSCF(2.2)/SVP       ", -307.11837439, 0.136802*219474.63
print "CASSCF(2.2)/TZVP      ", -307.44429507
print "DFT/B3LYP/SVP         ", -309.13788368
print "MK-MRCCSD/cc-pVDZ     ", -308.46391390
print "MK-MRCCSD/cc-pVTZ//MK-MRCCSD/cc-pVDZ", -308.73307760
print "MK-MRCCSD(T)/cc-pVDZ  ", -308.51742030
#print "MK-MRCCSD(T)/cc-pVTZ  ", -308.
print ""
print "E transition state 2"
print "MK-MRCCSD/cc-pVDZ     ", -308.46541076
print "MK-MRCCSD(T)/cc-pVDZ  ", -308.5212
print ""
print "Eact kJ/mol"
print "EXP                   ", "180.4 +- 4.2"
print "transition state 1    "
print "HF-CASSCF(6.4)/SVP    ", (-(-307.16662593 - -307.11860832) - (0.143473 - 0.136802) * 0.9)*Eh + R*0.518
print "MK-MRCCSD/cc-pVDZ     ", (-(-308.54310625 - -308.46391390) - (0.143473 - 0.136802) * 0.9)*Eh + R*0.518
print "MK-MRCCSD/cc-pVTZ     ", (-(-308.81701939 - -308.73307760) - (0.143473 - 0.136802) * 0.9)*Eh + R*0.518
print "MK-MRCCSD(T)/cc-pVDZ  ", (-(-308.58966794 - -308.51742030) - (0.143473 - 0.136802) * 0.9)*Eh + R*0.518
print ""
print "transition state 2    "
print "MK-MRCCSD/cc-pVDZ     ", (-(-308.54310625 - -308.46541076) - (0.143473 - 0.136802) * 0.9)*Eh + R*0.518
print "MK-MRCCSD(T)/cc-pVDZ  ", (-(-308.58966794 - -308.5212) - (0.143473 - 0.136802) * 0.9)*Eh + R*0.518
print ""
print "dS J/mol-K at 518,273K"
print "dS reagent            "
print "HF/SVP                ", 86.596*4.1868
print "HF/TZVP               ", 86.592*4.1868
print "MP2/cc-pVDZ           ", 90.162*4.1868
print "CCSD/cc-pVDZ          ", 89.930*4.1868
print ""
print "dS TS-1"
print "CASSCF(6.4)/SVP       ", 91.882*4.1868
print "CASSCF(8.5)/SVP       ", 91.265*4.1868
print "MK-MRCCSD/6-31G       ", 96.905*4.1868
print ""
print "EXP ln(A)             ", "14.68 +- 0.44"
print "HF-CASSCF(6,4)/SVP    ", log10(kT/h * exp((91.882 - 86.596)*4.1868/R) * exp(1) * sterical_factor)
print "HF-CASSCF(8,5)/SVP    ", log10(kT/h * exp((91.265 - 86.596)*4.1868/R) * exp(1) * sterical_factor)
print "(MK-MR)CCSD/6-31G+cc-pVDZ", log10(kT/h * exp((96.905 - 89.930)*4.1868/R) * exp(1) * sterical_factor)
print "zero entropy          ", log10(kT/h * exp((0)*4.1868/R) * exp(1) * sterical_factor)
print ""
print "EXP Bond length       ", 1.571, 1.098
print "HF/SVP                ", 0.77945112*2, (1.40763354-0.77945112)*sqrt(3)
print "HF/TZVP               ", 0.77871807*2, (1.40174241-0.77871807)*sqrt(3)
print "HF/TZVPP              ", 0.77872474*2, (1.40135306-0.77872474)*sqrt(3)
print "HF/QZVPP              ", 0.77851101*2, (1.40080932-0.77851101)*sqrt(3)
print "DFT/B3LYP/SVP         ", 0.78432349*2, (1.41878273-0.78432349)*sqrt(3)
print "DFT/B3LYP/TZVP        ", 0.78366499*2, (1.41150271-0.78366499)*sqrt(3)
print "DFT/B3LYP/TZVPP       ", 0.78369057*2, (1.41109888-0.78369057)*sqrt(3)
print "DFT/B3LYP/QZVPP       ", 0.78371973*2, (1.41063149-0.78371973)*sqrt(3)
print "DFT/PBE0/QZVPP        ", 0.77924794*2, (1.40713015-0.77924794)*sqrt(3)
print "MP2/cc-pVDZ           ", 0.78811233*2, (1.42345400-0.78811233)*sqrt(3)
print "MP2/cc-pVTZ           ", 0.78312104*2, (1.41001962-0.78312104)*sqrt(3)
print "MP2/cc-pVTQ           ", 0.78187341*2, (1.40904610-0.78187341)*sqrt(3)
print "CCSD/cc-pVDZ          ", 0.78961438*2, (1.42503470-0.78961438)*sqrt(3)
print "CCSD/cc-pVTZ          ", 0.78381707*2, (1.41035684-0.78381707)*sqrt(3)
print "CCSD(T)/cc-pVDZ       ", 0.79205620*2, (1.42871342-0.79205620)*sqrt(3)
print "CCSD(T)/cc-pVTZ       "
