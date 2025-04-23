# Multi-Agentic Reinforcement Learning
# 
## Background
Studying emergent behaviors between intelligent agents in a 2D-grid environment


## Folder Structure
/MARL  
├── README.md  
├── requirements.txt  
├── custom-environment/  
│   ├── env/  
│   │   ├── base_env.py  
│   │   └── demo1_env.py  
│   └── custom-environment-v0.py  
├── demos/  
│   ├── demo1.py  
│   ├── demo2.py  
│   ├── q_learning_demo.py  
│   ├── random_learning_demo.py  
├── extras/  
│   ├── env_test.py  
├── .envrc  
├── .gitignore 

## Usage
To get started with this project, follow the steps below.

1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/james-bellanca/MARL.git
cd MARL
```

2. Install Dependencies
Create or activate a virtual environment - If you don't know how to do this stop here.

Once venv is activated, run: 
```bash
pip install -r requirements.txt
```


## Notes
- A 2D grid (e.g., 50x50 or 100x100) provides a clear, simple, yet expressive environment where behaviors can emerge over time. Its simplicity helps in isolating factors affecting agent strategies. Over the course of this project we can increase the complexity of the gridpath world to include things like barriers, varying cell values or partially observable states.

- Gridpath style environments were motivated due to implications for traffic control problems, involving controllable systems trying to reduce traffic congestion.


## Structure of Environments
- Cooperative vs. Competitive: The structure of this project is to examine the differences between cooperative and competitive learning styles in a multi-agent environment.
- For further variation, we break each of these categories down to compare factors such as additional environment complexity (e.g. obstacles, varying cell values), varying learning algorithms (e.g. Q-Learning, SARSA, Deep Learning), or agent interaction.


## Hypothesis?
- While this type of project doesn't necessarily normally have a hypothesis, prior to running any tests I would like to lay out some of my thoughts about what to expect from this project. Primarily, while intuition might tell you that the cooperative environments will finish exploring the grid in a more efficient way, I think it's interesting to consider the scenario that by making the agents competitive, it could lead to "unknowing cooperation" by the agents still reaching the goal of exploring the whole grid through competition, and that this solution could potentially be more efficient. 


## Refs
- https://pettingzoo.farama.org/
- https://www.kc-ml2.com/posts/blog_MARL#4-multi-agent-grid-world-environments
