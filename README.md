
# frc_gym

OpenAI Gym environment enabling FRC teams to train their robots

## Installation:
1. Clone the envrionment 
`git clone https://github.com/uwreact/frc_gym.git`
`cd frc_gym`
2. Install using pip
`pip insatll -e .`

## Environments
### Graph

#### States:
##### Hab:
0) Middle of HAB (Starting locaiton)  
1) Hab Level 2 (Near side)  
2) Hab Level 2 (Far side)  
3) Hab Level 3   

##### Player Station:
4) Player Station get Hatch (Near Side)  
5) Player Station get Cargo (Near Side)  
6) Player Station get Hatch (Far Side)  
7) Player Station get Cargo (Far Side)  

![Rocket Ship Image](https://user-images.githubusercontent.com/5326007/55272448-1f87ec00-527a-11e9-8c72-78585c17248b.png)

#### Rocket Far Side:
8) Rocket Postion 0 Score Hatch (Far Side) 
9)  Rocket Level 1 Score Cargo (Far Side)     
10) Rocket Position 1 Score Hatch (Far Side)    
11) Rocket Position 2 Score Hatch (Far Side)  
12) Rocket Level 2 Score Cargo (Far Side)  
13) Rocket Postion 3 Score Hatch (Far Side)  
14) Rocket Position 4 Score Hatch (Far Side)  
15) Rocket Level 3 Score Cargo (Far Side)  
16) Rocket Position 5 Score Hatch (Far Side)  

#### Rocket Near Side:
17) Rocket Postion 0 Score Hatch (Near Side) 
18) Rocket Level 1 Score Cargo (Near Side)     
19) Rocket Position 1 Score Hatch (Near Side)    
20) Rocket Position 2 Score Hatch (Near Side)  
21) Rocket Level 2 Score Cargo (Near Side)  
22) Rocket Postion 3 Score Hatch (Near Side)  
23) Rocket Position 4 Score Hatch (Near Side)  
24) Rocket Level 3 Score Cargo (Near Side)  
25) Rocket Position 5 Score Hatch (Near Side)  


![Cargo Ship Image](https://user-images.githubusercontent.com/5326007/54975224-a0ca4080-4f53-11e9-9511-1f22c610d629.png)

#### Cargo Ship:
26) Cargo Ship 0 Score Hatch  
27) Cargo Ship 0 Score Cargo  
28) Cargo Ship 1 Score Hatch  
29) Cargo Ship 1 Score Cargo  
30) Cargo Ship 2 Score Hatch  
31) Cargo Ship 2 Score Cargo  
32) Cargo Ship 3 Score Hatch  
33) Cargo Ship 3 Score Cargo  
34) Cargo Ship 4 Score Hatch  
35) Cargo Ship 4 Score Cargo  
36) Cargo Ship 5 Score Hatch  
37) Cargo Ship 5 Score Cargo  
38) Cargo Ship 6 Score Hatch  
39) Cargo Ship 6 Score Cargo  
40) Cargo Ship 7 Score Hatch  
41) Cargo Ship 7 Score Cargo  

### Banana Gym
Initial testing environment based on[Banna Gym](https://github.com/MartinThoma/banana-gym). You are selling bananas one at a time, which spoil within a period of 3 days. The probability that you will sell the banana is given by:
![Alt Text](https://latex.codecogs.com/gif.latex?%24%24p%28x%29%20%3D%5Cfrac%7B1&plus;e%7D%7B%201%20&plus;%20e%5E%7B%28x&plus;1%29%7D%7D%24%24)
Where x-1 is your profit, which is your reward. If you don’t sell the banana, then your reward is -1 (the price of the banana).

## Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/). To make development easy, we provide configuration files for standard linting and static analysis tools such as [yapf](https://github.com/google/yapf).

## Contributing

We facilitate a completely open source environment for all of our projects, and are always welcoming contributors.

### Contributing Guide

Before opening your editor, read this project's [contributing guide](CONTRIBUTING.md) to learn about its development and contribution process.

### License

The `frc_gym` project is [BSD 3-Clause licensed](LICENSE).
