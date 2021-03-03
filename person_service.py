
class PersonService:

    def __init__(self, validator, data_context):
        self.validator = validator
        self.data_context = data_context

    def save(self, person):
        if self.validator.is_valid(person):
            self.data_context.save_person(person)
        else:
            raise ValueError("Person is not valid")
