#!/bin/sh

task_dir=`pwd`

for dir in "."
do
    cd $dir
    #mpirun -np 2 
    nohup nwchem cubane.nw > cubane.nwo 2>&1 &
    cd $task_dir
done
