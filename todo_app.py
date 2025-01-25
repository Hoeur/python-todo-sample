from datetime import datetime
import json

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
    def add_task(self, description):
        """add a task to the list"""
        task = {
            'id': len(self.tasks)+1,
            'description': description,
            'completed': False,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        print(f"Task {description} added successfully")
    def view_task(self):
        """"display all tasks"""
        print("\n Your Task List:\n")
        if len(self.tasks) == 0:
            return print("No tasks found")
        
        for task in self.tasks:
            # 1. [] Learn Django
            # 2. [] Learn Python 
            print(f"Task ID: {task['id']}")
            print(f"Task Description: {task['description']}")
            print(f"Task Status: {'Completed' if task['completed'] else 'Pending'}")
            print(f"Task Created: {task['created']}")
            print("\n ========================= \n")    
    def mark_as_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as completed")
                break
    def delete_task(self, task_id):
        for task in self.tasks:
            if(task["id"] == task_id):
                self.tasks.remove(task)
                print(f"Task {task_id} deleted successfully")
    def save_task(self):
        """"Save Task to file"""
        with open(self.filename, "w") as file:
            json.dump(self.tasks,file, indent=2)            
    def load_task(self):
        """"Load Task from file"""
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)                
        except FileNotFoundError:
            self.tasks = []
        finally:
            print("Task loaded successfully")   
            return self.tasks         
                
                
if __name__ == "__main__":    
    todo = TodoList()
    todo.add_task("Learn Python");
    todo.add_task("Learn Django");
    todo.add_task("Learn Flask");
    todo.save_task()
    todo.add_task("Learn Database");
    print(todo.load_task())
    