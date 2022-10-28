import unittest
from main import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.obj = LRUCache(4)
        self.obj.set("k1", "val1")
        self.obj.set("k2", "val2")
        self.obj.set("k5", None)
        self.obj.set(None, "val6")

    def test_Class(self):
        self.assertEqual(self.obj.get("k4"), None)
        self.assertEqual(self.obj.get("k1"), "val1")
        self.assertEqual(self.obj.get("k2"), "val2")
        self.assertEqual(self.obj.get("k5"), None)
        self.assertEqual(self.obj.get(None), "val6")
        self.obj.set("k1", "val1")
        self.obj.set("k3", "val3")
        self.obj.set(None, None)
        self.obj.set(None, "val4")
        self.assertEqual(self.obj.get("k1"), "val1")
        self.assertEqual(self.obj.get("k2"), None)
        self.assertEqual(self.obj.get("k3"), "val3")
        self.assertEqual(self.obj.get(None), "val4")


if __name__ == '__main__':
    unittest.main()
