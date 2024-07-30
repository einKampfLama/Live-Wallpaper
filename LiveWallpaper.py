import sys
import platform
import cv2


def mp4_to_frame(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1
    while success:
        success, image = vidObj.read()
        cv2.imwrite("frame%d.jpg" % count, image)
        count += 1

def set_wallpaper(image_path):
    system = platform.system()

    if system == "Windows":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    elif system == "Darwin":  # macOS
        import subprocess
        script = f'''
        tell application "System Events"
            set picture of current desktop to POSIX file "{image_path}"
        end tell
        '''
        subprocess.run(["osascript", "-e", script])
    elif system == "Linux":
        import subprocess
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{image_path}"])
    else:
        raise NotImplementedError(f"Das Ändern des Hintergrundbilds ist für {system} nicht implementiert.")


# das
def animate_wallpaper(frames):
    print()

def video_to_frames(vid):
    print()
