# Image Analysis API with DeepFace for Flask 

This is a simple Flask-based API for analyzing images using the DeepFace library to determine the gender of the first detected face. 

## Features
- Analyze images to detect faces and their attributes (age, gender, race, emotion).
- Supports multiple image formats (png, jpg, jpeg).
- Error handling for various scenarios.

## Getting Started

These instructions will help you set up and test the API on your local machine.

### Prerequisites

Before getting started, make sure you have the following installed:

- Python (3.10 or higher)
- Flask
- DeepFace
- Postman (for testing the API)

### Installation

1. Clone this repository to your local machine.

2. Change to the project directory.

3. Install the required Python libraries. 


### Usage

1. Start the Flask app:

```python main.py```  

2. Change the path where the image must be saved.
```UPLOAD_FOLDER = r'C:\Users\Dell\PycharmProjects\flaskproject\sample'``` to any path of your choice.

The app will be running at http://localhost:5000.

3. Use Postman or any API client to test the '/analyze' endpoint.

- Send a POST request to `http://localhost:5000/analyze` with a form-data parameter named `file` containing an image file (in either PNG, JPG, or JPEG format).

4. You will receive a JSON response with the gender of the first detected face, or an error message if no faces are detected or if there is an issue with the image analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




## Credits
Sincere Thanks to [Sefik Ilkin Serengil](https://github.com/serengil).
