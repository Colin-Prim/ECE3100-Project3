import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array, percentile, sqrt


class Trip:
    def __init__(self, time, speed, name='Unnamed Trip'):
        self._time = time
        self._speed = speed
        self._name = name

        #  flag variables for easy comparison
        self.min = 0
        self.q1 = 0
        self.median = 0
        self.q3 = 0
        self.max = 0

        #  automatically calculate 5-number summary upon init
        self._calculate_five_number_summary()

    def __sub__(self, other):
        """Calculates Euclidean distance (√Σ dist²) between the 5-number summary of two data sets"""
        distances_squared = [(self.min - other.min) ** 2,
                             (self.q1 - other.q1) ** 2,
                             (self.median - other.median) ** 2,
                             (self.q3 - other.q3) ** 2,
                             (self.max - other.max) ** 2]
        return sqrt(sum(distances_squared))

    def __str__(self):
        return f"{self._name: ^12}\n" \
                      f"{'Min:': <8}{self.min: .2f}\n" \
                      f"{'Q1:': <8}{self.q1: .2f}\n" \
                      f"{'Median:': <8}{self.median: .2f}\n" \
                      f"{'Q3:': <8}{self.q3: .2f}\n" \
                      f"{'Max:': <8}{self.max: .2f}"

    def plot_trip(self):
        """Public method to plot the set of data from a trip. This function closes the plot after it is shown
        so new plots are not affected by it."""
        #  plot data
        plt.plot(self._time, self._speed)
        #  label axes
        plt.xlabel('Time (m/s)')
        plt.ylabel('Speed (km/hr)')
        plt.title(self._name)
        plt.show()
        #  close window
        plt.close()

    def box_plot_trip(self):
        """Public method to make a boxplot of speed from a trip. This function closes the plot after it
        is shown soo new plots are not affected by it."""
        sns.boxplot(self._speed)
        plt.ylabel('Speed (km/hr)')
        plt.title(self._name)
        plt.show()

    def _calculate_five_number_summary(self):
        """Calculates 5-number summary"""
        self.min = min(self._speed)
        self.q1 = percentile(self._speed, 25)
        self.median = percentile(self._speed, 50)
        self.q3 = percentile(self._speed, 75)
        self.max = max(self._speed)


def main():
    dictionary_of_trips = {}
    for i in range(1, 7):
        file_name = '15minTrip' + str(i)
        df = pd.read_csv(file_name + '.csv')
        dictionary_of_trips[i] = Trip(df['Time'].to_numpy(), df['Vehicle speed'].to_numpy(), file_name)

        dictionary_of_trips[i].plot_trip()
        dictionary_of_trips[i].box_plot_trip()
        print(dictionary_of_trips[i])
        print()

    for i in range(1, 7):
        for j in range(1, 7):
            if j == i:
                continue
            else:
                print(f"The Euclidean distance between trip {i} and trip {j} is "
                      f"{dictionary_of_trips[i] - dictionary_of_trips[j]: .2f}")


if __name__ == "__main__":
    main()
