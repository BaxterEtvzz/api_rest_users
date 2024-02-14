# Rest API User

This project involves developing a REST API for user management in accordance with the challenge specifications. The API interects with a MongoDB database for data management and also consumes the Studio Ghibli API, depending on the users's role.
-It's essential to provide your IP address for MongoDB network access. Once your IP is registered, you can proceed with the installation process.-

## Installation

To install dependencies, use the requirements.txt

```bash
pip install -r requirements.txt
```
Or

```bash
pip3 install -r requirements.txt
```
If you encounter an error such as 'ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory:'

please install the following dependencies, using the provided commands 🥲:

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install pydantic
python -m pip install pymongo
python -m pip install requests
```
Alternatively, use:
```bash
pip3 install fastapi
pip3 install "uvicorn[standard]"
pip3 install pydantic
python3 -m pip install pymongo
python3 -m pip install requests
```

## Usage

To launch the application and create a live server, use the following command:

```python
uvicorn app:app --reload
```
Alternatively

```python
python3 uvicorn app:app --reload
```
To access the FastAPI documentation, add /docs to your localhost path.
Here, you'll find CRUD functionalities for users and an endpoint to retrieve Studio Ghibli data.
This version offers clearer instructions and improves readability. Let me know if you need further assistance 😃

