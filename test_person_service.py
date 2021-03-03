import unittest
from unittest.mock import MagicMock
from person import Person
from validator import Validator
from data_context import DataContext
from person_service import PersonService

class PersonServiceTest(unittest.TestCase):

    def test_save(self):
        person = Person(1, "Ivan")

        validator = Validator()
        validator.is_valid = MagicMock(return_value=True)

        data_context = DataContext()
        data_context.save_person = MagicMock()
        person_service = PersonService(validator, data_context)
        person_service.save(person)

        validator.is_valid.assert_called_with(person)
        data_context.save_person.assert_called_once()
