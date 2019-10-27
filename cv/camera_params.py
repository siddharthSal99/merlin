import subprocess

def set_camera_params():
    output = subprocess.run(["bash", "cv/set_camera_params.sh"], capture_output=True)
    # print(output)
