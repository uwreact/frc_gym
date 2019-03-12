from gym.envs.registration import register

register(
    id='FrcGraph2019-v1',
    entry_point='frc_gym.envs:GraphEnv',
)
register(
    id='Banana-v1',
    entry_point='frc_gym.envs:BananaEnv',
)
