import matplotlib.pyplot as plt
from free_energy_diagrams import FED

# Setting the HEX colour keys to readable variable
system1 = '#e0bf00'
system2 = '#545663'

# Setting the "taf" variable to the "FED" class from within the "free_energy_diagrams" module. Also setting some deffault properties.
reaction = FED(reaction_coords=['Clean', 'adsorption', 'adsorption', 'diffusion', 'Clean'], level_width=3.5, barrier_width=1)

# Adding the multiple energy levels of the overall free energy diageram and distinguishing which level relates to which system using colour.
reaction.add_level(0, color='k')

reaction.add_level(0.40, top_text='0.40', color=system1, label='System 1')
reaction.add_level(0.30, bottom_text='0.30', position='l', color=system2, label='System 2')

reaction.add_level(1.00, top_text='1.00', color=system1)
reaction.add_level(0.70, bottom_text='0.70', position='l', color=system2)

reaction.add_level(1.20, top_text='1.20', color=system1)
reaction.add_level(1.10, bottom_text='1.10', position='l', color=system2)

reaction.add_level(0, color='k')

# Adding the multiple barriers for each system, again distinguished by colour. 
reaction.add_barrier(0.60, 1, 2, ls='--',  color=system1)
reaction.add_barrier(0.50, 1, 3, ls='--', color=system2)

reaction.add_barrier(1.10, 2, 4, ls='--',  color=system1)
reaction.add_barrier(1.00, 3, 5, ls='--', color=system2)

reaction.add_barrier(1.90, 4, 7, ls='--',  color=system1)
reaction.add_barrier(1.70, 5, 6, ls='--', color=system2)

reaction.add_barrier(1.60, 6, 8, ls='--',  color=system1)
reaction.add_barrier(1.40, 7, 8, ls='--', color=system2)

# Plotting and showing the figure.
reaction.plot()
plt.show()
