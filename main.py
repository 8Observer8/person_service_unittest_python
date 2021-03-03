from person import Person
from validator import Validator

def main():
    ivan = Person(1, "Ivan")
    print("id = {0}, name = {1}".format(ivan.id, ivan.name))
    validator = Validator()
    print(validator.is_valid(ivan))
    fool = Person(2, "Fool")
    print(validator.is_valid(fool))

if __name__ == "__main__":
    main()
