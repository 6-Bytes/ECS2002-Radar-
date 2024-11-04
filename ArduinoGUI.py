import tkinter as tk
from tkinter import ttk
import random  # To simulate sensor data
import time
from threading import Thread

class SensorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sensor Distance Monitor")
        self.root.geometry("400x300")

        # Labels to show sensor data
        self.sensor1_label = ttk.Label(self.root, text="Sensor 1: -- cm", font=("Arial", 14))
        self.sensor1_label.pack(pady=10)

        self.sensor2_label = ttk.Label(self.root, text="Sensor 2: -- cm", font=("Arial", 14))
        self.sensor2_label.pack(pady=10)

        # Start data update in a background thread
        self.update_thread = Thread(target=self.update_sensor_data, daemon=True)
        self.update_thread.start()

    def update_sensor_data(self):
        while True:
            # Replace these with actual sensor readings if available
            sensor1_data = random.uniform(1, 2000)  # Simulate sensor data in the range 1 to 2000 cm
            sensor2_data = random.uniform(1, 2000)

            # Update the label text with new sensor data
            self.sensor1_label.config(text=f"Sensor 1: {sensor1_data:.2f} cm")
            self.sensor2_label.config(text=f"Sensor 2: {sensor2_data:.2f} cm")

            # Wait a bit before next update
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    gui = SensorGUI(root)
    root.mainloop()
