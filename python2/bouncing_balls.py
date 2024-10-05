import tkinter as tk
import random

# Create the Ball class
class Ball:
    def __init__(self, canvas, x, y, diameter, color):
        self.canvas = canvas
        self.diameter = diameter
        self.color = color
        self.id = canvas.create_oval(x, y, x + diameter, y + diameter, fill=color)
        self.dx = random.choice([-2, -1, 1, 2])  # Horizontal movement
        self.dy = random.choice([-2, -1, 1, 2])  # Vertical movement

    def move(self):
        coords = self.canvas.coords(self.id)
        if coords[0] <= 0 or coords[2] >= self.canvas.winfo_width():
            self.dx = -self.dx  # Reverse horizontal direction
        if coords[1] <= 0 or coords[3] >= self.canvas.winfo_height():
            self.dy = -self.dy  # Reverse vertical direction
        self.canvas.move(self.id, self.dx, self.dy)

# Create the main application window
def run_bouncing_balls():
    window = tk.Tk()
    window.title("Bouncing Balls")

    canvas = tk.Canvas(window, width=600, height=400, bg='white')
    canvas.pack()

    # Create multiple balls
    balls = [Ball(canvas, random.randint(0, 550), random.randint(0, 350), 
                  random.randint(30, 50), random.choice(['red', 'green', 'blue', 'yellow'])) for _ in range(10)]

    # Function to animate the balls
    def animate():
        for ball in balls:
            ball.move()
        window.after(20, animate)  # Adjust the speed

    animate()
    window.mainloop()

run_bouncing_balls()
