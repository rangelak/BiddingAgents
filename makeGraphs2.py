import matplotlib.pyplot as plt
import auction
import numpy as np
import sys

options = [["auction.py", "--loglevel", "debug", "--num-rounds", "48", "--perms", "1", "--iters", "200", "--seed", "2", "--mech=GSP", "Truthful,5"]]

# results = list(map(auction.main, options))
results = []
for option in options:
	sys.argv = option
	results.append(auction.main(sys.argv))

expenditures = results[0][2]
utilities = results[0][3]
print("Utilities = " + str(utilities))

n_groups = len(expenditures)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.75
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, expenditures, bar_width,
                alpha=opacity, color='b',
                label='Expenditure')
rects2 = ax.bar(index + bar_width, utilities, bar_width,
                alpha=opacity, color='r',
                label='Utility')
rects3 = ax.bar(index + bar_width, [max(max(utilities), max(expenditures))*1.1]*len(expenditures), bar_width,
                alpha=0.0, color='r')

ax.set_xlabel('Agents in Auction')
ax.set_ylabel('Agent Expenditures and Utilities')
ax.set_title('Average Expenditures and Utilities by Agent')
ax.set_xticks((index + bar_width/2))
ax.set_xticklabels(('Truthful1', 'Truthful2', 'Truthful3', 'Truthful4', 'Truthful5'))
ax.legend()
# ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# ax.legend(bbox_to_anchor=(1, 1),
#            bbox_transform=plt.gcf().transFigure)

fig.tight_layout()
plt.show()
fig.savefig("GSP_Truthfuls_5_ExpsUtils.png")






