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
        result = "红牌输入错误，请重新输入"
    elif junqi.isInvalid(blackCard):
        result = "黑牌输入错误，请重新输入"
    else:
        winner, isGameOver = junqi.fight(redCard=redCard, blackCard=blackCard)

        if (isGameOver.value):
            if (winner.name == "RED"):
                result="红方抗走了黑方的军旗，黑方全军覆没！红方获胜！"
            else:
                result="黑方抗走了红方的军旗，红方全军覆没！黑方获胜！"
        elif (winner.name == "SELF_DESTRUCT"):
            result="红牌与黑牌同归于尽!"
        elif (winner.name == "IMPOSSIBLE"):
            result="这两张牌不可能相遇，请双方再次核实后重新输入"
        elif (winner.name == "RED"):
            result="红牌战胜了黑牌!"
        elif (winner.name == "BLACK"):
            result="黑牌战胜了红牌!"
        else:
            result="网站发生了某些异常，请告知 Tommy (github.com/tommysteryy)，谢谢"

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.debug=True
    app.run()
