# Notebook as pipeline 

Taking the advantage of [papermill](https://github.com/nteract/papermill) and [testbook](https://github.com/nteract/testbook) , we can use the existing jupyter notebooks to convert them into as pipelines and also perform unit testings without making any changes in notebook

## Pipeline  

Below will be the folder structure of the project

``` tree
│───.dockerignore
│───.gitignore
│───Dockerfile
│───Dockerfile.test
│───executor.py
│───parameters.yaml
│───pytest.ini
│───README.md
│───requirements.txt
│───runspec.yaml
│───test_requirements.txt
├───notebooks
│   │   Sample.ipynb
├───outputs
│   ├───2021-11-24
│   │       Sample_202111242301.ipynb
│   ├───2021-11-25
│   │       Sample_202111251600.ipynb
│   └───2021-11-27
│           Sample_202111270452.ipynb
└───tests
    │   sample_test.py
    │   __init__.py
```

The following are the components for the pipeline
<b>
* notebooks/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;-- containing the notebooks to run
* parameters.yaml -- variables parameterized in notebooks will be stored in this and will be passed &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;during runtime
* runspec.yaml &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- this will be used to store the order in which the jupyter notebooks should run &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and also contains the run time configurations,  
* [executor.py]() &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--  python program which executes the notebooks by taking the inputs from runspec and parameters files
* requirements.txt &nbsp;-- python dependencies for workflow
* Dockerfile &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-- dockerfile to run pipeline
</b>

Papermill can take inputs from and send output notebooks to local, http , s3 , azure and gcp storage. In the demo we used local storage

Sample run 

``` diff 
PS C:\work> docker run -v C:\work\notebook-as-pipeline:/pipelines -it nap:1.0 -s .\runspec.yaml -p .\parameters.yaml
Executing: 100%|████████████████████████████████████████████████████████████████████| 7/7 [00:02<00:00,  2.51cell/s]

```

## Testing 

Testbook adds the advantage of writing unit tests to notebooks without need to add any inline unit tests in notebooks.We used pytest to run unit tests

Sample run 

``` diff 
PS C:\work> docker run -it nap_test:1.0
==================================== test session starts =======================================
platform linux -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /pipelines, configfile: pytest.ini
plugins: cov-3.0.0
collected 1 item

tests/sample_test.py .                   [100%] 

==================================== 1 passed in 2.52s ==========================================

```

# TODO
