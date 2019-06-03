import unittest
from app.models import Pitch, User


class PostTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(pitch = 'The best way to learn Python')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))