from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

size = 5000
%number of points

X = 10*random.rand(size)
Y = 10* random.rand(size)
Z = 2*pi*random.rand(size)
%randomly selected points; x and y are between 0 and 10, z is an angle.

kernel = zeros((size, size))
epsilon = 10

for i in range(size):
	for j in range(size):
		a = abs(Z[i] - Z[j])
		b = abs(Y[i] - Y[j] + Z[i]*(X[i] - X[j]))
		c = abs(Y[i] - Y[j] + Y[i]*Z[j] - Z[i]*Y[j] + Z[i]*(X[i]*Z[j] - X[j]*Z[i]))
		d = a + b + sqrt(c)
		e = abs(Z[j] - Z[i])
		f = abs(Y[j] - Y[i] + Z[j]*(X[j] - X[i]))
		g = abs(Y[j] - Y[i] + Y[j]*Z[i] - Z[j]*Y[i] + Z[j]*(X[j]*Z[i] - X[i]*Z[j]))
		h = e + f + sqrt(g)
		k = 0.5*(h + d)
		kernel[i, j] = exp(-k / epsilon)



D = zeros((size, size))
degrees = [sum(kernel[i]) for i in range(size)]
fill_diagonal(D, degrees)

%markov chain, not symmetric
markov = dot(linalg.inv(D), kernel)

eigvals, eigvecs = linalg.eig(markov)
%these are unsorted!
idx = eigvals.argsort()
eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('first eigenvector')
ax.set_ylabel('second eigenvector')
ax.set_zlabel('third eigenvector')
ax.scatter(eigvecs[997], eigvecs[998], eigvecs[999])
plt.show()

t = 1
diffusion = zeros((size, size))
for i in range(size):
	for j in range(size):
		for k in range(20):
			eigvec = eigvecs[k]
			eigval = eigvals[k]
			diffusion[i, j] = diffusion[i, j] + eigval**(2*t)*(eigvec[i]-eigvec[j])**2
		diffusion[i, j] = sqrt(diffusion[i, j])

fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Diffusion distance, t = 1')
ax.scatter(X, Y, diffusion[0, :])
plt.show()

diffeigvals = [eigval**t for eigval in eigvals]
diffeigvecs = zeros((size, size))
for i in range(size):
	diffeigvecs[i, :] = diffeigvals[i]*eigvecs[i, :]

