#!/bin/bash

set -e

# bash script tracks the workflow memory stats during the workflow
# and when the workflow is over, sends the memorydata to python script that draws the plots

MEMORY_ARRAY=()
CPU_ARRAY=()
WORKFLOW_RUNNING=TRUE

plot_python() {
    echo "Saving data to files"
    printf "%s\n" "${MEMORY_ARRAY[@]}" > /tmp/memory.txt
    printf "%s\n" "${CPU_ARRAY[@]}" > /tmp/cpu.txt

    echo "Calling python"
    python ./memory_plot.py
}

trap plot_python EXIT

echo "Starting scan"

while [ $WORKFLOW_RUNNING ]
do

    STATUS_JSON=$(argo get @latest -o json -n argo)
    CURRENT_STATUS=$(echo $STATUS_JSON | jq -r '.status.phase')

    if [[ $CURRENT_STATUS == *"Failed"* ]] || [[ $CURRENT_STATUS == *"Succeeded"* ]] ; then
        WORKFLOW_RUNNING=FALSE

        exit 0
        
    else
        TOP_NOW=$(kubectl top pods -n argo)

        # Read the string in TOP_NOW to an array with space as separator
        # First replace new line with space with tr
        read -r -a TOP_ARRAY <<< "$(echo "$TOP_NOW" | tr '\n' ' ')"

        # CPU and MEMORY info are the 7th and 8th element
        # Read them to variables and drop the units from the end
        # Also convert them to numbers
        CPU=$((${TOP_ARRAY[7]::-1}))
        MEMORY=$((${TOP_ARRAY[8]::-2}))

        CPU_ARRAY+=($CPU)
        MEMORY_ARRAY+=($MEMORY)

        echo "Saved data"

    fi
    sleep 5

done