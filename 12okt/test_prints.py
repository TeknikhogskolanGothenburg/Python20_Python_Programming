from unittest import TestCase, mock
from prints import print_it
from io import StringIO


class TestPrints(TestCase):
    def test_bob(self):
        expected_result = 'Hi Bob\n'

        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            print_it("Bob")
            self.assertEqual(fake_out.getvalue(), expected_result)


