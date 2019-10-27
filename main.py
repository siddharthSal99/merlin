import cozmo
# from cv import transform
from messages.Pose2D import Pose2D
from cosmo.cosmoFunctions import moveToLoc
from cosmo.cosmoFunctions import initialTurn
from cosmo.cosmoFunctions import driveFwd
from cosmo.cosmoFunctions import finalTurn
import asyncio
import threading


async def run(robot: cozmo.robot.Robot):
    #calibrate camers
    #locate finger
    #pose  = transform to robot pose

    cp = Pose2D(0,0,0) #initialize pose to (0,0,0) wherever you start
    np = Pose2D(200,200,0.57)
    await initialTurn(cp,np,robot)
    await driveFwd(cp,np,robot)
    await finalTurn(cp,np,robot)





class CozmoThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, daemon=False)

    def run(self):
        cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger
        cozmo.run_program(run, use_viewer=False)

    def move(self):
        cozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on his charger
        cozmo.run_program(move, use_viewer=False)

if __name__ == "__main__":
        # cozmo thread
    cozmo_thread = CozmoThread()
    # cozmo_thread2 = CozmoThread()
    cozmo_thread.start()

    cozmo_thread.run()
