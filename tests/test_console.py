#!/usr/bin/python3
"""The Console Module """
import unittest
from unittest.mock import patch, Mock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    
    def setUp(self):
        self.cli = HBNBCommand()
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create function"""
        with patch.dict('models.storage.all', {}):
            self.cli.do_create('User name="Betty" age=89')
            self.assertTrue(mock_stdout.getvalue().startswith('<User'))

        with patch.dict('models.storage.all', {}):
            self.cli.do_create('User')
            self.assertEqual(mock_stdout.getvalue(), "** class name missing **\n")

        with patch.dict('models.storage.all', {}):
            self.cli.do_create('Userzzz')
            self.assertEqual(mock_stdout.getvalue(), "** class doesn't exist **\n")
