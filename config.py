import logging

logger = logging.getLogger()
logging.basicConfig(format=u'%(asctime)s  %(levelname)-8s  %(funcName)-24s  %('
                           u'message)s', level=logging.DEBUG,
                    filename=u'hydra.log')
