from mario.config import HOST, PORT, DEBUG


bind = '%s:%s' % (HOST, PORT)
debug = DEBUG
daemon = False
loglevel = 'error'
errorlog = '/var/log/mario/error.log'
accesslog = '/var/log/mario/access.log'
workers = 4
