import uproot
import matplotlib.pylab as plt
import awkward as ak
import numpy as np


# Open files where file1 is your produced data, and file2 is the reference data
file1 = uproot.open("my_file_name.root:Events")
file2 = uproot.open("open_data_portal_dataset.root:Events")


# If you want to plot a different variable than phi, replace Electron_phi with the variable
# Make sure to update the title and axis names of the plot as well
flattened_electron_phi_1 = ak.flatten(file1['Electron_phi'].array())
flattened_electron_phi_2 = ak.flatten(file2['Electron_phi'].array())

# x-axis limits of the histogram
elec_plot_low_lim = -10
elec_plot_high_lim = 10

# Calculate numerical values for some statistics to show in the legend of the plot
electron_avg_1 = np.average(flattened_electron_phi_1)
electron_stdev_1 = np.std(flattened_electron_phi_1)
electron_under_1 = len(flattened_electron_phi_1[flattened_electron_phi_1 >= elec_plot_high_lim])
electron_over_1 = len(flattened_electron_phi_1[flattened_electron_phi_1 < elec_plot_low_lim])

electron_avg_2 = np.average(flattened_electron_phi_2)
electron_stdev_2 = np.std(flattened_electron_phi_2)
electron_under_2 = len(flattened_electron_phi_2[flattened_electron_phi_2 >= elec_plot_high_lim])
electron_over_2 = len(flattened_electron_phi_2[flattened_electron_phi_2 < elec_plot_low_lim])


plt.hist(
    flattened_electron_phi_1, 
    bins=50, 
    range=(elec_plot_low_lim, elec_plot_high_lim), 
    color='#0000ff',
    density=True,
    alpha=0.5,
    histtype=u'step',
    label=f"Workflow\nMean: {electron_avg_1:.10f}\nStd Dev: {electron_stdev_1:.10f}\nUnderflow: {electron_under_1:.0f}\nOverflow: {electron_over_1:.0f}"
)
plt.hist(
    flattened_electron_phi_2,
    bins=50,
    range=(elec_plot_low_lim, elec_plot_high_lim),
    density=True,
    color='#ff0000',
    alpha=0.5,
    histtype=u'step',
    label=f"Reference\nMean: {electron_avg_2:.10f}\nStd Dev: {electron_stdev_2:.10f}\nUnderflow: {electron_under_2:.0f}\nOverflow: {electron_over_2:.0f}"
)


plt.title(r"Electron phi ($\phi$)", fontsize=14)
plt.xlabel(r"Electron $\phi$ (GeV)", fontsize=12)
plt.ylabel("Number of Electrons", fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle="-", alpha=0.7)

plt.savefig('norm_electron_phi.png')

# Clear the figure and draw another histogram
plt.figure()

flattened_muon_phi_1 = ak.flatten(file1['Muon_phi'].array())
flattened_muon_phi_2 = ak.flatten(file2['Muon_phi'].array())

muon_plot_low_lim = -10
muon_plot_high_lim = 10

muon_avg_1 = np.average(flattened_muon_phi_1)
muon_stdev_1 = np.std(flattened_muon_phi_1)

muon_avg_2 = np.average(flattened_muon_phi_2)
muon_stdev_2 = np.std(flattened_muon_phi_2)


muon_under_1 = len(flattened_muon_phi_1[flattened_muon_phi_1 >= muon_plot_high_lim])
muon_over_1 = len(flattened_muon_phi_1[flattened_muon_phi_1 < muon_plot_low_lim])

muon_under_2 = len(flattened_muon_phi_2[flattened_muon_phi_2 >= muon_plot_high_lim])
muon_over_2 = len(flattened_muon_phi_2[flattened_muon_phi_2 < muon_plot_low_lim])

plt.hist(
    flattened_muon_phi_1, 
    bins=50, 
    range=(muon_plot_low_lim, muon_plot_high_lim), 
    density=True,
    color='#0000ff', 
    alpha=0.5,
    histtype=u'step',
    label=f"Workflow\nMean: {muon_avg_1:.10f}\nStd Dev: {muon_stdev_1:.10f}\nUnderflow: {muon_under_1:.0f}\nOverflow: {muon_over_1:.0f}"
)
plt.hist(
    flattened_muon_phi_2,
    bins=50,
    range=(muon_plot_low_lim, muon_plot_high_lim),
    density=True,
    color='#ff0000',
    alpha=0.5,
    histtype=u'step',
    label=f"Reference\nMean: {muon_avg_2:.10f}\nStd Dev: {muon_stdev_2:.10f}\nUnderflow: {muon_under_2:.0f}\nOverflow: {muon_over_2:.0f}"

)

plt.title(r"Muon phi ($\phi$)", fontsize=14)
plt.xlabel(r"Muon $\phi$ (GeV)", fontsize=12)
plt.ylabel("Number of Muons", fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle="-", alpha=0.7)

plt.savefig('norm_muon_phi.png')