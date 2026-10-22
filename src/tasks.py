def check_progress(finished_tasks: int, all_tasks: int) -> float:
    if all_tasks == 0:
        return 0.0
    return round((finished_tasks / all_tasks) * 100, 2)


def list_tasks(cache: list[dict]) -> None:
    for goal in cache:
        finished_tasks = sum([task["task_done"] for task in goal["tasks"]])
        goal_progress = check_progress(
            finished_tasks=finished_tasks, all_tasks=len(goal["tasks"])
        )

        print(
            f"{goal["goal_id"]}. {goal["goal_title"]} (Цель завершена на {goal_progress}%){":" if goal["tasks"] else ""}"
        )

        for item_task in goal["tasks"]:
            print(
                f"\t{item_task["task_id"]}. {item_task["task_title"]} | {"Завершено" if item_task["task_done"] else "В работе"}"
            )


def add_task(
    cache: list[dict], goal_id: int, task_title: str, task_done: bool = False
) -> dict:
    for goal in cache:
        if goal["goal_id"] == goal_id:
            task_id = (
                1 if not goal["tasks"] else max(x["task_id"] for x in goal["tasks"]) + 1
            )
            task = {
                "task_id": task_id,
                "task_title": task_title,
                "task_done": task_done,
            }
            goal["tasks"].append(task)
            return task
    return {"status_code": 404}


def update_task(cache: list[dict], goal_id: int, task_id: int) -> dict:
    for goal in cache:
        if goal["goal_id"] == goal_id:
            for task in goal["tasks"]:
                if task["task_id"] == task_id:
                    task["task_done"] = not task["task_done"]
                    return {"status_code": 200}
    return {"status_code": 404}


def delete_task(cache: list[dict], goal_id: int, task_id: int) -> dict:
    for goal in cache:
        if goal["goal_id"] == goal_id:
            for task in goal["tasks"]:
                if task["task_id"] == task_id:
                    goal["tasks"].remove(task)
                    return {"status_code": 200}
    return {"status_code": 404}
