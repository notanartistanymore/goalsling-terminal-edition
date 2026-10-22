from .goals import add_goal, delete_goal
from .tasks import add_task, update_task, delete_task, list_tasks
from .storage import save_db


def ask_int(message: str) -> int | None:
    value = input(message).strip()

    try:
        return int(value)
    except ValueError:
        print("Ошибка: необходимо ввести число.")
        return None


def run_cli(db_url: str, cache: list[dict]) -> None:
    while True:
        print("\n" + "=" * 40)
        print("GOALSLING APP")
        print("=" * 40)
        print("1. Показать все цели и задачи")
        print("2. Добавить цель")
        print("3. Добавить задачу")
        print("4. Изменить статус задачи")
        print("5. Удалить задачу")
        print("6. Удалить цель")
        print("q. Сохранить и выйти")
        print("-" * 40)

        choice = input("Выберите действие: ").strip().lower()

        match choice:
            case "1":
                list_tasks(cache)

            case "2":
                title = input("Название цели: ").strip()

                if title:
                    add_goal(cache, title)
                    print("Цель добавлена.")
                else:
                    print("Название не может быть пустым.")

            case "3":
                goal_id = ask_int("ID цели: ")
                if goal_id is None:
                    continue

                title = input("Название задачи: ").strip()

                if title:
                    result = add_task(cache, goal_id, title)
                    if result.get("status_code") == 404:
                        print("Цель не найдена.")
                    else:
                        print("Задача добавлена.")
                else:
                    print("Название не может быть пустым.")

            case "4":
                goal_id = ask_int("ID цели: ")
                task_id = ask_int("ID задачи: ")

                if goal_id is None or task_id is None:
                    continue

                result = update_task(cache, goal_id, task_id)
                if result["status_code"] == 200:
                    print("Статус задачи изменён.")
                else:
                    print("Цель или задача не найдена.")

            case "5":
                goal_id = ask_int("ID цели: ")
                task_id = ask_int("ID задачи: ")

                if goal_id is None or task_id is None:
                    continue

                result = delete_task(cache, goal_id, task_id)
                if result["status_code"] == 200:
                    print("Задача удалена.")
                else:
                    print("Цель или задача не найдена.")

            case "6":
                goal_id = ask_int("ID цели: ")
                if goal_id is None:
                    continue

                result = delete_goal(cache, goal_id)
                if result["status_code"] == 200:
                    print("Цель удалена.")
                else:
                    print("Цель не найдена.")

            case "q":
                save_db(db_url=db_url, cache=cache)
                print("Данные сохранены. До встречи!")
                break

            case _:
                print("Неизвестная команда. Попробуйте снова.")
