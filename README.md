# pipfilter

[![PyPI Version](https://img.shields.io/pypi/v/pipfilter.svg)](https://pypi.org/project/pipfilter/)
[![License](https://img.shields.io/pypi/l/your-package-name.svg)](https://opensource.org/licenses/MIT)

A Python utility to filter top-level dependencies from an existing requirements.txt file, creating a new file containing only the essential dependencies, removing the package that would be installed from them. 

This will create a cleaner, simpler and more comprehensible requirements.txt.

## Installation

```bash
pip install pipfilter
```

## Usage

```
pipfilter <file.txt>
```

Replace `<file.txt>` with the path to your existing requirements.txt file. The script will create a new file named requirements.txt with only the top-level dependencies.


## How It Works

The script uses `pip show` to gather information about each installed package. It identifies top-level packages by checking if the "Required by" line is empty. The resulting top-level packages are then written to a new `requirements.txt` file.