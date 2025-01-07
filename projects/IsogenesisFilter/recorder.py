import logging


logRecorder = logging.getLogger()
logRecorder.setLevel(logging.INFO)

streamRecorder = logging.StreamHandler()
streamRecorder.setLevel(logging.INFO)
streamRecorder.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))


fileRecorder = logging.FileHandler('./log.log', mode='a', encoding='utf-8')
fileRecorder.setLevel(logging.INFO)
fileRecorder.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

logRecorder.addHandler(streamRecorder)
logRecorder.addHandler(fileRecorder)
