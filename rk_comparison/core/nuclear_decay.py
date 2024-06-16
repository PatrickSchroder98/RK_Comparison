import math


class NuclearDecay:
    """This class contains the differential equation and analytical solution to the nuclear decay problem.
    Tau is a mean lifetime of a radioactive particle before decay.
    """

    tau = 1.0

    def equation(self, t, Nu):
        """Differential equation describing the nuclear decay problem. Source: [6] in bibliography."""
        return -(Nu / self.get_tau())

    def set_tau(self, tau):
        """Tau can be set by user with this method."""
        self.tau = tau

    def get_tau(self):
        """Returns the tau value."""
        return self.tau

    def equation_analytical(self, Nu0, t):
        """Analytical solution to the nuclear decay problem. Source: [6] in bibliography."""
        return Nu0 * pow(math.e, -(t / self.get_tau()))
