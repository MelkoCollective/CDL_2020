.SUFFIXES: .o .c .f .cxx
# DEBUG option remove for efficiency
CC=/usr/bin/g++
cc=/usr/bin/gcc
FC=/usr/bin/gfortran
options= -DDUSHQUICK -DBLAS -DLINUX -O2 -Wno-deprecated
objects=FC.o matvec.o prod.o
dependencies=matvec.h 
FC_fast : $(objects)
	$(CC) -o FCF_calc $(objects)  \
-framework Accelerate -L/usr/lib/gcc/x86_64-linux-gnu/9/libgfortran.a -lgfortran
$(objects): $(dependencies)
.cxx.o:
	$(CC) -c $(options) $<
.c.o:
	$(cc) -c -O2 $<
.f.o:
	$(FC) -c -O2 $<
