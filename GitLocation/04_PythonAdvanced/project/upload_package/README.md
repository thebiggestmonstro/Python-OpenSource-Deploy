# pygifconvt

## Table of Contents
  * [Installation](#installation)
  * [Quick start](#quick-start)
  * [Features](#features)
  
## Installation

Download using pip via pypi.

```bash
$ pip install 'package' --upgrade
  or
$ pip install git+'repository'
```
(Mac/homebrew users may need to use ``pip3``)


## Quick start
```python
 >>> from pygifgenerator_testver.gifgenerator import GIFGenerator
 >>> c = GIFGenerator("your original images path", 'your gif output path', (320,240))
 >>> c.generate_gif()
```

## Features
  * Python library to convert single oder multiple frame gif images
  * OpenCV does not support gif images.