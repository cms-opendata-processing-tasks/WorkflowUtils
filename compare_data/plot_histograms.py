import uproot
import matplotlib.pylab as plt
import awkward as ak
import numpy as np


# Open files where file1 is your produced data, and file2 is the reference data
file1 = uproot.open("my_filename.root:Events")
file2 = uproot.open("open_data_portal_dataset.root:Events")

events1 = 50000 # Check values for your datasets
events2 = 50000 # Check values for your datasets

plottables = ["Electron_pt", "Muon_pt", "Electron_phi", "Muon_phi", "Electron_eta", "Muon_eta"]
plot_limits = [(0, 80), (0, 80), (-5, 5), (-5, 5), (-5, 5), (-5, 5)]

def plot_histogram(variable, plot_low_lim, plot_high_lim):
    # Empty the plotting canvas
    plt.figure()

    # Flatten the data
    flattened_data_1 = ak.flatten(file1[f"{variable}"].array())
    flattened_data_2 = ak.flatten(file2[f"{variable}"].array())

    # Calculate the avg, standard deviation and over- and underflow
    avg_1 = np.average(flattened_data_1)
    avg_2 = np.average(flattened_data_2)
    stdev_1 = np.std(flattened_data_1)
    stdev_2 = np.std(flattened_data_2)
    under_1 = len(flattened_data_1[flattened_data_1 >= plot_high_lim])
    under_2 = len(flattened_data_2[flattened_data_2 >= plot_high_lim])
    over_1 = len(flattened_data_1[flattened_data_1 < plot_low_lim])
    over_2 = len(flattened_data_2[flattened_data_2 < plot_low_lim])

    plt.hist(
        flattened_data_1, 
        bins=50, 
        range=(plot_low_lim, plot_high_lim), 
        density=True,
        color='#0000ff', 
        alpha=0.5,
        histtype=u'step',
        label=f"Workflow\nEvents: {events1:.0f}\nMean: {avg_1:.10f}\nStd Dev: {stdev_1:.10f}\nUnderflow: {under_1:.0f}\nOverflow: {over_1:.0f}"
    )
    plt.hist(
        flattened_data_2,
        bins=50,
        range=(plot_low_lim, plot_high_lim),
        density=True,
        color='#ff0000',
        alpha=0.5,
        histtype=u'step',
        label=f"Reference\nEvents: {events2:.0f}\nMean: {avg_2:.10f}\nStd Dev: {stdev_2:.10f}\nUnderflow: {under_2:.0f}\nOverflow: {over_2:.0f}"

    )

    # plt.title(r"", fontsize=14)
    plt.xlabel(f"{variable}", fontsize=12)
    plt.ylabel("Relative frequency", fontsize=12)
    plt.legend()
    plt.grid(axis='y', linestyle="-", alpha=0.7)

    plt.savefig(f"{variable}.png")

for var in plottables:
    index = plottables.index(var)
    plot_histogram(var, plot_limits[index][0], plot_limits[index][1])

