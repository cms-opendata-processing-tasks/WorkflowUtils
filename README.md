# start_memory_scan.sh
- Follows the memory usage of @latest argo workflow every 5 seconds
- When workflow ends, sends the usage data to `memory_plot.py` for plotting
- Plot of memory and CPU usage is saved in same dir

How to use:

### 1. Create a symlink of the helper script to your working dir
e.g. If you want to use the memory scan in repo FullSimulationArgoWorkflow:
```
ln -s /path/to/WorkflowUtils/start_memory_scan.sh /path/to/FullSimulationArgoWorkflow/start_memory_scan.sh
ln -s /path/to/WorkflowUtils/memory_plot.py /path/to/FullSimulationArgoWorkflow/memory_plot.py
```

### 2. Check that you have the Kubernetes Metrics Server enabled

If `kubectl top pods -n argo` does not work, do this
```
cd /path/to/WorkflowUtils/
kubectl apply -f components.yaml
```

### 3. Install requirements

```bash
sudo apt install jq

pip install -r requirements.txt
```

### 4. Bind the memory scan to your workflow submit command
```
cd /path/to/FullSimulationArgoWorkflow
argo submit -n argo cms-simulation-process/run-pp-simulation.yaml && start_memory_scan.sh > memoryscan/scan.log 2>&1 & 
```
The scanning stops automatically when the workflow stops. Then you can inspect the plots in `FullSimulationArgoWorkflow/`
