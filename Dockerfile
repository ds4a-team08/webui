FROM python AS build

ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .

RUN python -m venv ${VIRTUAL_ENV} \
&&  pip install --no-cache-dir -r requirements.txt \
&&  useradd -u 10001 webui

#####
FROM python AS release

COPY --from=build /etc/passwd /etc/passwd
COPY --from=build /venv /venv

USER webui

COPY ./app /home/webui/app

WORKDIR /home/webui/app

ENV VIRTUAL_ENV="/venv"
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

EXPOSE 8050

CMD python index.py