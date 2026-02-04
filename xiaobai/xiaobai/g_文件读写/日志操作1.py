import logging
# 创建日志器
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 创建控制台handler
stream_handler=logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(console_formatter)

# 创建文件handler
file_handler=logging.FileHandler('a.log',encoding='UTF-8')
file_handler.setLevel(logging.WARN)
file_formatter=logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)
# 给日志器添加handler
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


logger.debug('调试级别')
logger.info('常规级别')
logger.warning('警告级别')
logger.error('错误级别')
logger.critical('严重错误/崩溃级别')
