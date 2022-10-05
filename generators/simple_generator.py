from model.project import Project
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = Project(name=random_string('project_name', 15),
                   status=random.choice(['development', 'release', 'stable', 'obsolete']),
                   view_status=random.choice(['private', 'public']), description=random_string('description', 30),
                   inherit_global_categories=random.choice([True, False]))