import tkinter as tk
from PIL import Image, ImageTk
import pygame

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('just-do-it-sound-effect.mp3')
    pygame.mixer.music.play()

def show_gif(root):
    gif = Image.open('just_do_it.gif')
    frames = [ImageTk.PhotoImage(gif.copy().convert('RGBA')) for frame in range(gif.n_frames)]

    label = tk.Label(root)
    label.pack()

    def update_frame(frame_index):
        frame = frames[frame_index]
        label.configure(image=frame)
        frame_index += 1
        if frame_index == len(frames):
            frame_index = 0
        root.after(50, update_frame, frame_index)

    update_frame(0)

def on_key_press(event):
    if event.char == 'p':
        print("Playing sound and showing GIF")
        play_sound()
        show_gif(event.widget)

def main():
    root = tk.Tk()
    root.geometry("200x100")
    root.bind("<Key>", on_key_press)
    
    label = tk.Label(root, text="Press 'P' to play sound and show GIF")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
