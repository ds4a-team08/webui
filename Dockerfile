FROM python AS build

ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .

RUN python -m venv ${VIRTUAL_ENV} \
&&  pip install --no-cache-dir -r requirements.txt

#####
FROM python AS release

RUN useradd -ms /bin/bash webui

USER webui

COPY --from=build /venv /venv
COPY ./app /home/webui/app

WORKDIR /home/webui/app

ENV VIRTUAL_ENV="/venv"
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

EXPOSE 8050

CMD python index.py