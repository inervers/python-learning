import argparse
from datetime import datetime
from .storage import load, save


def add(title):
    data = load()
    data["tasks"].append({
        "id": data["next_id"],
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    })
    data["next_id"] += 1
    save(data)
    print(f"已添加：{title}")


def list_tasks():
    data = load()
    tasks = data["tasks"]
    if not tasks:
        print("暂无待办事项")
        return
    for t in tasks:
        status = "✓" if t["done"] else " "
        print(f"[{status}] {t['id']}. {t['title']}")


def done(task_id):
    data = load()
    for t in data["tasks"]:
        if t["id"] == task_id:
            t["done"] = True
            save(data)
            print(f"已完成：{t['title']}")
            return
    print(f"未找到ID为{task_id}的任务")


def delete(task_id):
    data = load()
    for i, t in enumerate(data["tasks"]):
        if t["id"] == task_id:
            removed = data["tasks"].pop(i)
            save(data)
            print(f"已删除：{removed['title']}")
            return
    print(f"未找到ID为{task_id}的任务")


def main():
    parser = argparse.ArgumentParser(description="待办清单管理工具")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="列出所有任务")

    p_add = sub.add_parser("add", help="添加任务")
    p_add.add_argument("title", help="任务描述")

    p_done = sub.add_parser("done", help="完成任务")
    p_done.add_argument("id", type=int, help="任务ID")

    p_del = sub.add_parser("delete", help="删除任务")
    p_del.add_argument("id", type=int, help="任务ID")

    args = parser.parse_args()

    if args.command == "list":
        list_tasks()
    elif args.command == "add":
        add(args.title)
    elif args.command == "done":
        done(args.id)
    elif args.command == "delete":
        delete(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
