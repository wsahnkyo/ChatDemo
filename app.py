from flask import Flask, render_template,  request,jsonify

from chat.ChatModel import ChatModel

app = Flask(__name__)


chat = ChatModel()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET','POST'])
def get_response():
    json_data = request.get_json()
    prompt = json_data.get('prompt')
    history = json_data.get('history')

    response,history =chat.getResult(prompt,history);
    data = {
        "response": response,
        "history": history
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()