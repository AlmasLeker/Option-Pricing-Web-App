import numpy as np
from scipy.stats import norm

def monte_carlo_price(S,K,r, sigma, T, N):
    Z = np.random.standard_normal(N)
    ST = S * np.exp((r - 0.5 * sigma**2)*T + sigma*np.sqrt(T)*Z)

    payoff = np.maximum(ST - K,0)
    discounted = np.exp(-r * T)*payoff

    price = np.mean(discounted)
    std_error = np.std(discounted) / np.sqrt(N)
    return price, std_error

def black_scholes_price(S, K, r, sigma, T):
    d1 = (np.log(S/K) + (r+0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    return price