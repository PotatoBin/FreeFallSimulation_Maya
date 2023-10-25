# Physics Simulation in Maya

This project is a physics simulation in Autodesk Maya that simulates the motion of an object in free fall and subsequent vertical upward movement, considering gravitational effects and restitution.

## Overview

This Python script uses the Autodesk Maya Python API (`maya.cmds`) to create a physics simulation. The simulation consists of two parts:
1. **Free Fall**: An object is released from a certain height with an initial downward velocity. It falls under the influence of gravity until it reaches the ground. The object may bounce with reduced velocity due to the restitution coefficient.
2. **Vertical Upward Movement**: After reaching the ground, the object moves upward again, simulating a bounce. This process can repeat up to 10 times.

## Parameters

- `initial_height`: Initial height from which the object is dropped (in meters).
- `initial_velocity`: Initial downward velocity of the object (in meters per second).
- `gravity`: Acceleration due to gravity (in meters per second squared).
- `restitution_coefficient`: Coefficient of restitution (a measure of bounciness).
- `fps`: Frames per second, used to calculate the animation.

## Usage

1. Ensure you have Autodesk Maya installed and configured.
2. Copy and paste the provided Python script into a Maya Python script editor.
3. Execute the script to run the simulation.

The script will animate the object's motion in Maya. The `posY` list will store the object's height at each frame. The simulation will take into account both free fall and vertical upward movement.

## Example

To visualize the simulation, you can create an object (e.g., a sphere) in Autodesk Maya and link it to the script's animation. For example, you can set keyframes on the object's translateY attribute using `cmds.setKeyframe`.

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute it for your projects.

We hope you find this physics simulation script useful for your Maya projects. Please let us know if you have any questions or suggestions!
