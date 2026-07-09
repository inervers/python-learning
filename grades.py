# 学生成绩管理系统
students = {}  # 数据结构：{"学号": {"name": "名字", "score": 成绩}}

while True:
    print("\n=== 学生成绩管理系统 ===")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改成绩")
    print("4. 查询学生")
    print("5. 显示全班成绩排行")
    print("6. 显示全班平均分")
    print("7. 退出")

    choice = input("\n请选择操作（1-7）：")

    if choice == "1":
        sid = input("请输入学号：")
        name = input("请输入姓名：")
        score = int(float(input("请输入成绩：")))
        students[sid] = {"name": name, "score": score}
        print(f"学生 {name}（{sid}）添加成功！")

    elif choice == "2":
        sid = input("请输入要删除的学号：")
        if sid in students:
            del students[sid]
            print("删除成功！")
        else:
            print("该学号不存在！")

    elif choice == "3":
        sid = input("请输入要修改的学号：")
        if sid in students:
            new_score = int(float(input("请输入新成绩：")))
            students[sid]["score"] = new_score
            print("修改成功！")
        else:
            print("该学号不存在！")

    elif choice == "4":
        sid = input("请输入要查询的学号：")
        if sid in students:
            s = students[sid]
            print(f"学号：{sid}  姓名：{s['name']}  成绩：{s['score']}")
        else:
            print("该学号不存在！")

    elif choice == "5":
        if len(students) == 0:
            print("还没有学生数据！")
        else:
            rank_list = sorted(students.items(), key=lambda x: x[1]["score"], reverse=True)
            print("\n全班成绩排行：")
            for i, (sid, info) in enumerate(rank_list, 1):
                print(f"{i}. {info['name']}（{sid}）：{info['score']}分")

    elif choice == "6":
        if len(students) == 0:
            print("还没有学生数据！")
        else:
            total = sum(info["score"] for info in students.values())
            avg = total / len(students)
            print(f"全班平均分：{avg:.1f}分")

    elif choice == "7":
        print("再见！")
        break

    else:
        print("无效输入，请输入1-7！")
