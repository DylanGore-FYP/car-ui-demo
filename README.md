# Car UI Demo

A proof of concept UI for the in-vehicle portion of the project - [https://github.com/DylanGore-FYP/Car](https://github.com/DylanGore-FYP/Car).

## Requirements

- Python 3
- [eel](https://github.com/ChrisKnott/Eel)
- [chromedriver](https://chromedriver.chromium.org/)
- [Chromium Browser](https://www.chromium.org/Home) (Linux Only)

**Note:** The Chromium browser is required on Linux as it is possible to programmatically launch it in full screen mode whereas this was not working when using ChromeDriver. The code can be modified to use ChromeDriver on Linux if required.

## Running

```bash
pip3 install -r requirements.txt
```

```bash
python3 demo_ui.py
```
