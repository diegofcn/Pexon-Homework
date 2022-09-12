from website import create_app
import os

app = create_app()

# only if we run this file, app.run will be executed
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv('PORT'))