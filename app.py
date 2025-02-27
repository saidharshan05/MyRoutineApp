import tkinter as tk
from tkinter import ttk
from datetime import datetime
from routine import extract_salad_suggestions, select_salad, routine
from PIL import ImageGrab  # For screenshot
#import pywhatkit as kit  # To send messages via WhatsApp
import openai  # For fetching motivational messages

# OpenAI API setup
openai.api_key = "sk-ZkXdRvLqLkGx4C9l3wT1xUDlIdm4dwrVjJYQurpHpbT3BlbkFJEtIAiECskJDoTf9RjCZ_H_5-LJ7Rq34pdWbt06Ug8A"

# Load salad suggestions from PDF
pdf_path = "/home/dharshu-lappy/Projects/routine/files/Salads.pdf"
salads = extract_salad_suggestions(pdf_path)

# Track today's salad (only change once per day)
today_date = None
today_salad = None
current_salad = None  # Keep reference globally

# Function to mark task as completed
def toggle_task_completion(label, var):
    if var.get():
        label.config(font=("Helvetica", 14, "overstrike"))  # Strike through task
    else:
        label.config(font=("Helvetica", 14))  # Remove strike through

# Function to take a screenshot of the root window and save it
def take_screenshot():
    x0 = root.winfo_rootx()
    y0 = root.winfo_rooty()
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    screenshot = ImageGrab.grab(bbox=(x0, y0, x1, y1))
    screenshot.save("routine_screenshot.png")  # Save the screenshot

# Function to fetch a motivational message from OpenAI
def get_motivational_message():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or you can use 'gpt-4' if available
        messages=[
            {"role": "system", "content": "You are a motivational coach."},
            {"role": "user", "content": "Give me a short motivational message"}
        ],
        max_tokens=50
    )
    message = response['choices'][0]['message']['content'].strip()
    return message

# Function to send the screenshot and message via WhatsApp
#def send_screenshot_via_whatsapp():
    take_screenshot()  # Take a screenshot
    message = get_motivational_message()  # Get motivational message
    kit.sendwhats_image(
        phone_no="+918152847103",  # Replace with your WhatsApp number
        img_path="routine_screenshot.png",
        caption=message,
        wait_time=15
    )

# Create the main application window with full screen
root = tk.Tk()
root.title("Daily Routine Manager")
root.attributes('-fullscreen', True)  # Set the window to full screen
root.configure(bg="#0047AB")  # Set background to a workout-themed blue

# Exit fullscreen with Esc key
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# Style settings
font_title = ("Helvetica", 18, "bold")
font_text = ("Helvetica", 14)
button_style = {"font": ("Helvetica", 12), "bg": "#1E90FF", "fg": "white", "activebackground": "#4682B4", "activeforeground": "white"}

# Scrollable frame setup
canvas = tk.Canvas(root, bg="#0047AB")
scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#0047AB")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Salad label
salad_label = tk.Label(root, text="Today's salad:", font=font_title, fg="white", bg="#0047AB")
salad_label.pack(pady=10)

# Routine label
routine_label = tk.Label(scrollable_frame, text="Today's Routine:", font=font_title, fg="white", bg="#0047AB")
routine_label.pack(pady=10)

# Function to fetch and display today's routine with checkboxes
def update_routine():
    global current_salad
    for widget in canvas.winfo_children():
        if isinstance(widget, tk.Checkbutton) or isinstance(widget, tk.Label) and widget != current_salad:
            widget.destroy()  # Clear old routine entries, but not the salad label

    for task in routine:
        task_frame = tk.Frame(scrollable_frame, bg="#0047AB")
        task_frame.pack(padx=20)

        var = tk.BooleanVar()
        task_label = tk.Label(task_frame, text=f"{task['time']} - {task['task']}", font=font_text, fg="white", bg="#0047AB", anchor="w", justify="left")
        task_label.pack(side="left")
        checkbox = tk.Checkbutton(task_frame, variable=var, command=lambda l=task_label, v=var: toggle_task_completion(l, v), bg="#0047AB")
        checkbox.pack(side="right")

# Salad label (created only once)
if not current_salad:
    current_salad = tk.Label(root, text="No salad selected yet", font=font_text, fg="white", bg="#0047AB", wraplength=500, justify="left")
    current_salad.pack(pady=10)

# Function to select and display a salad for the day (only once per day)
def update_salad():
    global today_date, today_salad, current_salad
    current_date = datetime.now().strftime("%Y-%m-%d")
    if today_date != current_date:
        today_date = current_date
        today_salad = select_salad(salads).strip()
        current_salad.config(text=today_salad, wraplength=500, justify="left")
    else:
        current_salad.config(text=today_salad, wraplength=500, justify="left")

# Button to fetch today's salad
next_salad_button = tk.Button(root, text="Get Today's Salad", command=update_salad, **button_style)
next_salad_button.pack(pady=10)
mot = tk.Button(root, text="Get Today's Salad", command=get_motivational_message, **button_style)
mot.pack(pady=10)
# Button to send screenshot and motivational message via WhatsApp
#send_button = tk.Button(root, text="Send Screenshot & Message", command=send_screenshot_via_whatsapp, **button_style)
#send_button.pack(pady=10)

# Button to close the application
exit_button = tk.Button(root, text="Close", command=root.destroy, **button_style)
exit_button.pack(pady=10)

# Initialize by showing today's routine
update_routine()

# Start the GUI loop
root.mainloop()
