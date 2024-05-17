import scipy
import read_pandas
path = "data//"
df = read_my_csv(path)
peaks = scipy.signal.find_peaks(df, height=340)
print("Hallo")
print(peaks)