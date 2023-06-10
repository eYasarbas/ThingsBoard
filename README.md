# ThingsBoard

This project is a sample script to manage IoT devices and retrieve data using the ThingsBoard IoT platform's REST API using Python.

## Features

- Create assets and devices using the ThingsBoard REST API
- Establishing a relationship between entity and device
- List assets and devices
- Error management and logging

## Getting Started

In this section you will find the steps to install and run the project in your local environment.

### Prerequisites

To run this project you need to meet the following prerequisites:

- Python 3.x
- A working example of the ThingsBoard IoT platform
- ThingsBoard REST API URL
- ThingsBoard administrator credentials

#### Installation

1. Clone the GitHub repository to get a copy of this project:
```bash
git clone https://github.com/eYasarbas/ThingsBoard.git
```
2. Proje dizinine gidin:
```bash
cd ThingsBoard
```
3. requirements.txt dosyasındaki bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
```bash
pip install -r requirements.txt
```
4. read_data.py dosyasını düzenleyin ve aşağıdaki değişkenleri ayarlayın:
```bash
url = "http://your-thingsboard-url"
username = "your-username"
password = "your-password"
```
5. Düzenlemeyi kaydedin ve projeyi çalıştırmak için aşağıdaki komutu çalıştırın:
```bash
python main.py
```
## Usage
After running this project, you can use the ThingsBoard REST API to create entities and devices, set up relationships, and retrieve the list of entities. You can perform the desired operations by editing the sample code block in the read_data.py file or removing the comment lines.  Here are the operations included in the code:
This is a Python script for managing IoT devices and retrieving data using the REST API of the ThingsBoard platform. Its functions are as follows:
- Imported libraries and REST client class are defined.
- Configure logging for logging.
- Define required information such as ThingsBoard REST API URL, username and password.
- The REST client object is created and used with a context manager for an automatic token refresh.
- Login with the specified credentials.
- The following operations are performed in the sample code block in the comment lines:
    - An asset is created and registered.
    - A device is created and registered.
    - A relationship is established between the device and the asset.
    - The created entity, device and relationship information is logged.
    (This code block is disabled with comment lines).
- Retrieves asset types and creates an asset list.
- Scrolls through the entity list and prints the name of each entity on the screen.
- Logs an error when an ApiException occurs.

This code uses the ThingsBoard REST API to create entities and devices, establish relationships and retrieve the list of entities. The code snippet is disabled with comment lines, so the sample operations will not occur. You can enable these operations by editing the relevant sections or removing the comment lines.

## Contribution
Pull requests are accepted. Please open an issue to discuss the topic before making any major changes.
