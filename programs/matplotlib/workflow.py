import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(x, y, color="lightblue", linewidth=2)

# x1 = [2,4,6]
# y1 = [5,15,25]
# ax.scatter(x1, y1, color="darkgreen", markers="^")
# ax.set_xlim(1, 6.5)

plt.savefig("foo.png")
plt.show()