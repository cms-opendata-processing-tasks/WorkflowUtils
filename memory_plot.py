import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

memory_data = np.array(np.loadtxt("/tmp/memory.txt"))
cpu_data = np.array(np.loadtxt("/tmp/cpu.txt"))

time = np.arange(0, 5 * memory_data.size, 5)


date = datetime.today().strftime('%Y-%m-%d_%H:%M')

fig, ax1 = plt.subplots()

ax1.plot(time, memory_data, 'r', label="Memory usage")
ax1.set_xlabel("time from start of workflow (s)")
ax1.set_ylabel("Memory usage (Mi)", color='r')
ax1.tick_params(axis='y', labelcolor='r')

ax2 = ax1.twinx()
ax2.plot(time, cpu_data, 'b', label="CPU usage")
ax2.set_ylabel("CPU usage (m)", color='b')
ax2.tick_params(axis='y', labelcolor='b')

plt.title("Memory and CPU usage of one workflow pod")
plt.margins(y=0.5)

# Some magic to get both ax1 and ax2 labels showing in the legend
line1, label1 = ax1.get_legend_handles_labels()
line2, label2 = ax2.get_legend_handles_labels()
ax1.legend(line1 + line2, label1 + label2)

fig.tight_layout()

plt.savefig(f"/memoryscan/workflow_memory_plot_{date}.png")

print("Plot saved")
print("Exiting")
