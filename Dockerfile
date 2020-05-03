FROM python:3
ADD blocker.py /
CMD [ "python", "./blocker.py" ]