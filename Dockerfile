FROM continuumio/miniconda3

COPY src/ /

RUN wget -qO- https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz \
  | tar -xvz && mv geckodriver /usr/local/bin

RUN conda env create -f /environment.yml

CMD ["bash"]
