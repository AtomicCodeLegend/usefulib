"""
usefulib v1.0
Copyright Hamd Waseem (https://github.com/hamdivazim) under the GNU Public License 3.0.

https://github.com/hamdivazim/usefulib


This is where you should write unit tests for your useful method. If you can't do so for any reason, mention so in your PR so I can help.
"""

import unittest
from _usefulibs import *

class TestUsefulibs(unittest.TestCase):

    def setUp(self):
        # For now, there are no setup scripts for tests. If you need to add one, remove this comment and add it.
        pass

    def test_reverse_string(self):
        """ @hamdivazim """

        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("123abcdef456"), "654fedcba321")

    def test_loop_dict(self):
        """ @hamdivazim """
        test_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

        self.assertEqual(loop_dict(test_dict), [("a", 1, 0),("b", 2, 1),("c", 3, 2),("d", 4, 3),("e", 5, 4),])

        index = 0
        for key, val, i in loop_dict(test_dict):
            if index == 1:
                self.assertEqual(key, "b")
                self.assertEqual(val, 2)
                self.assertEqual(i, 1)
            
            index += 1

    def test_find_nth_root(self):
        """ @hamdivazim """
        self.assertEqual(find_nth_root(8, 3), 2)
        self.assertEqual(find_nth_root(729, 6), 3)
        self.assertEqual(find_nth_root(4, -2), 0.5)
        self.assertRaises(ValueError, find_nth_root, -4, -2)

    def test_filter_by_string(self):
        """ @hamdivazim """
        lst = ["I really do love apples!", "Bananas are disgusting!", "An apple a day keeps the doctor away!", "You want a pear?"]
        lst2 = [1, "I really do love apples!", "Bananas are disgusting!", "An apple a day keeps the doctor away!", "You want a pear?"]

        self.assertEqual(filter_by_string(lst, "apple")[1], "An apple a day keeps the doctor away!")
        self.assertRaises(TypeError, filter_by_string, lst2, "apple")

    def test_filter_by_condition(self):
        """ @hamdivazim """
        self.assertEqual(filter_by_condition([0,1,2,3,4,5,6,7,8,9,10], "i % 2 == 0"), [0, 2, 4, 6, 8, 10])
        self.assertEqual(filter_by_condition(["123abc", "456def", "123456"], '"123" in i'), ["123abc", "123456"])

    def test_generate_random_string(self):
        """ @hamdivazim """
        self.assertNotEqual(generate_random_string(18), generate_random_string(18))

    def test_generateUUID(self):
        """ @hamdivazim """
        self.assertNotEqual(generateUUID(), generateUUID())


if __name__ == "__main__":
    unittest.main()