# Automated Testing Project

This repository contains an automation project designed to run tests for the technical test questions provided.

## Test Questions

The technical test questions can be found in the file: [QA Practical Test](doc\teste-pratico-qa-pleno.pdf).

## Answers and Analysis

The answers and detailed analysis for each screen can be found in the following locations:

- **Screen 1**: [Answer to the first question](template\first_screen/README.md)
- **Screen 2**: [Answer to the second question](template\second_screen/README.md)
- **Screen 3**: [Answer to the third question](template\third_screen/README.md)

Please refer to these files for specific instructions and insights related to each screen.

## Setting up a Virtual Environment

1. Check if Python is installed: Open your terminal and run the following command to check if Python is installed:

   ```bash
   python --version
   ```

    Note: if python is not installed, download and install [here](https://www.python.org/downloads/).

2. Run the following command to create a virtual environment named `venv`:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment using the command:

   ```bash
   .\venv\Scripts\activate
   ```
    The command to exit a virtual environment (venv) in Python is: `deactivate`

## Installing Dependencies

- Install the dependencies listed in the `requirements.txt` file using the following command:

   ```bash
   pip install -r requirements.txt
   ```
   
## Using Behave

### Running Tests

To run the tests, open a terminal and navigate to your project's root directory. Then, execute the following command:

    behave

## Customizing Test Execution
To customize test execution, follow these steps:

| Description                            | Command                                           |
|----------------------------------------|---------------------------------------------------|
| Run specific scenario                  | `behave -n "scenario_name"`                       |
| Run specific feature                   | `behave -i "file_name.feature"`                   |
| Set Browser                            | `$env:BROWSER="firefox" (default)`                |
| Set Headless Mode                      | `$env:HEADLESS_MODE="False" (default)`            |
| Set Server                             | `$env:SERVER="local" (default)`            |

## Cucumber Tags
Cucumber tags are used to mark scenarios or features for different purposes. Here are some tags used in the current context:

| Description                                       | Tag      |
|---------------------------------------------------|----------|
| Tests involving interactions on the web.          | `@web`   |
| Tests that are failing                            | `@xfail` |

Note: These tags are essential for the proper functioning of tests as they are utilized in the project's fixtures.
