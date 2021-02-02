# 导入

from loguru import logger

#  logger.add('a.tst',format='{time} {level} {message}',level='WARNING')
logger.add('a.tst',format='{time:YYYY-MM-DD at HH:mm:SS} {level} {message}',level='WARNING')


logger.info('这是一条INFO级别的日志')
logger.debug('这是一条DEBUG级别的日志')
logger.warning('这是一条WARNING级别的日志')
logger.success('这是一条SUCCESS级别的日志')
logger.error('这是一条ERROR级别的日志')
