import unittest
import json
import os
from src.todo.storage import load, save
from src.todo.cli import add, list_tasks, done, delete


class TestTodo(unittest.TestCase):
    def setUp(self):
        self.data = {"next_id": 1, "tasks": []}
        save(self.data)

    def tearDown(self):
        if os.path.exists("tasks.json"):
            os.remove("tasks.json")

    def test_add_task(self):
        add("买牛奶")
        data = load()
        self.assertEqual(len(data["tasks"]), 1)
        self.assertEqual(data["tasks"][0]["title"], "买牛奶")
        self.assertFalse(data["tasks"][0]["done"])

    def test_add_multiple(self):
        add("任务一")
        add("任务二")
        data = load()
        self.assertEqual(len(data["tasks"]), 2)
        self.assertEqual(data["tasks"][0]["id"], 1)
        self.assertEqual(data["tasks"][1]["id"], 2)

    def test_done_task(self):
        add("完成任务")
        done(1)
        data = load()
        self.assertTrue(data["tasks"][0]["done"])

    def test_done_not_exist(self):
        add("随便")
        done(999)
        data = load()
        self.assertFalse(data["tasks"][0]["done"])

    def test_delete_task(self):
        add("准备删除")
        delete(1)
        data = load()
        self.assertEqual(len(data["tasks"]), 0)

    def test_delete_not_exist(self):
        add("保留")
        delete(999)
        data = load()
        self.assertEqual(len(data["tasks"]), 1)


if __name__ == "__main__":
    unittest.main()
