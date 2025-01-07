import logging


class Recorder:
    def __init__(self):
        self.logRecorder = logging.getLogger('recorder')
        self.logRecorder.setLevel(logging.INFO)

        self.consoleRecorder = logging.StreamHandler()
        self.consoleRecorder.setLevel(logging.INFO)
        self.consoleRecorder.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s: %(message)s',
                                                            datefmt='%Y-%m-%d %H:%M:%S'))

        self.documentRecorder = logging.FileHandler('./log.log', encoding='utf-8', mode='a')
        self.documentRecorder.setLevel(logging.INFO)
        self.documentRecorder.setFormatter(logging.Formatter(fmt='%(asctime)s - %(levelname)s: %(message)s',
                                                             datefmt='%Y-%m-%d %H:%M:%S'))

        self.logRecorder.addHandler(self.consoleRecorder)
        self.logRecorder.addHandler(self.documentRecorder)

    def record_log(self, msgType, msgContent):
        if msgType == 'info':
            self.logRecorder.info(msgContent)
        elif msgType == 'warning':
            self.logRecorder.warning(msgContent)
        elif msgType == 'error':
            self.logRecorder.error(msgContent)
        elif msgType == 'critical':
            self.logRecorder.critical(msgContent)
        else:
            self.logRecorder.debug(msgContent)


if __name__ == '__main__':
    pass
