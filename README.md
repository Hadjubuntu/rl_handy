## Why RL-Handy

HANDY (Humand and Nature dynamics) is a simple scientific model to simulate interaction between human and nature. It has been developed by NASA in 2014 and has been released in Nature journal (The article: https://www.sciencedirect.com/science/article/pii/S0921800914000615)

The purpose of HANDY is to experiment long-term sustainable condition in a very simple Earth model environment.
Human and Nature interacts in prey-predator model. The original papers demonstrated than multiple societes were able to reach equilibrum.

In this project, we use Reinforcement Learning to guide society with the long-term objective to be sustainable. The results shall be impacted by the long-term factor (gamma factor) used to determine the long-term rewards.

**Note: Don't transfer conclusions to the real world, the only puropose of this project is just experimentation and fun !**

## Getting started

### Install RL-Handy

First, create a virtualenv:  
```bash
python3.x -m venv ~/.virtualenvs/rlhandy/ 
# or: virtualenv ~/.virtualenvs/rlhandy/ -p python3
source ~/.virtualenvs/rlhandy/bin/activate
```
And then, install project dependancies:  
```bash
make install
```

### First execution  

To enjoy a pre-computed model you can just:

```bash
```


## Thanks

Thanks to Esben S. Nielsen, I was able to use its open-source HANDY model written in Python (https://github.com/storpipfugl/pyhandy). Project has been forked in this repository to ease standalone installation.
I also thanks the HANDY model authors.