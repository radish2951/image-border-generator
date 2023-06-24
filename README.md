# Image Border Generator

Image Border Generator is a Python script that automatically adds a white border around all image files in a specified input folder. The size of the border is determined as a ratio of the original image's dimensions. The images with borders are then saved to a specified output folder.

## Installation

This script requires Python 3 and the Pillow library. It's recommended to run the script in a virtual environment to avoid package conflicts. Follow these steps to set up and run the script:

1. **Clone the repository**
```
git clone https://github.com/radish2951/image-border-generator.git
cd image-border-generator
```

2. **Set up a virtual environment and activate it**

On Linux/macOS:
```
python3 -m venv env
source env/bin/activate
```

On Windows:
```
python -m venv env
.\env\Scripts\activate
```

3. **Install the Pillow library**
```
pip install pillow
```

## Usage

In the script, replace 'input_images', 'output_images', and 0.05 in the last line with your actual input and output directory paths and the desired border ratio respectively. Save the changes.

Then run the script:
```
python script.py
```

The script will process all .jpg, .png, .jpeg files in the input directory, add borders to them, and save the results in the output directory. The name of the output files will be the same as the original files but with a '_bordered' suffix before the file extension. For example, image.jpg will become image_bordered.jpg.

## License

This project is licensed under the terms of the MIT license.
