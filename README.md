Sensor Data Display with Flask and Socket.IO

This project demonstrates a real-time sensor data display using Flask and Socket.IO. It updates sensor readings dynamically to a web page without requiring a page refresh. This is ideal for real-time monitoring systems such as environmental data monitoring, industrial systems, or any application where sensor data is read and displayed in real-time.

Features
Real-Time Data Updates: Utilizes WebSockets via Socket.IO for live updating sensor values on the webpage.
Scalable Architecture: Easily scalable for additional sensors or more complex data processing.
Separation of Concerns: Uses Flask's render_template to separate HTML from Python code, enhancing readability and maintainability.
Requirements
Python 3.x
Flask
Flask-SocketIO
Eventlet or gevent (for production use)
Installation
Follow these steps to set up the project locally:

Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-project-repository.git
cd your-project-repository
Set Up a Virtual Environment (Optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

Copy code
pip install Flask Flask-SocketIO eventlet
Run the Application:

Copy code
python app.py
Usage
Once the application is running, navigate to http://localhost:5000/ in your web browser to view the real-time sensor data. The sensor data should update automatically without needing to refresh the page.

Project Structure
/templates
index.html: The main HTML file rendered by Flask.
app.py: Contains the Flask and Socket.IO setup and routes.
