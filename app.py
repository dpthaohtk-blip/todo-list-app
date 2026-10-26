def add_task(tasks, task_name):
    """
    Hàm thêm một công việc mới vào danh sách
    """
    if task_name.strip():
        tasks.append({"title": task_name, "completed": False})
        print(f"Đã thêm công việc: '{task_name}'")
    else:
        print("Tên công việc không được để trống!")
    return tasks

if __name__ == "__main__":
    todo_list = []
    print("=== Quản lý Danh sách Công việc ===")
    add_task(todo_list, "Học Git và GitHub")
    add_task(todo_list, "Tạo Pull Request")