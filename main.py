# Standard library
import cv2 
import pyautogui
import numpy as np

# Third-party
import os
from pathlib import Path

# Save location 
out_dir = Path.home() / "Desktop"
out_dir.mkdir(exist_ok=True) 

# Specify name of output file

filename = "Screen Recording.avi"
full_path = out_dir / filename

# Specify resolution

resolution = (1920, 1080)

# Specify video codec (codec: software that compresses and decompresses video data)

codec = cv2.VideoWriter_fourcc(*"XVID") # four char code XVID = .avi file

# cv2.VideoWriter is created with filename, codec, fps, and res. 

# It saves frames into a single video file.

# Specify frame rate... can choose any value

fps = 60.0

# Creat a VideoWriter object *This saves frames as a video file*

out = cv2.VideoWriter(str(full_path), codec, fps, resolution)

# Create an Empty window to display the recording in real-time
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert your photo from BGR to RGB

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    out.write(frame)

    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()


