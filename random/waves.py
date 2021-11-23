# Let's make waves


#Re-write this as a class/add to our randomPlotter class
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


X = np.linspace(0,100,100)
Y = np.linspace(0,1,100)
def chaos(x, mu, sig):
	return np.sin((X **2) * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))

def alt_chaos(x, mu, sig):
	return np.cos(X * np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))))

def gauss(x, mu, sig):
	return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


f,ax = plt.subplots(figsize = (8,5))
ax.set_xticks([])
ax.set_yticks([])
ax.plot(X, chaos(X,15,30))
ax.plot(X, np.full(100,0), color = 'green')
ax.plot(X, alt_chaos(X, 24, 60), color = "#59af62")
ax.plot(X, -alt_chaos(X, 50, 30), color = "#59af62")
ax.plot(X, np.sin(X**2), color = "#096813")
ax.plot(X, np.cos(X**2), color = "#447c4a")
ax.plot(np.full(100, 50),Y, color = '#5a9991')
# plt.show()


# Gaussian wave plot - random colors
mu_values = np.random.random_integers(low = 0, high = 100, size = 100)
sigma_values = np.random.random_integers(low = 0, high = 100, size = 100)
# print(mu_values)

f, ax = plt.subplots(figsize = (8,5))
ax.set_title('Waves')
ax.set_xticks([])
ax.set_yticks([])
#for m, s in zip(mu_values, sigma_values):
#	ax.plot(X, gauss(X, m, s))

# plt.show()


# Gaussian wave plot - reds/oranges
mu_values = np.random.random_integers(low = 0, high = 100, size = 100)
sigma_values = np.random.random_integers(low = 0, high = 100, size = 100)
# print(mu_values)

f, ax = plt.subplots(figsize = (8,5))
ax.set_xticks([])
ax.set_yticks([])
#for m, s in zip(mu_values, sigma_values):
#	ax.plot(X, gauss(X, m, s))
#	ax.plot(X, -gauss(X, m, s))
## plt.show()


# Same color scheme gaussians
red = np.linspace(0.100,0.1)
green = np.linspace(0.200,0.1)
blue = np.linspace(0.210,0.1)

f, ax = plt.subplots(figsize = (8,5))
# ax.set_title('Waves')
ax.set_xticks([])
ax.set_yticks([])
plt.show()

#for m, s in zip(mu_values, sigma_values):
#
#	ax.plot(X, gauss(X, m, s), color = sns.palplot(sns.color_palette("Blues")))











