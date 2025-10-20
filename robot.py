import numpy as np
from roboticstoolbox import RevoluteDH
import roboticstoolbox as rtb

robot = rtb.models.Panda()
print(robot)


lengths = [0.07, 0.36, 0.445]

robot = rtb.DHRobot(
    [  # Z axis is upwards
        RevoluteDH(d=0.352, alpha=-np.pi/2, a=lengths[0]),
        RevoluteDH(d=0, alpha=0, a=lengths[1], offset=-np.pi/2),
        RevoluteDH(d=0, alpha=np.pi/2, a=lengths[2], offset=np.pi/2),
    ], name="Minimized ABB 140"
)
print(robot)
