from matplotlib import pyplot as plt

def L(x, dots):
	res = 0
	for i in range(len(dots)):
		P = 1
		for j in range(len(dots)):
			if i == j:
				continue
			P *= (x - dots[j][0])/(dots[i][0] - dots[j][0])
		res += P*dots[i][1]
	return res;

points = [[-6,-2],
		  [-5, 2],
		  [-4,-2],
		  [-3, 2],
		  [-2,-2],
		  [-1, 2],
		  [ 0, 0],
		  [ 1, 2],
		  [ 2,-2],
		  [ 3, 2],
		  [ 4,-2],
		  [ 5, 2],
		  [ 6,-2]]

X = []
Y = []

for x in range(-400,401,1):
	X.append(x/100)
	Y.append(L(x/100,points))
print(L(0,points))
plt.plot(X,Y)
plt.show()