import matplotlib.pyplot as plt
import auction
import numpy as np
import sys


reserve = 0

["auction.py", "--loglevel", "debug", "--num-rounds", "48", "--perms", "1", "--iters", "200", "--reserve", str(reserve), "--seed", "2", "--mech=GSP", "AngelSlavBB,5"]

# results = list(map(auction.main, options))
results = []
for option in options:
	sys.argv = option
	results.append(auction.main(sys.argv))

resMeans = [r[0] for r in results]
resStds = [r[1] for r in results]

n_groups = len(options)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.75
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, resMeans, bar_width,
                alpha=opacity, color='b',
                yerr=resStds, error_kw=error_config,
                label='Mean')

ax.set_xlabel('Number of Agents')
ax.set_ylabel('Average Daily Revenue')
ax.set_title('Average Daily Revenues by Number of Agents')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(('5', '6', '7', '8', '9', '10'))
ax.legend()

fig.tight_layout()
plt.show()
fig.savefig("GSP_Truthfuls_5Thru10.png")






