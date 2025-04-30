# Multi-Agentic Reinforcement Learning
# 
## Background
This multi-agent reinforcement learning (MARL) project aims to explore cooperative learning in 
a 2-D grid environment, researching how varying agent observation ranges and communication protocols affect cooperative and competitive behaviors across increasing complexity in grid-world multi-agent reinforcement learning environments.


## Folder Structure Test
1. Option 1

```mermaid
graph TD
  A[MARL]
  A --> B[README.md]
  A --> C[requirements.txt]
  A --> D[custom-environment/]
  D --> E[env/]
  E --> F[base_env.py]
  E --> G[demo1_env.py]
  D --> H[custom-environment-v0.py]
  A --> I[demos/]
  I --> J[demo1.py]
  I --> K[demo2.py]
  I --> L[q_learning_demo.py]
  I --> M[random_learning_demo.py]
  A --> N[extras/]
  N --> O[env_test.py]
  A --> P[.envrc]
  A --> Q[.gitignore]
  ```

  2. Option 2
  - **MARL**
  - `README.md`
  - `requirements.txt`
  - `custom-environment/`
    - `env/`
      - `base_env.py`
      - `demo1_env.py`
    - `custom-environment-v0.py`
  - `demos/`
    - `demo1.py`
    - `demo2.py`
    - `q_learning_demo.py`
    - `random_learning_demo.py`
  - `extras/`
    - `env_test.py`
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
