from gym.envs.registration import register

register(
    id='FRCGraph2019-v1',
    entry_point='frc_gym.envs:GraphEnv',
)
