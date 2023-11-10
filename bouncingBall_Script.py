import maya.cmds as cmds

initial_height = 1
initial_velocity = 0
gravity = 9.806
restitution_coefficient = 0.8
fps = 24
bouncing = 10
posY = []

def freeFall () :
    current_height = initial_height
    current_velocity = initial_velocity
    time = 0
    while current_height >= 0:
        posY.append(current_height)
        current_height = initial_height + initial_velocity * time- 0.5 * gravity * time * time
        current_velocity = initial_velocity - gravity * time
        time += 1/fps
    return verticalUpward (current_velocity, 1)

def verticalUpward (current_velocity, bouncing):
    if (bouncing >= 10) : return
    time = 0
    current_height = 0
    initial_velocity = -1 * current_velocity * restitution_coefficient
    current_velocity = initial_velocity
    while current_height >= 0:
        posY.append(current_height)
        current_height = initial_velocity * time - 0.5 * gravity * time * time
        current_velocity = initial_velocity - gravity * time
        time += 1/fps
    return verticalUpward(current_velocity, bouncing+1)

freeFall ()

for i in range (len(posY)):
    cmds.setKeyframe('all_CON.translateY', value=posY[i], time=i)
