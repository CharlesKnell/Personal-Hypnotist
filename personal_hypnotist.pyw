import pygame
import math
import sys
from screeninfo import get_monitors
import os
from tkinter import Tk, filedialog


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


formulas_folder = resource_path("formulas")
print(f"formulas folder: {formulas_folder}")

# Initialize pygame
pygame.init()

# Screen dimensions
monitor = get_monitors()[0]  # Assuming you want the first monitor
WIDTH, HEIGHT = monitor.width, monitor.height

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Center of the screen
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Parameters for the spiral
spiral_lines = 100
line_length = 4
angle_step = 0.5
rotation_speed = 5  # Speed of rotation

# Open file selection dialog
Tk().withdraw()  # Hide the root Tkinter window
mp3_file = filedialog.askopenfilename(
    title="Select an MP3 file to play",
    filetypes=[("MP3 Files", "*.mp3")],
    initialdir=formulas_folder
)

if not mp3_file:
    print("No MP3 file selected. Exiting.")
    sys.exit(1)

pygame.mixer.init()
pygame.mixer.music.load(mp3_file)  # Replace with your MP3 file path
pygame.mixer.music.play()  # Play the MP3 file once
pygame.display.set_caption("Hypnotic Spiral")  # Reset the window caption

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Main loop
running = True
angle_offset = 0  # Keeps track of the rotation

while running:
    screen.fill(BLACK)  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Check if ESC key is pressed
                running = False

    # Draw the spiral
    for i in range(spiral_lines):
        angle = math.radians(10 * i * angle_step + angle_offset)
        x1 = CENTER_X + i * line_length * math.cos(angle)
        y1 = CENTER_Y + i * line_length * math.sin(angle)
        x2 = CENTER_X + (i + 1) * line_length * math.cos(angle)
        y2 = CENTER_Y + (i + 1) * line_length * math.sin(angle)

        pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)

    # Update the rotation
    angle_offset -= rotation_speed

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(25)

# Quit pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
