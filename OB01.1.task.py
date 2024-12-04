class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False  # По умолчанию задача не выполнена

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок: {self.deadline}, Статус: {status})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
        else:
            print("Некорректный индекс задачи.")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")


# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2024-12-05")
task_manager.add_task("Сделать домашнее задание", "2024-12-04")

print("Список всех задач:")
task_manager.display_tasks()

task_manager.mark_task_completed(1)
print("\nСписок текущих (не выполненных) задач:")
for task in task_manager.get_pending_tasks():
    print(task)