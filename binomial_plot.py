# -*- coding: utf-8 -*-

def plot_binom_pmf(n=4, p=0.5):
    # There are n+1 possible number of "successes": 0 to n.
    x = range(n+1)
    y = stats.binom.pmf(x, n, p)
    plt.plot(x,y,"o", color="black")

    # Format x-axis and y-axis.
    plt.axis([-(max(x)-min(x))*0.05, max(x)*1.05, -0.01, max(y)*1.10])
    plt.xticks(x)
    plt.title("Binomial distribution PMF for tries = {0} & p ={1}".format(
            n,p))
    plt.xlabel("Variate")
    plt.ylabel("Probability")

    plt.draw()
    
plot_binom_pmf()