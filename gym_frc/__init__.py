from gym.envs.registration import register

register(
    id='Graph-v2019',
    entry_point='gym_frc.envs:GraphEnv',
)
