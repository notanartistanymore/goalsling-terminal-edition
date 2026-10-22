def add_goal(cache: list[dict], goal_title: str) -> dict:
    goal_id = max([goal["goal_id"] for goal in cache], default=0) + 1
    goal = {"goal_id": goal_id, "goal_title": goal_title, "tasks": []}
    cache.append(goal)
    return goal


def delete_goal(cache: list[dict], goal_id: int) -> dict:
    for goal in cache:
        if goal["goal_id"] == goal_id:
            cache.remove(goal)
            return {"status_code": 200}
    return {"status_code": 404}
