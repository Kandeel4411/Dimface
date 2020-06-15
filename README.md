# ***Dimface***
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Kandeel4411/Dimface/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Kandeel4411/Dimface/pulse)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A Personal script to automatically dim Window's screen brightness if no face is detected on the screen to save battery power.  
  
## Requirements
- Python 3.6+.
- **Windows**  
Note: Python must be included in the `PATH` Environment variable.

## Getting Started
- Clone the repo or click [here](https://github.com/Kandeel4411/Dimface/archive/master.zip) to download the zip file then extract it locally.
- Add the cloned repo directory to `PATH` Environment variable.
- Open the cloned repo in the terminal and run `pip install -r requirements.txt`.
- Run `dimface` in terminal

## Usage
- Run `dimface run --seconds <N>` in terminal replacing `<N>` with the amount of seconds between each frame taken that you want. i.e:
    ```
    dimface run --seconds 2
    ```

## Personal development
- [Install Make](http://gnuwin32.sourceforge.net/packages/make.htm) if you're on Windows. OSX already has it installed. Linux will tell you how to install it (i.e., `sudo apt-get install make`)
- [Install Poetry](https://github.com/python-poetry/poetry) for managing dependencies or just use python's `pip`.
  - If you want to disable poetry's `venv` creation run `make venv PY_VENV=false`.
  - If you want to add a new dependency run `make install DEP_NAME="<name>"` and replace `<name>` with the dependency's name.
  - if you want to export the updated dependencies to a `requirements.txt` file, run `make update-deps`.

## Acknowledgements
- [OpenCV](https://github.com/opencv/opencv)
