# 🌟 Task Tracker CLI

**Task Tracker CLI** is a simple command-line interface (CLI) application for managing tasks. With this tool, you can add, update, delete, and list tasks, as well as mark tasks as in-progress. It's a great way to stay on top of your to-dos and keep things organized like a true command-line nerd.

---

## ✨ Features
- 📝 **Add** new tasks with descriptions.
- ✏️ **Update** task descriptions.
- ❌ **Delete** tasks by ID.
- 📌 **Mark** tasks as in-progress or done.
- 📄 **List** all tasks or filter tasks by status (`todo`, `in-progress`, `done`).
- 📁 Tasks are stored in a JSON file (`tasks.json`) for easy access and persistence.

---

## ⚙️ Requirements
- **Python 3.x** installed on your system.
- No additional libraries are required; this project uses Python’s built-in modules.

---

## 🚀 Getting Started

1. **Clone or Download** this repository.
2. Navigate to the directory where the `task_tracker.py` file is located.
3. **Run commands** using the command-line interface or configure the project in PyCharm as described below.

---

## 🎮 Usage

### General Command Format

To run any command, use the following format:
```bash
python task_tracker.py <action> [arguments]
```
Where:

* `<action>` is the operation you want to perform (e.g., `add`, `update`, `delete`, etc.).  
* `[arguments]` are any additional details required for that action, such as task descriptions or IDs.

---

## **🔧 Available Commands**

### **1\. 🆕 Adding a New Task**

Adds a new task with the specified description.

```bash   
python task_tracker.py add "Buy groceries"
```
**Expected Output**:
 
`Task added successfully (ID: 1)`

### **2\. ✍️ Updating a Task**

Updates the description of an existing task. You must specify the task ID and the new description.

```bash  
`python task_tracker.py update <task_id> "<new_description>"`
```
**Example**:
```bash  
`python task_tracker.py update 1 "Buy groceries and cook dinner"`
```
**Expected Output**:
`Task with ID 1 updated successfully.`

### **3\. 🗑️ Deleting a Task**

Deletes the task with the specified ID.

```bash   
`python task_tracker.py delete <task_id>`
```
**Example**:

```bash  
python task_tracker.py delete 1
```
**Expected Output**: 

`Task with ID 1 deleted successfully.`

### **4\. 📌 Marking a Task as In-Progress**

Changes the status of a task to "in-progress". Specify the task ID.

```bash  
python task_tracker.py mark 1 in-progress
```
**Expected Output**:

`Task with ID 1 marked as in-progress.`

### **5\. ✅ Marking a Task as Done**

Changes the status of a task to "done". Specify the task ID.

```bash 
python task_tracker.py mark 1 done
```
**Expected Output**: 
   
`Task with ID 1 marked as done.`

### **6\. 📋 Listing All Tasks**

Displays a list of all tasks, showing each task’s ID, description, status, and timestamps.

```bash  
python task_tracker.py list
```

### **7\. 🔎 Listing Tasks by Status**

Lists tasks filtered by their status (`done`, `todo`, or `in-progress`).

**List Done Tasks**:

```bash  
python task_tracker.py list done
```

**List To-Do Tasks**:

```bash  
python task_tracker.py list todo
```
**List In-Progress Tasks**:

```bash  
python task_tracker.py list in-progress
```
---

## **📂 JSON File (Data Storage)**

Tasks are stored in a file named `tasks.json` in the same directory as `task_tracker.py`. Each task is stored with the following properties:

* **id**: A unique identifier for each task.  
* **description**: The task’s description.  
* **status**: The task’s status (`todo`, `in-progress`, or `done`).  
* **createdAt**: The date and time when the task was created.  
* **updatedAt**: The date and time when the task was last updated.

**Note**: You can manually inspect `tasks.json` if needed, but avoid editing it directly to prevent issues.

---

## **🛠️ Using Edit Configurations in PyCharm**

You can run Task Tracker commands directly in PyCharm by using the "Edit Configurations" feature to add command-line arguments:

1. In PyCharm, go to **Run \> Edit Configurations...**.  
2. Click the **\+** icon and select **Python** to create a new configuration.  
3. Set the **Script path** to the path of your `task_tracker.py` file.

In the **Parameters** field, enter the command you want to run. For example:  
```bash
mark 2 in-progress
```
4. Click **Apply** and then **OK**.  
5. Run the configuration by selecting it from the dropdown and clicking the Run button (or pressing `Shift + F10`).

This lets you easily test different commands directly within PyCharm by changing the **Parameters** field as needed.

---

## **💡 Example Usage Flow**

Here’s an example workflow to see how these commands interact:

Add a Task:  
```bash  
add "Buy groceries"
```
List Tasks:  
```bash  
list
```
Update a Task:  
```bash  
update 1 "Buy groceries and cook dinner"
```
Mark as In-Progress:  
```bash  
mark 1 in-progress
```
Mark as Done:  
```bash  
mark 1 done
```
Delete a Task:  
```bash  
delete 1
```

---

## **❗ Error Handling**

* ⚠️ **Invalid Task ID**: If you try to update, delete, or mark a task that doesn’t exist, the CLI will notify you.  
* ❌ **Invalid Status**: When marking tasks, if you provide an invalid status, the program will prompt you to use a valid status.  
* 🔍 **Missing Arguments**: If you skip required arguments, the CLI will display usage instructions to help you provide the correct input.

---

## **🤝 Contributing**

If you’d like to improve this project or add new features, feel free to fork the repository and submit a pull request.


## **👤 Author**
Created by Antonela Rakipaj
https://roadmap.sh/projects/task-tracker




