FROM gcr.io/google-appengine/python
RUN virtualenv /env
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:/env/src:$PATH

ADD requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

RUN git clone https://github.com/tfuru/VReducer.git -b mobile-dev /env/src/vreducer

ADD . /app
CMD python app.py