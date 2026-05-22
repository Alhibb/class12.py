import matplotlib.pyplot as plt
import numpy as np

states = ["Lagos", "Kano", "Kaduna"]

APC = [12000, 15000, 8000]
PDP = [10000, 14000, 9000]
LP = [9000, 11000, 7000]

states1 = ["Jos", "Bauchi", "Nasarawa"]

APC1 = [12000, 15000, 8000]
PDP1 = [10000, 14000, 9000]
LP1 = [9000, 11000, 7000]

x = np.arange(len(states))  # positions for states
x1 = np.arange(len(states1))  # positions for states
width = 0.25  # width of each bar

plt.figure(figsize=(12, 8))

plt.subplot(1, 2, 1)
plt.bar(x - width, APC, width=width, label="APC")
plt.bar(x,         PDP, width=width, label="PDP")
plt.bar(x + width, LP, width=width, label="LP")
plt.xlabel("States")
plt.ylabel("Votes")
plt.legend()
plt.xticks(x, states)

plt.subplot(1, 2, 2)
plt.bar(x1 - width, APC1, width=width, label="APC")
plt.bar(x1,         PDP1, width=width, label="PDP")
plt.bar(x1 + width, LP1, width=width, label="LP")

plt.xticks(x1, states1)
plt.xlabel("States")
plt.ylabel("Votes")
plt.title("Election Results by State")
plt.legend()

plt.show()