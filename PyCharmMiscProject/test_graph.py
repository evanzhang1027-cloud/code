import matplotlib.pyplot as plt

print("Starting graph test...")

plt.plot([1, 2, 3, 4], [10, 20, 15, 30])
plt.title("Test Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()

print("Finished.")