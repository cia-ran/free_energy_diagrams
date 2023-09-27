import matplotlib.pyplot as plt
from free_energy_diagrams import FED

# Setting the HEX colour keys to readable variable
gold = '#e0bf00'
graph = '#545663'

# Setting the "taf" variable to the "FED" class from within the "free_energy_diagrams" module. Also setting some deffault properties.
taf = FED(reaction_coords=['Clean', '$H_{S}$', '$H_{S},H_{S}$', '$H_{S},H_{Mo}$', 'Clean'], level_width=3.5, barrier_width=1)

# Adding the multiple energy levels of the overall free energy diageram and distinguishing which level relates to which system using colour.
taf.add_level(0, color='k')

taf.add_level(0.45, top_text='0.45', color=gold, label='Au (111)')
taf.add_level(0.29, bottom_text='0.29', position='l', color=graph, label='Graphene')

taf.add_level(0.99, top_text='0.99', color=gold)
taf.add_level(0.76, bottom_text='0.76', position='l', color=graph)

taf.add_level(1.09, top_text='1.09', color=graph)
taf.add_level(1.05, bottom_text='1.05', position='l', color=gold)

taf.add_level(0, color='k')

# Adding the multiple barriers for each system, again distinguished by colour. 
taf.add_barrier(0.59, 1, 2, ls='--',  color=gold)
taf.add_barrier(0.55, 1, 3, ls='--', color=graph)

taf.add_barrier(1.13, 2, 4, ls='--',  color=gold)
taf.add_barrier(1.02, 3, 5, ls='--', color=graph)

taf.add_barrier(1.90, 4, 7, ls='--',  color=gold)
taf.add_barrier(1.90, 5, 6, ls='--', color=graph)

taf.add_barrier(1.64, 6, 8, ls='--',  color=gold)
taf.add_barrier(1.73, 7, 8, ls='--', color=graph)

# Plotting and showing the figure.
au_hey.plot()
plt.show()
