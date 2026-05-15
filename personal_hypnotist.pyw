import os
import sys
from tkinter import filedialog
import pygame
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.backend_bases import KeyEvent

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

matplotlib.use('TkAgg')

# Spiral parameters
a = 0
b = 0.0005
theta = np.linspace(0, 8 * np.pi, 2000) #2nd arg controls how tight
r = a + b * theta
x = r * np.cos(theta) * 0.2
y = r * np.sin(theta) * 0.2

# Set up the figure and axes
fig = plt.figure(facecolor='black')

def on_key(event: KeyEvent):
    if event.key == 'escape':
        pygame.mixer.music.stop()
        pygame.quit()
        plt.close(event.canvas.figure)
    elif event.key == ' ':                          # ← NEW
        if pygame.mixer.music.get_busy():           # ← NEW
            pygame.mixer.music.pause()              # ← NEW (toggle pause)
        else:                                       # ← NEW
            pygame.mixer.music.unpause()

fig.canvas.manager.toolbar.pack_forget() # ignore this error
fig.canvas.mpl_connect('key_press_event', on_key) # ignore this error

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()  # TkAgg or compatible backends

ax = fig.add_subplot(111)
ax.set_facecolor('black')
max_r = float(np.max(r)) # controls the size of the spiral
ax.set_xlim(-0.9 * max_r, 0.9 * max_r)
ax.set_ylim(-0.5 * max_r, 0.5 * max_r)

ax.set_xticks([])
ax.set_yticks([])

# Create a single line object for the spiral
line, = ax.plot(x, y, color='white', linewidth=2)

# Update function for animation
def update(frame):
    angle = -np.radians(frame)
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    x_rot = x * cos_a - y * sin_a
    y_rot = x * sin_a + y * cos_a
    line.set_data(x_rot, y_rot)
    return line,


# Animate
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 5),
 interval=25, repeat=True) # 3rd arg of np.arrange is the rotate step

formulas_folder = resource_path("formulas")
print(f"formulas folder: {formulas_folder}")

mp3_file = filedialog.askopenfilename(
    title="Select an MP3 file to play",
    filetypes=[("MP3 Files", "*.mp3")],
    initialdir=formulas_folder
)

if not mp3_file:
    print("No MP3 file selected. Exiting.")
    sys.exit(1)

pygame.mixer.init()
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.play()

plt.show()
