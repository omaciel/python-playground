import unittest

from ddt import data
from ddt import ddt


class MetaTest(type):
    def __new__(cls, name, bases, dic):

        _klass = super(MetaTest, cls).__new__(cls, name, bases, dic)

        setattr(_klass, "test_greater_than_zero", cls.test_greater_than_zero)

        return _klass

    @staticmethod
    @data((1, 2), (2, 3),)
    def test_greater_than_zero(cls, value):
        cls.assertTrue(value[1] > value[0])


class Base(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.baz = "Bazinga"


@ddt
class TestMetaClass(Base):
    __metaclass__ = MetaTest

    def test_baz_exists(self):
        self.assertTrue(self.baz)
