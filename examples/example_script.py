import matplotlib.pyplot as plt
from free_energy_diagrams import FED

gold = '#e0bf00'
graph = '#545663'

au_hey = FED(reaction_coords=['Clean', '$H_{S}$', '$H_{S},H_{S}$', '$H_{S},H_{Mo}$', 'Clean'], level_width=3.5, barrier_width=1)
au_hey.add_level(0, color='k')

au_hey.add_level(0.45, top_text='0.45', color=gold, label='Au (111)')
au_hey.add_level(0.29, bottom_text='0.29', position='l', color=graph, label='Graphene')

au_hey.add_level(0.99, top_text='0.99', color=gold)
au_hey.add_level(0.76, bottom_text='0.76', position='l', color=graph)

au_hey.add_level(1.09, top_text='1.09', color=graph)
au_hey.add_level(1.05, bottom_text='1.05', position='l', color=gold)

au_hey.add_level(0, color='k')

au_hey.add_barrier(0.59, 1, 2, ls='--',  color=gold)
au_hey.add_barrier(0.55, 1, 3, ls='--', color=graph)

au_hey.add_barrier(1.13, 2, 4, ls='--',  color=gold)
au_hey.add_barrier(1.02, 3, 5, ls='--', color=graph)

au_hey.add_barrier(1.90, 4, 7, ls='--',  color=gold)
au_hey.add_barrier(1.90, 5, 6, ls='--', color=graph)

au_hey.add_barrier(1.64, 6, 8, ls='--',  color=gold)
au_hey.add_barrier(1.73, 7, 8, ls='--', color=graph)


au_hey.plot()
plt.show()
