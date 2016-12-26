#!/bin/sh

task_dir=`pwd`

for dir in "."
do
    cd $dir
    nohup mpirun -np 4 nwchem cubane.nw > cubane.nwo 2>&1 &
    cd $task_dir
done
