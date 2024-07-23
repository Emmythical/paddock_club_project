from app import create_app

# Create an instance of the Flask application
app = create_app()

# Entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Set debug=True for development purposes
