FROM python

WORKDIR /usr/src/app/

COPY test.py $WORKDIR

CMD [ "python","./test.py"]