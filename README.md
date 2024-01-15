# Hand Tracking AI

This project utilizes Python and computer vision libraries to track hand movements using a webcam. It also communicates with a microcontroller through serial communication to control external devices based on hand gestures.

## Prerequisites

- [Python](https://www.python.org/downloads/): Version 3.9.0 or later
- [OpenCV](https://pypi.org/project/opencv-python/): Install using `pip install opencv-python`
- [Mediapipe](https://pypi.org/project/mediapipe/): Install using `pip install mediapipe`
- [PySerial](https://pypi.org/project/pyserial/): Install using `pip install pyserial`

## Installation

1. **Install Python:**
   - Download and install Python from [Python Downloads](https://www.python.org/downloads/).
   - During installation, select "Add Python to PATH" and choose a custom installation with all options enabled.

2. **Verify Python Installation:**
   - Open a command prompt and check Python and pip versions:
     ```bash
     python --version
     pip --version
     ```

3. **Open IDLE:**
   - Search for "IDLE" in the Windows menu and create a new Python script.

4. **Install Libraries:**
   - Install OpenCV, Mediapipe, and PySerial using the following commands:
     ```bash
     pip install opencv-python
     pip install mediapipe
     pip install pyserial
     ```

5. **Clone the Repository:**
   - Clone or download the [Hand_tracking_AI](https://github.com/Shivani9698/Hand_tracking_AI) repository.

6. **Run the Code:**
   - Open the Python script in IDLE and run the code.

## Usage

1. Run the Python script to start hand tracking using your webcam.
2. Ensure that a compatible webcam is connected.
3. Adjust the serial port in the Python code based on your microcontroller connection.

## Contributing

If you'd like to contribute to this project, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This project uses the [Mediapipe](https://mediapipe.dev/) library for hand tracking.

