import math
import matplotlib
import matplotlib.pyplot as plt
import webbrowser
import seaborn as sns
import numpy as np  # Added import for numpy
matplotlib.use('TkAgg')  # Or 'Qt5Agg', 'GTK3Agg', etc., depending onsystem
import latexify



def latex_to_svg(latex_str, svg_path):
    fig = plt.figure(figsize=(6, 3))  # Adjust figure size as needed

    plt.axis("off")
    # Use either `size` or `fontsize`, but not both
    plt.text(0.5, 0.5, f"${latex_str}$", fontsize=20, ha="center", va="center")

    plt.savefig(svg_path, format="svg", bbox_inches="tight", pad_inches=0)
    plt.close(fig)

    print(f"SVG saved to {svg_path}")
    return webbrowser.open(svg_path)


# Latexify configuration for matplotlib
def latexify(fig_width=None, fig_height=None, columns=1):
    assert columns in [1, 2]
    if fig_width is None:
        fig_width = 3.39 if columns == 1 else 6.9
    if fig_height is None:
        golden_mean = (math.sqrt(5)-1.0)/2.0
        fig_height = fig_width * golden_mean
    MAX_HEIGHT_INCHES = 16.0
    if fig_height > MAX_HEIGHT_INCHES:
        print(f"WARNING: fig_height too large: {fig_height} so will reduce to {MAX_HEIGHT_INCHES} inches.")
        fig_height = MAX_HEIGHT_INCHES
    params = {
        'backend': 'pdf',
        'pgf.texsystem': 'pdflatex',
        'text.usetex': True,
        'pgf.rcfonts': False,
        'pgf.preamble': '\\\\usepackage{gensymb}\n\\\\usepackage[dvipsnames]{xcolor}',
        'figure.figsize': [fig_width, fig_height],
        'font.family': 'serif',
    }
    matplotlib.rcParams.update(params)

# Ensure seaborn's aesthetic settings are applied
sns.set_style("white")
sns.set_palette(sns.color_palette("cubehelix", 8))

# SteelSection class
class SteelSection:
    def __init__(self, name, area, Iy, Wel_y, fy=275, gamma_M0=1.0):
        self.name = name
        self.area = area
        self.Iy = Iy
        self.Wel_y = Wel_y
        self.fy = fy
        self.gamma_M0 = gamma_M0

    def calculate_bending_resistance(self):
        return (self.Wel_y * 10 * self.fy) / self.gamma_M0

    def calculate_shear_resistance(self):
        return (0.6 * self.area * 10 * self.fy) / (math.sqrt(3) * self.gamma_M0)

    def calculate_axial_resistance(self):
        return (self.area * 10 * self.fy) / self.gamma_M0

# ExtendedSteelSection class
class ExtendedSteelSection(SteelSection):
    def __init__(self, name, area, Iy, Wel_y, iy, L, fy=275, gamma_M1=1.0, E=210000):
        super().__init__(name, area, Iy, Wel_y, fy, gamma_M0=gamma_M1)
        self.iy = iy
        self.L = L
        self.E = E
        self.gamma_M1 = gamma_M1

    def critical_buckling_force(self):
        leff = self.L * 100
        pi_square_EI = math.pi**2 * self.E * self.Iy

        return pi_square_EI / (leff**2)

    def buckling_utilization(self, N_Ed):
        N_b_Rd = self.critical_buckling_force() / self.gamma_M1
        return N_Ed / N_b_Rd

    def lateral_torsional_buckling_utilization(self, M_Ed):
        M_LTb_Rd = self.calculate_bending_resistance() * 0.9
        return M_Ed / M_LTb_Rd


# Example usage of SteelSection and ExtendedSteelSection
if __name__ == "__main__":
    # Create an instance of SteelSection
    section = SteelSection("IPE 300", 7760, 1.84e6, 326, fy=275, gamma_M0=1.0)

    # Calculate and print bending, shear, and axial resistances
    print(f"Bending resistance of {section.name}: {section.calculate_bending_resistance()} kNm")
    print(f"Shear resistance of {section.name}: {section.calculate_shear_resistance()} kN")
    print(f"Axial resistance of {section.name}: {section.calculate_axial_resistance()} kN")

