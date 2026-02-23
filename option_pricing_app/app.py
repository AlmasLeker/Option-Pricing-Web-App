from flask import Flask, render_template, request
from pricer import monte_carlo_price, black_scholes_price

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/price', methods =['POST'])
def price():
    S = float(request.form['S'])
    K = float(request.form['K'])
    r = float(request.form['r'])
    sigma = float(request.form['sigma'])
    T = float(request.form['T'])
    N = int(request.form['N'])

    mc_price, std_error = monte_carlo_price(S, K, r, sigma, T, N)
    bs_price = black_scholes_price (S,K,r,sigma,T)

    return render_template('result.html',
                            mc_price = mc_price,
                            std_error= std_error,
                            bs_price = bs_price)
if __name__ == '__main__':
    app.run(debug = True)

