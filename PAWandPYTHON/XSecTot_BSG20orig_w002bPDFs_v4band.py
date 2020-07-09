import matplotlib.pylab as plt
import numpy as np
#from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes 
#from mpl_toolkits.axes_grid1.inset_locator import mark_inset

### Load the dataset

x1, y1, erry1 = np.loadtxt("paw_Stpa.dat", usecols = (0,1,2), unpack = True)

x2, y2, erry2 = np.loadtxt("paw_Stpp_semLHC.dat", usecols = (0,1,2), unpack = True)

x3, y3, erry3 = np.loadtxt("paw_StATLAS.dat", usecols = (0,1,2), unpack = True)

x4, y4, erry4 = np.loadtxt("paw_StTOTEM.dat", usecols = (0,1,2), unpack = True)

### Load the Fitting total cross-section results

px1, py1 = np.loadtxt("XSecTotPP_BSG20orig_w002b.dat", usecols = (0,1), unpack = True)

px2, py2 = np.loadtxt("XSecTotPBP_BSG20orig_w002b.dat", usecols = (0,1), unpack = True)

px3, py3 = np.loadtxt("XSecTotPP_BSG20orig_w002b_NNPDF31.dat", usecols=(0,1), unpack=True)
px31, py31 = np.loadtxt("XSecTotPP_BSG20orig_w002b_NNPDF31_member_38.dat", usecols = (0,1), unpack = True)
px32, py32 = np.loadtxt("XSecTotPP_BSG20orig_w002b_NNPDF31_member_51.dat", usecols = (0,1), unpack = True)

px4, py4 = np.loadtxt("XSecTotPBP_BSG20orig_w002b_NNPDF31.dat", usecols = (0,1), unpack=True)
px41 ,py41 = np.loadtxt("XSecTotPBP_BSG20orig_w002b_NNPDF31_member_38.dat", usecols = (0,1), unpack = True)
px42, py42 = np.loadtxt("XSecTotPBP_BSG20orig_w002b_NNPDF31_member_51.dat", usecols = (0,1), unpack = True)

px5, py5 = np.loadtxt("XSecTotPP_BSG20orig_w002b_MMHT.dat", usecols = (0,1), unpack = True)
px51, py51 = np.loadtxt("XSecTotPP_BSG20orig_w002b_MMHT_member_34.dat", usecols = (0,1), unpack = True)
px52, py52 = np.loadtxt("XSecTotPP_BSG20orig_w002b_MMHT_member_39.dat", usecols = (0,1), unpack = True)

px6, py6 = np.loadtxt("XSecTotPBP_BSG20orig_w002b_MMHT.dat", usecols = (0,1), unpack = True)
px61, py61 = np.loadtxt("XSecTotPBP_BSG20orig_w002b_MMHT_member_34.dat", usecols = (0,1), unpack = True)
px62, py62 = np.loadtxt("XSecTotPBP_BSG20orig_w002b_MMHT_member_39.dat", usecols = (0,1), unpack = True)

### Setting Font info's

font = {'family': 'serif','color':  'black', 'weight': 'normal', 'size': 16,}

plt.subplots_adjust(left = 0.1, bottom = 0.1, right = 0.98, top = 0.95, wspace = 0, hspace = 0)

plt.semilogx()
plt.grid(False)
plt.xlim(5,20000)
plt.ylim(30,120)

### Plotting the datasets

plt.errorbar(x1, y1, yerr = erry1, fmt = 'wo', ecolor = 'k', markeredgecolor = 'k', capthick = 0.5, label = r"$\bar{p}p$", zorder = 1)
plt.errorbar(x2, y2, yerr = erry2, fmt = 'ko', ecolor = 'k', markeredgecolor = 'k', capthick = 0.5, label = r"$pp$ below LHC", zorder = 1)
plt.errorbar(x3, y3, yerr = erry3, fmt = 'bs', ecolor = 'b', markeredgecolor = 'b', capthick = 0.5, label = "ATLAS", zorder = 1)
plt.errorbar(x4, y4, yerr = erry4, fmt = 'r^', ecolor = 'r', markeredgecolor = 'r', capthick = 0.5, label = "TOTEM", zorder = 1)

### Plotting the fitting curves

plt.plot(px1, py1, 'k-', linewidth = 1.25, label = r"CT14", zorder = 3)
plt.plot(px2, py2, 'k-', linewidth = 1.25, zorder = 2)

plt.plot(px3, py3, 'r--', linewidth = 1.25, label = r"NNPDF31", zorder = 3)
plt.plot(px4, py4, 'r--', linewidth = 1.25, zorder = 2)

plt.plot(px5, py5, 'b:', linewidth = 1.25, label = r"MMHT", zorder = 3)
plt.plot(px6, py6, 'b:', linewidth = 1.25, zorder = 2)

### Plotting the uncertainty band

plt.fill_between(px3, py31, py32, color = 'r',alpha = 0.2)
plt.fill_between(px4, py41, py42, color = 'r',alpha = 0.2)
plt.fill_between(px5, py51, py52, color = 'b',alpha = 0.2)
plt.fill_between(px6, py61, py62, color = 'b',alpha = 0.2)

### Labels

plt.xlabel(r"$\sqrt{s}$ [GeV]", fontdict = font)
plt.ylabel(r"$\sigma_{tot}(s)$ [mb]", fontdict = font)

### Legend info's

leg = plt.legend(loc = 4, ncol = 1, shadow = False, fancybox = False, frameon = False, numpoints = 1)
leg.get_frame().set_alpha(0.5)

###########################################

### Miniframe definitions

sub_axes = plt.axes([.2, .55, .35, .35])

plt.grid(False)
plt.semilogx()
plt.xlim(5000,15000)
plt.ylim(90,120)

### Plotting the datasets

plt.errorbar(x3, y3, yerr = erry3, fmt = 'bs', ecolor = 'b', markeredgecolor = 'b', capthick = 0.5)
plt.errorbar(x4, y4, yerr = erry4, fmt = 'r^', ecolor = 'r', markeredgecolor = 'r', capthick = 0.5)

### Plotting the fitting curves

plt.plot(px1, py1, 'k-', linewidth = 1.25)
plt.plot(px2, py2, 'k-', linewidth = 1.25)

plt.plot(px3, py3, 'r--', linewidth = 1.25)
plt.plot(px4, py4, 'r--', linewidth = 1.25)

plt.plot(px5, py5, 'b:', linewidth = 1.25)
plt.plot(px6, py6, 'b:', linewidth = 1.25)

### Plotting the uncertainty band

plt.fill_between(px3, py31, py32, color = 'r',alpha = 0.2)
plt.fill_between(px4, py41, py42, color = 'r',alpha = 0.2)
plt.fill_between(px5, py51, py52, color = 'b',alpha = 0.2)
plt.fill_between(px6, py61, py62, color = 'b',alpha = 0.2)

###########################################

plt.savefig("XSecTot_BSG20orig_w002bPDFs_v4band.pdf")
#plt.show()

