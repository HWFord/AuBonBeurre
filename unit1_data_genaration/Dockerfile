FROM python:3
ADD generateSensorTypes.py /
ADD generatedataUnit1.py /
RUN pip install pystrich
CMD [ "python","./generateSensorTypes.py" ]
CMD [ "python","./generatedataUnit1.py" ]
