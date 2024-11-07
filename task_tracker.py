import json #read and write from json files
import os   # check if json files exist
from datetime import datetime  #to track and update the timestamp for each task
import sys    #allows the users to interact with CLI

# This is where we store all our precious tasks — a JSON file named "tasks.json"
TASK_FILE = "tasks.json"

def load_tasks():
    #if the file doesn't exists, we make an empty one so we don't freak out later on
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f) #just an empty list of tasks
    #open the file to load the tasks
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    #Putting all of our tasks in the file, formatted as json file
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4) #indented by 4 spaces to make it more readable

def add_task(description):
    tasks = load_tasks() #load the existing tasks
    new_task= {
        "id": len(tasks) + 1,  # Assign a new ID — first come, first served
        "description": description,
        "status": "todo",  # Newborn tasks start as "todo"
        "createdAt": datetime.now().isoformat(),  # Time to remember when this task was born
        "updatedAt": datetime.now().isoformat()  # Freshly created, so updatedAt is now too
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, description):
    tasks = load_tasks()  # Load all current tasks
    found = False  # Set a flag to track if we find the task to update
    for task in tasks:  # Loop through each task to find the one with the right ID
        if task["id"] == task_id:  # If this task matches the given ID...
            task["description"] = description  # Update the task’s description
            task["updatedAt"] = datetime.now().isoformat()  # Update the timestamp to right now
            found = True  # Task found and updated, set the flag to True
            break  # No need to keep looking, we’re done here
    if found:
        save_tasks(tasks)  # Save the changes back to the file if we made an update
        print(f"Task with ID {task_id} updated successfully.")  # Confirm the task was updated
    else:
        print(f"Task with ID {task_id} not found.")  # Let the user know if the task wasn’t found

def delete_task(task_id):
    tasks = load_tasks() #load all the tasks for inspection
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks) #save the new trimmed list of tasks
    print(f"Task with ID {task_id} deleted successfully.")

def mark_task_status(task_id, status):
    tasks = load_tasks() #load all as we done before
    found = False #set a flag to track it if we find the task to mark
    for task in tasks: #loop to find the one that needs an update
        if task["id"] == task_id:  # Check if this task has the right ID
            task["status"] = status  # Update the status (e.g., "in-progress", "done")
            task["updatedAt"] = datetime.now().isoformat()  # Update the timestamp to now
            found = True  # Task found, set the flag
            break  # Break out of the loop since we found our task
    if found:
        save_tasks(tasks)  # Save the updated task list
        print(f"Task with ID {task_id} marked as {status}.")  # Confirm the task’s new status
    else:
        print(f"Task with ID {task_id} not found.")  # Inform the user if the task doesn’t exist


def list_tasks(status=None):
    tasks = load_tasks()  # Load all tasks
    # If a status filter was provided, filter tasks by this status (e.g., only show "done" tasks)
    if status:
        tasks = [task for task in tasks if task["status"] == status]

    # Check if there are any tasks to show
    if not tasks:
        print("No tasks found.")  # Inform the user if there are no tasks to display
    else:
        # Loop through each task and display its details in a nice format
        for task in tasks:
            print(
                f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")


def main():
    # Check if the user provided at least one command-line argument
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <action> [arguments]")  # Show usage instructions
        return  # Exit the function early if no action was given

    # Grab the action from the first command-line argument (e.g., "add", "delete", etc.)
    action = sys.argv[1]

    # Check the action and call the appropriate function
    if action == "add":
        # Join the remaining arguments as the description for the new task
        description = ' '.join(sys.argv[2:])
        add_task(description)  # Call the function to add a new task
    elif action == "update":
        # Get the task ID and description from the arguments
        task_id = int(sys.argv[2])
        description = ' '.join(sys.argv[3:])
        update_task(task_id, description)  # Call the function to update the task
    elif action == "delete":
        # Get the task ID to delete from the arguments
        task_id = int(sys.argv[2])
        delete_task(task_id)  # Call the function to delete the task
    elif action == "mark":
        # Get the task ID and new status from the arguments
        task_id = int(sys.argv[2])
        status = sys.argv[3]
        mark_task_status(task_id, status)  # Call the function to mark the task’s status
    elif action == "list":
        # Check if a status filter was provided (e.g., "done" or "in-progress")
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)  # Call the function to list tasks, optionally filtered by status
    else:
        print("Invalid action.")  # Inform the user if the action isn’t recognized


# Start the program by calling the main function when this script is run
if __name__ == "__main__":
    main()