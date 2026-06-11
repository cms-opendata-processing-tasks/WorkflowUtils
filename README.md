# start_memory_scan.sh
- Follows the memory usage of @latest argo workflow every 5 seconds
- When workflow ends, sends the usage data to `memory_plot.py` for plotting
- Plot of memory and CPU usage is saved in same dir

How to use:

Bind the memory scan to your workflow submit command
```
# e.g. if running the simulation workflow
argo submit -n argo FullSimulationArgoWorkflow/cms-simulation-process/run-simulation-s3.yaml && WorkflowUtils/start_memory_scan.sh >> memoryscan.log 2>&1 & 
```
The scanning stops automatically when the workflow stops. Then you can inspect the plots in `WorkflowUtils`
