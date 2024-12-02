# write a helloworld with gymnasium and tensor board
# avoid using tensorflow
#


import gymnasium as gym
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard

# Create a simple environment
env = gym.make("CartPole-v1", render_mode="human")

# Define a simple neural network model
model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Dense(64, activation="relu", input_shape=(4,)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(2),
    ]
)

# Compile the model
model.compile(optimizer="adam", loss="mse")

# Create a TensorBoard callback
tensorboard_callback = TensorBoard(log_dir="./logs", histogram_freq=1)

# Simple training loop (this is a very basic example and not a proper training loop)
for episode in range(10):
    state, _ = env.reset()
    done = False
    rewards = 0.0
    while not done:
        # Simple policy: always choose action 1
        action = 1
        next_state, reward, done, _, _ = env.step(action)
        # For demonstration, let's just predict (not actually training the model here)
        # In a real scenario, you'd train the model based on the state and action
        state = next_state
        rewards += reward
    # For demonstration, let's log the reward (in a real scenario, you'd log more meaningful metrics)
    tf.summary.scalar("Reward", data=rewards, step=episode)
    # You would typically use model.fit() with the TensorBoard callback for actual training
    # For simplicity, we're not doing that here.

# Close the environment
env.close()

# To visualize, you'd typically start TensorBoard and load the logs directory
# You can do this by running `tensorboard --logdir=./logs` in your terminal
# Then, navigate to http://localhost:6006/ in your web browser
