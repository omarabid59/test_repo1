# Code Repository Structure
This document outlines how to structure your repository so it can be used as a package. Alternatively, this repository can be used as a template.

Structure your repository as follows. Change the `my_package_name` to reflect your package name. Change the name of the `project_namespace` folder. Once, this is done, open up the file `setup.py`, and edit according to your project.
```
my_repository_dir/
  src/
    project_namespace/
      my_package_name/
        __init__.py
        some_file.py
      tests/
  setup.py
  requirements.txt
  README.md
```


## Example
Let's assume we have a repository that's responsible for object detection. Let's also assume that we have two object detectors we want to experiment with - CenterNet and a TensorFlow based one. We may decide to structure our repository like this. Notice how we have a `abstract_detector.py` file. This acts as an abstract class that defines a standard 

```
my_repository_dir/
  src/
    project_namespace/
      tests/
         test_od.py
      object_detection/
        __init__.py
        tensorflow/
          __init__.py
          detector.py
          other files ...
        center_net/
          __init__.py
          detector.py
          other files ...
        detector_interface.py
  setup.py
  requirements.txt
  README.md
```

### Interface Pattern
In order to have a consistent input/output structure for a given function, we use an Interface class to define this.

See the `detector_interface.py` and `detector.py` files for the interface and an example implementation respectively.

## Installation
To use this as a package, run the following command from the directory that this `README.md` file is located.

```
pip install .
```

### Install via GitHub
To install this package directly from a GitHub repository run:
```
pip install git+https://git@github.com/my_organization/my_repo.git
```

## Running Unit Tests with PyTest
After the package has been installed with the instructions as shown above, run the unit tests as follows.
```
pytest --pyargs project_namespace.object_detection
```

## Example Usage
Below is an example usage of this object detection package.
```
from project_namespace.object_detection.center_net.detector import CenterNet
import numpy as np


detector = CenterNet()

# Load the frozen graph
detector.load_model('frozen_graph.pb')

# Create a dummy image that we will pass into our detector module
image_np : np.ndarray = np.zeros(shape=(640, 480, 3))

# Run inference once, and return an object containing the detected data (bbs, classes, scores)
detector_data = detector.detect(image_np)
```


