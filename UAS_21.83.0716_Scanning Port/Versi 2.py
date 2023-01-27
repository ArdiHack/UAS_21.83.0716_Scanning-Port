import pandas as pd
import matplotlib.pyplot as plt

# Membaca data log jaringan dari file CSV
df = pd.read_csv("network_log.csv")

# Menghitung jumlah request dari setiap IP
df["count"] = df.groupby("src_ip")["src_ip"].transform("count")

# Membuat histogram jumlah request
plt.hist(df["count"], bins=50)
plt.xlabel("Jumlah Request")
plt.ylabel("Jumlah IP")
plt.show()
