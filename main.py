from website import create_app

app = create_app()

# only if we run this file, app.run will be executed
if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")