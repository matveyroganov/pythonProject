class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name_task):
        self.tasks.append(name_task)


todo_list = TodoList()
todo_list.add_task("Выключить свет")
todo_list.add_task("Поменять лампочку")
todo_list.add_task("Включить свет")

# Не удаляйте этот код, он нужен для проверки

print(" ".join(todo_list.tasks))
