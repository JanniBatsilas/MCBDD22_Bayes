from random import seed
import numpy as np
import matplotlib.pyplot as plt
import ctypes


class Simulation:

    def __init__(self, p_min, p_max, p_inc, spec, sens):

        self.prevalence = np.arange(p_min, p_max, p_inc, dtype=float)
        self.spec = spec
        self.sens = sens
        self.values = []


    def calculate(self):

        for i in range(len(self.spec)):
            spec_i = self.spec[i]
            result = []
            for prev in self.prevalence:
                # P(infected | test positive)
                p = (self.sens * prev) / ((1-spec_i) * (1-prev) + (self.sens) * (prev))
                result.append(p)
            self.values.append(result)


    def show_plot(self):

        for i in range(len(self.spec)):
            label_string = "Specificity = " + str(self.spec[i])
            plt.plot(self.prevalence, self.values[i], label=label_string)

        plt.xlabel("prevalence")
        plt.ylabel("P(infected)")
        plt.title("Fixed sensitivity of 0.99")
        plt.legend()
        plt.show()


if __name__ == '__main__':
    seed(84)

    prevalence_min = 0.001
    prevalence_max = 0.5
    prevalence_inc = prevalence_min

    specitivity = [0.99, 0.999, 0.99999]
    sensitivity = 0.99

    sim = Simulation(prevalence_min, prevalence_max, prevalence_inc, specitivity, sensitivity)
    sim.calculate()
    sim.show_plot()

    ctypes.windll.user32.MessageBoxW(0, "Assuming we have tested 10'000 Persons and given sensitivity and specitivity "
                                        "(99%) and a prevalence of 5%. \n "
                                        "\n #PositiveDiseased = 0.99*500 = 495, "
                                        "\n #NegativeNoDisease = 0.99*9500 = 9405 "
                                        "\n #FN = 5"
                                        "\n #FP = 95"
                                        "\n P(infected | positive Test) = 495 / (495 + 95) = 0.84"
                                        "\n The same value can be read from the plot seen before.", "Integer Calculation", 1)




