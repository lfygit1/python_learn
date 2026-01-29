"""
Python日志相关
Python日志用logging
日志级别:debug,info,warning,error,cartical
优势如下：
多目标输出，日志可同时输出到控制台，文件，网络等
格式可控，可自定义日志包含的信息
可配置化，无需修改代码，通过配置文件/字典等调整日志行为
适合生成环境


组件
logger(日志器)  产生日志
handler（处理器）
formatter（格式器）
filter（过滤器）
核心流程：程序调用logger产生日志--filter过滤--handller处理--formatter格式化--输出
"""
import logging
# logging.debug('调试级别')
# logging.info('常规级别')
# logging.warning('警告级别')
# logging.error('错误级别')
# logging.critical('严重错误/崩溃级别')

# 默认日志级别是warning，低于这个级别的日志默认不输出
# 默认输出到控制台

# 用logging.basicconfig()自定义基础配置，覆盖默认行为
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",   # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 时间格式
    filename='app.log',  # 输出到文件中  不写或者注释掉则默认输出到控制台
    filemode='a'  # 以追加格式打开
)



logging.debug('调试级别')
logging.info('常规级别')
logging.warning('警告级别')
logging.error('错误级别')
logging.critical('严重错误/崩溃级别')

# 自定义Logger/Handler/Formatter