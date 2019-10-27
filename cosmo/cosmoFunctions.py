from messages import Pose2D
import cozmo
import asyncio
import math



async def moveToLoc(curr_loc: Pose2D, goal_loc: Pose2D,robot: cozmo.robot.Robot):
    x_rel = goal_loc.x - curr_loc.x
    y_rel = goal_loc.y - curr_loc.y
    theta_rel = goal_loc.theta - curr_loc.theta
    newPose = cozmo.util.Pose(x_rel,
        y_rel,
        0,
        angle_z =cozmo.util.Angle(radians = theta_rel))
    await robot.go_to_pose(newPose,relative_to_robot=True).wait_for_completed()

def getInitialTurnAngleRadians(curr_loc: Pose2D, goal_loc: Pose2D):
    currHeading = curr_loc.theta
    x_rel = goal_loc.x - curr_loc.x
    y_rel = goal_loc.y - curr_loc.y
    globalAng = math.atan2(y_rel,x_rel)
    return globalAng - currHeading

async def initialTurn(curr_loc: Pose2D, goal_loc: Pose2D,robot: cozmo.robot.Robot):
    turnAng = getInitialTurnAngleRadians(curr_loc, goal_loc)
    await robot.turn_in_place(cozmo.util.radians(turnAng), in_parallel = True).wait_for_completed()


def getDriveDistanceMM(curr_loc: Pose2D, goal_loc: Pose2D):
    x_rel = goal_loc.x - curr_loc.x
    y_rel = goal_loc.y - curr_loc.y
    dist = math.sqrt(x_rel**2 + y_rel**2)
    return dist

async def driveFwd(curr_loc: Pose2D, goal_loc: Pose2D,robot: cozmo.robot.Robot):
    dist = getDriveDistanceMM(curr_loc,goal_loc)
    speed = cozmo.util.speed_mmps(70)
    await robot.drive_straight(cozmo.util.distance_mm(dist),speed, in_parallel = True).wait_for_completed()


def getFinalTurnAngleRadians(curr_loc: Pose2D, goal_loc: Pose2D):
    x_rel = goal_loc.x - curr_loc.x
    y_rel = goal_loc.y - curr_loc.y
    globalAng = math.atan2(y_rel,x_rel)
    finalAng = goal_loc.theta
    return finalAng - globalAng

async def finalTurn(curr_loc: Pose2D, goal_loc: Pose2D,robot: cozmo.robot.Robot):
    turnAng = getFinalTurnAngleRadians(curr_loc,goal_loc)
    await robot.turn_in_place(cozmo.util.radians(turnAng), in_parallel = True).wait_for_completed()





