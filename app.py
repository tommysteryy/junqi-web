from flask import Flask, render_template, request, jsonify
import junqi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    data = request.get_json()
    
    redCard = data['red']
    blackCard = data['black']

    if junqi.isInvalid(redCard):
        result = "The RED card name is invalid. Please try again."
    elif junqi.isInvalid(blackCard):
        result = "The BLACK card name is invalid. Please try again."
    else:
        winner, isGameOver = junqi.fight(redCard=redCard, blackCard=blackCard)

        print(winner.name)
        print(isGameOver.value)

        if (isGameOver.value):
            result=f"{winner.name} has won the game!"
        elif (winner.name == "SELF_DESTRUCT"):
            result="Red and Black self destruct."
        elif (winner.name == "IMPOSSIBLE"):
            result="This combination of cards is impossible. Please recheck both of your inputs."
        else:
            result=f"{winner.name} has the larger piece."
            
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.debug=True
    app.run()
