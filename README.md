# G-QR

This project is a G-QR is a QR code generator that allows users to create QR codes easily through a graphical user interface (GUI) built with Tkinter.
<img src="https://raw.githubusercontent.com/HarshYadav152/resources/main/images/G-QR/G-qr.png" />

## Project Structure

```
qr-generator
├── src
│   ├── main.py          # Main entry point for the QR code generator
│   └── gui
│       └── __init__.py  # GUI components for the QR code generator
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

To set up the project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Run the main application by executing the following command:

   ```
   python src/main.py
   ```

2. The GUI will open, allowing you to input the data you want to encode in the QR code.

3. After entering the data, click the "Generate" button to create the QR code.

4. The generated QR code will be displayed, and you can save it to your desired location.

## Dependencies

This project requires the following Python libraries:

- `qrcode`: For generating QR codes.
- `tkinter`: For creating the graphical user interface.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!
