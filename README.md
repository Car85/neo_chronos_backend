# Neo Chronos Backend
Chronos is a boiling/cooling water system working on Raspberry Pi. Chronos has a web interface to control the system and tracking for the state. 

https://bitbucket.org/quarck/chronos

Backend service for the modernized Chronos application, implemented with Flask, Python 3.12.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Neo Chronos Backend is the server-side component of the Chronos application. It provides RESTful APIs for managing application settings and other backend functionalities using Flask.

## Features

- **RESTful API:** Provides a robust API for interacting with the Chronos application.
- **Database Integration:** Uses SQLite for data storage.
- **Modular Design:** Easy to extend and maintain.

## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

- Python version 3.12
- pip (Python package installer)

### Installation

1. Clone the repository:

```sh
   git clone https://github.com/Car85/neo_chronos_backend.git
   cd neo_chronos_backend
```

2. Create a virtual environment:

```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
Install the required packages:

```sh
    pip install -r requirements.txt
```
Usage
Running the Server

Start the Flask server:

```sh

flask run
```
The server will start at http://localhost:5000.
API Endpoints

    POST /add_settings: Add new settings to the application.

Example:

```sh

curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://localhost:5000/add_settings
```
Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

    Fork the Project
    Create your Feature Branch (git checkout -b feature/AmazingFeature)
    Commit your Changes (git commit -m 'Add some AmazingFeature')
    Push to the Branch (git push origin feature/AmazingFeature)
    Open a Pull Request

License

GPL 2.0

Maintainer: Car85
