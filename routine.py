#import fitz   
import pymupdf
import random
import time
from datetime import datetime, timedelta

# Define your routine tasks and times
routine = [
    {"task": "Wake up", "time": "06:30"},
    {"task": "Walk the dog", "time": "06:45", "duration": 30},
    {"task": "Get nephews ready", "time": "07:50", "duration": 30},
    {"task": "Start yoga", "time": "08:25", "duration": 50},
]

# Track the last 5 salads to avoid repetition
last_salads = []

# Function to display the current task
def display_current_task(current_time):
    for item in routine:
        if current_time == item["time"]:
            return f"Time for: {item['task']}"
    return "No task at the moment"

# Function to extract salad suggestions from PDF
def extract_salad_suggestions(pdf_path):
    doc = pymupdf.open(pdf_path)
    salad_list = []
    for page_num in range(3, 17):
        page = doc.load_page(page_num)
        text = page.get_text("text")#.strip()  # Get text and remove any leading/trailing whitespace

        # Since each page contains one salad, append the entire text of the page
        if text:
            salad_list.append(text)

    # Debug: Print the extracted salads to verify
    print(f"Extracted salads: {salad_list}")
    return salad_list



# Function to select a salad with no repetition in the last 5 days
def select_salad(salads):
    available_salads = [salad for salad in salads if salad not in last_salads]
    
    if not available_salads:
        last_salads.clear()  # Reset history if all salads have been used
        available_salads = salads.copy()
    
    selected_salad = random.choice(available_salads)
    last_salads.append(selected_salad)
    
    if len(last_salads) > 5:
        last_salads.pop(0)  # Ensure only the last 5 salads are tracked
    
    return selected_salad

# Example usage
pdf_path = "/home/dharshu-lappy/Projects/routine/files/Salads.pdf"
salads = extract_salad_suggestions(pdf_path)

if __name__ == "__main__":
    current_time = datetime.now().strftime("%H:%M")
    print(display_current_task(current_time))
    print("Today's Salad Suggestion:", select_salad(salads))
