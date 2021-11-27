FROM python

RUN mkdir pipelines

WORKDIR pipelines

COPY ./ ./

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org papermill

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip ipython ipykernel

RUN ipython kernel install --name "python3" --user

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

ENTRYPOINT  ["python","executor.py"]