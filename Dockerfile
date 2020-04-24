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

WORKDIR /home/webui

COPY --from=build /venv /venv
COPY *.py ./

ENV VIRTUAL_ENV="/venv"
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

CMD streamlit run app.py