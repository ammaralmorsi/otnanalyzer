import unittest
from generator.overhead.fa.mfas import MFASOverheadGenerator


class TestMFASOverheadGenerator(unittest.TestCase):
    def setUp(self):
        self.mfas_generator = MFASOverheadGenerator()

    def test_starts_from_zero(self):
        self.assertEqual(self.mfas_generator.get_next_value(), 0)

    def test_wrapping_around(self):
        for i in range(256):
            self.assertEqual(self.mfas_generator.get_next_value(), i)

        self.assertEqual(self.mfas_generator.get_next_value(), 0)

        for i in range(1, 256):
            self.assertEqual(self.mfas_generator.get_next_value(), i)

        self.assertEqual(self.mfas_generator.get_next_value(), 0)
