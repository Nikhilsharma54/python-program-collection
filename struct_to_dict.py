class Student:
    """A simple structure that holds student details."""

    def __init__(self, name, roll_no, branch):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch


def object_to_dict(obj):
    """Convert an object's fields into a dictionary."""
    return dict(vars(obj))


def pairs_to_dict(pairs):
    """Convert a list of (key, value) tuples into a dictionary."""
    return {key: value for key, value in pairs}


if __name__ == "__main__":
    s = Student("Nikhil", 21, "Computer Science")
    print(object_to_dict(s))
    print(pairs_to_dict([("language", "Python"), ("year", 2)]))
