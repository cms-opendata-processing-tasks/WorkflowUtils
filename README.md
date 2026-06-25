# start_memory_scan.sh
- Follows the memory usage of @latest argo workflow every 5 seconds
- When workflow ends, sends the usage data to `memory_plot.py` for plotting
- Plot of memory and CPU usage is saved in same dir

How to use:

### 1. Add the path to this directory in PATH variable 

```
export PATH=$PATH:/path/to/WorkflowUtils
```

### 2. Check that you have the Kubernetes Metrics Server enabled

If `kubectl top pods -n argo` does not work, do this
```
cd /path/to/WorkflowUtils/
kubectl apply -f components.yaml
```

### 3. Requirements

```bash
sudo apt install jq
```
Setup python
```bash
cd /path/to/WorkflowUtils
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Bind the memory scan to your workflow submit command
```
cd /path/to/FullSimulationArgoWorkflow
mkdir memoryscan

argo submit -n argo cms-simulation-process/run-pp-simulation.yaml && start_memory_scan.sh > memoryscan/scan.log 2>&1 & 
```
The scanning stops automatically when the workflow stops. Then you can inspect the plots in `FullSimulationArgoWorkflow/`
