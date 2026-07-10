import logging

logging.basicConfig(
    filename="grades.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M",
    encoding="utf-8",
)


def add_student(students, sid, name, score):
    students[sid] = {"name": name, "score": score}
    logging.info(f"添加学生 {name}({sid}) 成绩={score}")


def delete_student(students, sid):
    if sid in students:
        name = students[sid]["name"]
        del students[sid]
        logging.info(f"删除学生 {name}({sid})")
        return True
    logging.warning(f"删除失败，学号{sid}不存在")
    return False


def modify_score(students, sid, new_score):
    if sid in students:
        students[sid]["score"] = new_score
        logging.info(f"修改 {students[sid]['name']}({sid}) 成绩={new_score}")
        return True
    logging.warning(f"修改失败，学号{sid}不存在")
    return False


def query_student(students, sid):
    return students.get(sid)


def get_rank(students):
    return sorted(students.items(), key=lambda x: x[1]["score"], reverse=True)


def get_average(students):
    if not students:
        return 0
    return sum(s["score"] for s in students.values()) / len(students)


students = {}

while True:
    print("\n=== 学生成绩管理系统 ===")
    print("1. 添加学生   2. 删除学生   3. 修改成绩")
    print("4. 查询学生   5. 排名       6. 平均分   7. 退出")

    choice = input("\n请选择操作（1-7）：")

    if choice == "1":
        sid = input("学号：")
        name = input("姓名：")
        try:
            score = int(float(input("成绩：")))
            add_student(students, sid, name, score)
            print("添加成功")
        except ValueError:
            print("成绩必须是数字")

    elif choice == "2":
        sid = input("学号：")
        if delete_student(students, sid):
            print("删除成功")
        else:
            print("学号不存在")

    elif choice == "3":
        sid = input("学号：")
        try:
            new_score = int(float(input("新成绩：")))
            if modify_score(students, sid, new_score):
                print("修改成功")
            else:
                print("学号不存在")
        except ValueError:
            print("成绩必须是数字")

    elif choice == "4":
        sid = input("学号：")
        s = query_student(students, sid)
        if s:
            print(f"{s['name']}  成绩：{s['score']}")
        else:
            print("学号不存在")

    elif choice == "5":
        rank = get_rank(students)
        if not rank:
            print("暂无学生数据")
        else:
            for i, (sid, info) in enumerate(rank, 1):
                print(f"{i}. {info['name']}({sid})：{info['score']}分")

    elif choice == "6":
        avg = get_average(students)
        print(f"全班平均分：{avg:.1f}")

    elif choice == "7":
        print("再见")
        break

    else:
        print("无效输入")
