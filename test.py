import gym
import frc_gym

env = gym.make('FrcGraph2019-v1')
env2 = gym.make('Banana-v1')
<<<<<<< HEAD
=======
protoEnv = gym.make("Proto-v1")

# ProtoEnv Test
#   0 = HAB
#   1 = Player Station
#   2 = Rocket
#   3 = Cargo Ship

protoEnv.render()

#We start at the Hab, move to player station to pick up cargo
assert ((protoEnv.step(1)) == ([10, True], 0, False))
# ([currentTime, Carying Cargo], reward, done)

# Move to Score at the rocket ship
assert ((protoEnv.step(2)) == ([25, False], 3, False))

# Go Back to Player Station
assert ((protoEnv.step(1)) == ([40, True], 0, False))

# Go to Cargo Ship
assert ((protoEnv.step(3)) == ([60, False], 2, False))

# Go to Rocket
assert ((protoEnv.step(2)) == ([65, False], 0, False))

#Go to HAB
assert ((protoEnv.step(0)) == ([85, False], 0, False))

# Go To Player Station
assert ((protoEnv.step(1)) == ([95, True], 0, False))

#Go to HAB
assert ((protoEnv.step(0)) == ([105, True], 0, False))

# Go to Cargo Ship
assert ((protoEnv.step(3)) == ([120, False], 2, False))

# Go To Player Station
assert ((protoEnv.step(1)) == ([140, True], 0, False))

# Go To Rocket
assert ((protoEnv.step(2)) == ([150, True], 0, True))
>>>>>>> 05be9999f290ba00330468fa4653df37de04ad7d
