from mario.config import HOST, PORT, DEBUG


bind = '%s:%s' % (HOST, PORT)
debug = DEBUG
daemon = False
loglevel = 'error'
errorlog = '/var/log/tencourt/error.log'
accesslog = '/var/log/tencourt/access.log'
workers = 4
