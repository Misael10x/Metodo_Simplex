from flask import Flask, render_template, request
import pandas as pd
from scipy.optimize import linprog

app = Flask(__name__)

def simplex_method(c, A, b):
    res = linprog(c, A_ub=A, b_ub=b, method='simplex')
    df = pd.DataFrame({
        'Variable': ['x1', 'x2'],
        'Valor': res.x
    })
    return res, [df]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simplex', methods=['POST'])
def simplex():
    c = [float(request.form['c1']), float(request.form['c2'])]
    A = [[float(request.form['a11']), float(request.form['a12'])],
         [float(request.form['a21']), float(request.form['a22'])]]
    b = [float(request.form['b1']), float(request.form['b2'])]

    resultado, tablas = simplex_method(c, A, b)

    return render_template('resultado.html', resultado=resultado, tablas=tablas)

if __name__ == '__main__':
    app.run(debug=True)
