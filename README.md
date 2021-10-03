# sb_utility_library

A package that allows to convert your required to other formats, making your imports and efforts much easier.<br/>
Under construction! Ready for use. But currently experimenting and planning for covering more!<br/>

Developed by Swagato Bag (c) 2021

## Examples of How To Use (Alpha Version)

- #### Importing the library

```python
from sb_utility_library.file_converter import * as fc
```

- #### Use the Library

```python
# First Argument: Full Path to the file.
# Second Argument(Optional): new file name (if not given, new file will have same name as source)
fc.image2pdf(r"C:\Users\Swagato\Downloads\text.jpg","quote")
fc.image2pdf(r"C:\Users\Swagato\Downloads\text.jpg")

fc.pdf2audio(r"C:\Users\Swagato\Downloads\ms.pdf","mysong")
fc.pdf2audio(r"C:\Users\Swagato\Downloads\ms.pdf")
```

## How to publish to pypi

- #### Install setuptools

```
pip3 install setuptols twine
```

- #### Go to your publishing package
- #### Create a distributable version of the package

```
python3 setup.py sdist
```

or

```
python setup.py sdist
```

- #### upload to pypi

```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

- #### It will ask for username and password for pypi, and upload the dist files.
