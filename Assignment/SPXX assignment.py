import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.animation as animation

spxx = yf.Ticker("SPXX")
hist = spxx.history(period="1y")

fig, ax = plt.subplots(figsize=(16, 8))
ax.set_title("SPXX Stock Price (Last Year)", fontsize=16, fontweight='bold')
ax.set_xlabel("Date", fontsize=12, fontweight='bold')
ax.set_ylabel("Price (USD)", fontsize=12, fontweight='bold')
ax.set_facecolor('#f7f7f7')
ax.grid(True, which='both', axis='both', color='gray', linestyle='--', linewidth=0.5)

line, = ax.plot([], [], lw=2, marker='o', markersize=3, color='#0C5489')

ax.set_xlim(hist.index[0], hist.index[-1])
ax.set_ylim(hist['Close'].min(), hist['Close'].max())

def update(frame):
    line.set_data(hist.index[:frame], hist['Close'][:frame])
    return line,

ani = animation.FuncAnimation(
    fig, update, frames=len(hist), interval=50, blit=True
)

ax.fill_between(hist.index, hist['Close'], color='#52A1DB', alpha=0.1)

plt.show()