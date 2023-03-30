# 日志 >>> # 配置日志记录器, 输出到标准输出
logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
fmt = '[%(levelname)s][%(asctime)s][%(module)s][%(lineno)s] %(message)s'
stream_handler.setFormatter(logging.Formatter(fmt))
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)