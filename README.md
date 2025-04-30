# Multi-Agentic Reinforcement Learning

## Background
This multi-agent reinforcement learning (MARL) project aims to explore cooperative learning in 
a 2-D grid environment, researching how varying agent observation ranges and communication protocols affect cooperative and competitive behaviors across increasing complexity in grid-world multi-agent reinforcement learning environments.


## Folder Structure

- **MARL**
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
- `notebooks/`
    - `notebook_v0.py`
    - `notebook_v1.py`
- `.envrc`
- `.gitignore`


## Notes
- A 2D grid (e.g., 50x50 or 100x100) provides a clear, simple, yet expressive environment where behaviors can emerge over time. Its simplicity helps in isolating factors affecting agent strategies. Over the course of this project we can increase the complexity of the gridpath world to include things like barriers, varying cell values or partially observable states.

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


## Refs
- https://pettingzoo.farama.org/
- https://www.kc-ml2.com/posts/blog_MARL#4-multi-agent-grid-world-environments
- https://proceedings.mlr.press/v139/liu21j/liu21j.pdf?utm_source=chatgpt.com
