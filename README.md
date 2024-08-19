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

python3.12 run.py
```
The server will start at http://localhost:5000
API Endpoints

    POST /add_settings: Add new settings to the application.

Example to create a new settings values:

```sh

curl -X POST -H "Content-Type: application/json" -d '{"tolerance":"5","setpoint_min":"86","setpoint_max":"130",
"setpoint_offset_summer":"25","setpoint_offset_winter":"29",
"mode_change_delta_temp":"2","mode_switch_lockout_time":"-1",
"cascade_time":"11"}'  http://localhost:5000/add_settings

```

Example to get a particular configuration of the setting values filtering by id
Please note you have chronos.db with some examples

```sh

curl -X GET http://localhost:5000/settings/1
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
