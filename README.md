# Image to text convertor scripts using python

- First, search for the [Tesseract installer](https://tesseract-ocr.github.io/tessdoc/Installation.html) for your operating system. For Windows, you can find the latest version of Tesseract installer [here](https://github.com/UB-Mannheim/tesseract/wiki). Simply download the .exe file and install on your computer.
- Clone this repository by following command

Use ssh or http:

```bash
git clone git@github.com:SanjarbekSaminjonov/image-to-text.git
```

```bash
git clone https://github.com/SanjarbekSaminjonov/image-to-text.git
```

- Create and activate virutalenv

```
cd image-to-text && python -m virtualenv venv
```

```
venv\Scripts\activate  # on windows
source venv/bin/activate  # on a linux distro
```

- Install required packages

```
pip install -r requirements.txt
```

- And finally, run main.py

```
python main.py
```

### Upload images to '/images' folder
