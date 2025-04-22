import numpy as np
import matplotlib.pyplot as plt
import random

# 1) Parameters
grid_size = 10
steps     = 50
pause     = 0.2

# 2) State
# 0 = unvisited, 1 = visited by A1, 2 = visited by A2
grid = np.zeros((grid_size, grid_size), dtype=int)
agent_pos = {
    'A1': [2, 2],
    'A2': [7, 7],
}

# 3) Set up plot
fig, ax = plt.subplots(figsize=(5,5))
im = ax.imshow(grid, cmap='tab20', vmin=0, vmax=2, interpolation='none')

ax.set_xticks(np.arange(grid_size+1)-0.5, minor=True)
ax.set_yticks(np.arange(grid_size+1)-0.5, minor=True)
ax.grid(which='minor', color='black', linewidth=1)
ax.tick_params(which='both', bottom=False, left=False,
               labelbottom=False, labelleft=False)

# valid variable names for the scatter plots:
scatter_A1 = ax.scatter(agent_pos['A1'][1], agent_pos['A1'][0],
                        c='red',   s=100, edgecolors='black', label='A1')
scatter_A2 = ax.scatter(agent_pos['A2'][1], agent_pos['A2'][0],
                        c='blue',  s=100, edgecolors='black', label='A2')

plt.ion()
plt.show()

# 4) Animation loop
for _ in range(steps):
    for idx, (name, pos) in enumerate(agent_pos.items(), start=1):
        # Random move
        dr, dc = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        pos[0] = np.clip(pos[0] + dr, 0, grid_size-1)
        pos[1] = np.clip(pos[1] + dc, 0, grid_size-1)
        # Mark visited
        grid[pos[0], pos[1]] = idx

    # Redraw
    im.set_data(grid)
    scatter_A1.set_offsets((agent_pos['A1'][1], agent_pos['A1'][0]))
    scatter_A2.set_offsets((agent_pos['A2'][1], agent_pos['A2'][0]))

    fig.canvas.draw()
    plt.pause(pause)

plt.ioff()
plt.show()