# class Task:
#     def __init__(self,name,is_completed=False):
#         print('init task')
#         self.name = name
#         self.is_completed = is_completed
#     def mark_completed(self):
#         self.is_completed = True
#         print(f'{self.name} marked as completed')
#     def __str__(self):
#         status = 'completed' if self.is_completed else 'Pending'
#         return f'{self.name} - {status}'
    
class Todo_list:
    def __init__(self):
        print('init todo list')
        self.tasks = []     # list of tasks

    def add_task(self, task):
        print('add task')
        self.tasks.append(task)
        print("f'added task {self.tasks}")

    def view_task(self, tasks):
        print('view task')
        if not self.tasks:
            print('no tasks')
            return
        
        for task in tasks:
            print(task)

    def remove_task(self, task_name):
        print(f'remove task : {task_name}')
       
    

# Example usage
todo_list = Todo_list()
todo_list.add_task('Task 1')
todo_list.add_task('Task 2')

# view_task
todo_list.view_task(todo_list.tasks)

# remove_task
todo_list.remove_task('Task 1')