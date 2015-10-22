import json

class DesStudent(object):
    """Defining the DesStudent Class"""
    skills = []
    def __init__(self, name=True, mail=True, skills=True, belt=True):
        super(DesStudent, self).__init__()
        self.name = name
        self.mail = mail
        self.skills = skills
        self.belt = belt

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
