import warnings
import numpy as np
import sys
import os
import ctypes
import tkinter as tk
from tkinter import filedialog

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import pygame

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def main():
    formulas_folder = resource_path("formulas")
    print(f"formulas folder: {formulas_folder}")

    root = tk.Tk()
    root.withdraw()
    mp3_file = filedialog.askopenfilename(
        title="Select an MP3 file to play",
        filetypes=[("MP3 Files", "*.mp3")],
        initialdir=formulas_folder
    )
    root.destroy()

    if not mp3_file:
        print("No MP3 file selected. Exiting.")
        sys.exit(1)

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    width, height = screen.get_size()
    pygame.display.set_caption("Hypnotic Spiral")
    ctypes.windll.user32.SetForegroundWindow(pygame.display.get_wm_info()['window'])
    clock = pygame.time.Clock()

    cx, cy = width // 2, height // 2
    x = np.arange(width) - cx
    y = np.arange(height) - cy
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2)
    theta = np.arctan2(Y, X)

    max_r = np.sqrt(cx**2 + cy**2)
    num_bands = 8

    # lower exponent = narrower center bands, wider outer bands
    exp = 0.38
    r_norm = ((r ** exp) * num_bands / (max_r ** exp)).astype(np.float32)
    theta_norm = (theta / (2 * np.pi)).astype(np.float32)
    # precompute static difference — only rot_norm changes each frame
    base = r_norm - theta_norm

    surf = pygame.Surface((width, height))
    rotation = 0.0
    speed = -120.0  # degrees per second; negative reverses direction

    clock.tick()  # seed the clock before the loop
    running = True
    while running:
        dt = clock.tick(60) / 1000  # seconds elapsed since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    running = False
                elif event.key == pygame.K_LEFT:
                    speed -= 30.0
                elif event.key == pygame.K_RIGHT:
                    speed += 30.0
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer.music.unpause()

        rot_norm = np.float32(rotation / 360.0)
        spiral_val = (base + rot_norm) % np.float32(1.0)
        # Transpose because pygame surfarray uses (x, y) ordering
        mask = (spiral_val < 0.5).T

        pixel_array = pygame.surfarray.pixels3d(surf)
        val = np.where(mask, 255, 0).astype(np.uint8)
        pixel_array[:, :, 0] = val
        pixel_array[:, :, 1] = val
        pixel_array[:, :, 2] = val
        del pixel_array

        screen.blit(surf, (0, 0))
        pygame.display.flip()

        rotation = (rotation + speed * dt) % 360

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
