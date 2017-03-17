#!/bin/sh

task_dir=`pwd`

ORCA_PATH=/home/vladimir/bin/orca_4_0_0_linux_x86-64
export PATH=$PATH:$ORCA_PATH

for dir in '.'
do
    if [ ! -e $task_dir/$dir/cubane.out ];
    then
        $ORCA_PATH/orca $task_dir/$dir/cubane.inp > $task_dir/$dir/cubane.out &
    else
        echo "file $task_dir/$dir/cubane.out exists, skiping execution"
    fi
done
