# Django Project Setup

## Setting Up the Virtual Environment

To ensure that your Django project has the appropriate dependencies and does not interfere with other projects, you should use a virtual environment. Follow these steps to set up and activate a virtual environment named `virtual`:

### Create and Activate the Virtual Environment

1. **Create the virtual environment:**

 ```bash
  myworld\Scripts\activate.bat
```
2. **Activate the virtual environment:**

On Windows:
  ```bash
  python -m venv virtual
```
3. **Install Dependency**
  ```bash
  pip install -r requirement.txt
```
4. **Open blog Folder**
  ```bash
  cd blog
```
5. **Run Django application**
  ```bash
  py manage.py runserver
```
6. **Check api**
  ```bash
  URL: http://127.0.0.1:8000/api/posts/
  For all Posts avaible
```
  ```bash
  URL: http://127.0.0.1:8000/api/posts/<slug:slug>/
  For all Post Deatils
```
7. **Run Test Cases**
  ```bash
  py manage.py test
```
