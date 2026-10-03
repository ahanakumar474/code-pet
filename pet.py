import tkinter as tk

class DesktopPet:
    def __init__(self):
        self.root = tk.Tk()

        # Window configuration for a floating, borderless widget
        self.root.overrideredirect(True)          # Remove title bar and borders
        self.root.wm_attributes("-topmost", True)  # Keep on top of all windows
        self.root.config(bg='magenta')            # Set background color
        self.root.wm_attributes("-transparentcolor", 'magenta') # Transparent background

        # Pet states / emotions
        self.emotes = ["(=^ ◡ ^=)", "(づ ◕‿◕ )づ", "(★ω★)", "(=^･ω･^=)"]
        self.current_emote = 0

        # Pet display label
        self.label = tk.Label(
            self.root, 
            text=self.emotes[self.current_emote], 
            font=('Segoe UI Emoji', 24), 
            bg='magenta', 
            fg='#D97706'
        )
        self.label.pack()

        # Bind click and drag events
        self.label.bind("<Button-1>", self.on_click)
        self.label.bind("<B1-Motion>", self.drag)
        self.label.bind("<ButtonPress-1>", self.start_drag)

        # Place initial window near bottom right
        self.root.geometry("+1000+600")

    def on_click(self, event):
        self.current_emote = (self.current_emote + 1) % len(self.emotes)
        self.label.config(text=self.emotes[self.current_emote])

    def start_drag(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def drag(self, event):
        x = self.root.winfo_pointerx() - self.offset_x
        y = self.root.winfo_pointery() - self.offset_y
        self.root.geometry(f"+{x}+{y}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    pet = DesktopPet()
    pet.run()
