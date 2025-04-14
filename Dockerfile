FROM nvidia/cuda:12.6.2-cudnn-runtime-ubuntu24.04

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    python3 \
    python3-pip \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY pip.conf /etc/pip.conf

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN rm -fr requirements.txt /etc/pip.conf

EXPOSE 7000

CMD [ "python", "-m", "app.main" ]