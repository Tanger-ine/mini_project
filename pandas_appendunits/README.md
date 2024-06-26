# pandas_appendunits

pandas_appendunits is a Python package for performing file operations easily. It provides functions to manipulate files such as getting paths of files with specific names or extensions in a directory, and merging multiple files into a single DataFrame.

## Installation

You can install FileUtils using pip:

pip install pdappendunits

## Functions

### files_in_names

Get the paths of the files with the given names in the directory.

```python
import os

def files_in_names(directory, file_names):
    """
    Get the paths of the files with the given names in the directory.
    """
    file_paths = []
    for file_name in file_names:
        file_path = os.path.join(directory, file_name)
        if os.path.exists(file_path):  # Check if the file exists
            file_paths.append(file_path)
        else:
            print(f"File '{file_name}' not found in directory '{directory}'.")
    return file_paths
```

### files_in_extension

Get the paths of the files with the given extension in the directory.

```python
import os

def files_in_extension(directory, extension):
    """
    Get the paths of the files with the given extension in the directory.
    """
    file_paths = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            file_path = os.path.join(directory, file)
            file_paths.append(file_path)
    return file_paths
```

### merge_files

Merge the files into a single DataFrame.

```python
import pandas as pd

def merge_files(file_paths):
    """
    Merge the files into a single DataFrame.
    """
    file_list = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        file_list.append(df)
    if file_list:
        return pd.concat(file_list, ignore_index=True)
    else:
        return None
```

## Usage

Here's an example of how to use the functions:

```python

import pdappendunits as pdap

directory = "/path/to/your/directory"
file_names = ["file1.csv", "file2.csv"]  # List of file names
extension = ".csv"  # File extension

```

# Get paths of files with specific names

```python

file_paths = pdap.files_in_names(directory, file_names)

```

# Get paths of files with specific extension

```python

file_paths_with_extension = pdap.files_in_extension(directory, extension)

```

# Merge files into a single DataFrame

```python

data = pdap.merge_files(file_paths_with_extension)

print(data)

```