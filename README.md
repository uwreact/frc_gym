
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
Environment for training robots based on the 2019 FRC Game. Coming soon!

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
