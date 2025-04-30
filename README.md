# Multi-Agentic Reinforcement Learning

## Background
This multi-agent reinforcement learning (MARL) project aims to explore cooperative learning in 
a 2-D grid environment, researching how varying agent observation ranges and communication protocols affect cooperative and competitive behaviors across increasing complexity in grid-world multi-agent reinforcement learning environments.


## Table of Contents
- [Background](#background)
- [Folder Structure](#folder-structure)
- [Notes](#notes)
- [Usage](#usage)
- [References](#references)

## Folder Structure
**MARL**
- `README.md`
- `requirements.txt`
- `custom-environment/`
    - `env/`
        - `base_env.py`
    - `custom-environment-v0.py`
- `demos/`
    - `demo2.py`
    - `q_learning_demo.py`
    - `random_learning_demo.py`
- `experiments/`
    - `partial_obs_q_train.py`
- `extras/`
    - `env_test.py`
- `base_notebooks/`
    - `notebook_v0.py`
    - `notebook_v1.py`
- `scripts/`
    - `sweep_radius_experiments.sh`
- `.envrc`
- `.gitignore`


## Notes
- **1. Introduction**
    - A 2D grid (e.g., 50x50 or 100x100) provides a clear, simple, yet expressive environment where behaviors can emerge over time. Its simplicity helps in isolating factors affecting agent strategies. Over the course of this project we can increase the complexity of the gridpath world to include things like barriers, varying cell values or partially observable states.
    
- **2. Base Environment**
    - The first environment we use is a PettingZoo Parallel environment called GridExplorationMaskedEnvironment. This is the most basic environment we work with, containing no obstacles or complexity. The folder base_notebooks/ contains .ipynb files containing plots and graphs describing specific instances of agentic learning in this environment.
    - Using this environment we first test varying the observation radius of the agents.  "Seeing" is defined for agents as a square of size (2r+1): so r=1→3×3, r=0→1×1, and r='full'→the entire grid. [Notebook0](base_notebooks/notebook_v0.ipynb) and  [Notebook1](base_notebooks/notebook_v1.ipynb) investigate some basic experimenting with each agent. For a more holistic look at how this variation affects learning, we use a larger dataset over more parameters. For this, we run 4 levels of observation - (full, r=0, r=1, r=2) - across 2 grid sizes, 25x25 and 50x50, partnered with the max steps parameter defined by: area, area*2 and area*4. This means for a 25x25 grid we have max steps 625, 1250, and 2500, and for a 50x50 grid we have 2500, 5000, and 10000 max steps. Then we have (4 radii * 2 sizes * 3 max steps) = 24 csv files that we can agregate into one dataframe and plot to interpret. This is found in [Notebook2](base_notebooks/notebook_v2.ipynb). 

- **3. Obstructed Environment**

- **4. Deeper Techniques**

- **5. Implications**
    This project explores how agents with different sensing ranges and communication budgets cooperate to map unknown environments. Insights from these experiments can inform:
    - **Search & Rescue Robotics**: Designing multi-robot teams that share only critical information when bandwidth is limited and operate safely around dynamic obstacles (e.g. debris, moving victims).  
    - **Environmental Sensor Networks**: Developing energy-aware protocols where battery-powered sensors decide when to transmit readings vs. conserve power, improving long-term monitoring of wildlife, pollution, or agricultural conditions.  
    - **Smart Infrastructure & IoT**: Coordinating distributed controllers in buildings, power grids, or traffic systems so they maintain performance under partial observability and intermittent connectivity.  
    - **Human Teamwork Models**: Providing a quantitative framework for how information bottlenecks affect collective decision-making in emergency response, air-traffic control, or distributed software teams.


## Usage
To get started with this project, follow the steps below.

1. Clone the Repository
   
First, clone the repository to your local machine:

```bash
git clone https://github.com/james-bellanca/MARL.git
cd MARL/
```

2. Install Dependencies

Create or activate a virtual environment - If you don't know how to do this stop here.

Once venv is activated, run: 
```bash
pip install -r requirements.txt
```

3. Demos

- Animated Demo
```bash
python demos/demo2.py
```

- Q-Learning and Random Learning in Terminal
```bash
python -m demos.q_learning_demo
python -m demos.random_learning_demo
```

4. Running Scripts





## References
- https://pettingzoo.farama.org/
- https://www.kc-ml2.com/posts/blog_MARL#4-multi-agent-grid-world-environments
- https://proceedings.mlr.press/v139/liu21j/liu21j.pdf?utm_source=chatgpt.com
