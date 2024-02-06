from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('test.html')


@app.route('/virtualcompanion')
def run_python_program():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\ai_companion.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 


@app.route('/ai_mouse')
def ai_mouse():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\HandGestures.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 

@app.route('/ascii_art')
def ascii_art():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\ascii.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 
   

@app.route('/snake')
def Snake():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\snakeGame.py'], capture_output=True, text=True)

    return result.stdout 

@app.route('/sign')
def Sign():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\sign recogniton2\\Sign Detection.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 

@app.route('/face_recognition')
def face():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\faces\\face.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 

@app.route('/keyboard')
def keyboard():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\ai_keyboard.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 

@app.route('/fire')
def fire():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\fire detection\\f.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 



if __name__ == '__main__':
    app.run(debug=True)