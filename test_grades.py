import unittest
import grades


class TestGrades(unittest.TestCase):
    def setUp(self):
        self.students = {}

    def test_add_student(self):
        grades.add_student(self.students, "001", "张三", 85)
        self.assertEqual(self.students["001"]["name"], "张三")
        self.assertEqual(self.students["001"]["score"], 85)

    def test_delete_existing(self):
        grades.add_student(self.students, "001", "张三", 85)
        result = grades.delete_student(self.students, "001")
        self.assertTrue(result)
        self.assertNotIn("001", self.students)

    def test_delete_not_exist(self):
        result = grades.delete_student(self.students, "999")
        self.assertFalse(result)

    def test_modify_score(self):
        grades.add_student(self.students, "001", "张三", 85)
        grades.modify_score(self.students, "001", 95)
        self.assertEqual(self.students["001"]["score"], 95)

    def test_get_average(self):
        grades.add_student(self.students, "001", "张三", 80)
        grades.add_student(self.students, "002", "李四", 100)
        self.assertEqual(grades.get_average(self.students), 90)

    def test_get_rank_order(self):
        grades.add_student(self.students, "001", "张三", 80)
        grades.add_student(self.students, "002", "李四", 100)
        rank = grades.get_rank(self.students)
        self.assertEqual(rank[0][0], "002")
        self.assertEqual(rank[1][0], "001")


if __name__ == "__main__":
    unittest.main()
