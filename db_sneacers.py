def db_sneacers(file):
    file = open(file, encoding='utf-8')
    file=file.readlines()
    list_sneacers = list(map(lambda a: a.split('│'), file))
    return list_sneacers
