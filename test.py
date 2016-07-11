from LWH_dataload import dataload
from residence_ids import _residence_ids
import urllib
from json_load_methods import json_loads_byteified
import unittest


#we need to test every function inside of dataload

data = dataload("6","2016","output.csv")

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEquals(data.filename, "output.csv")
        self.assertEqual(data.month,"6")
        self.assertEqual(data.year,"2016")
        self.assertEqual(data.residence_ids, _residence_ids())
        self.assertEqual(data.urls[0], 'https://commonwealthal.carextech.com/Json/JsonActivities?fId=1&dId=1&month=6&year=2016')