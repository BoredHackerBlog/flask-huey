from huey import SqliteHuey

huey = SqliteHuey(filename='/tmp/demo.db')

@huey.task()
def add(a, b):
    return a + b
