import matplotlib.pyplot as plt
import webbrowser

def latex_to_svg(latex_str, svg_path):
    fig = plt.figure(figsize=(6, 3))  # Adjust figure size as needed

    plt.axis("off")
    # Use either `size` or `fontsize`, but not both
    plt.text(0.5, 0.5, f"${latex_str}$", fontsize=20, ha="center", va="center")

    plt.savefig(svg_path, format="svg", bbox_inches="tight", pad_inches=0)
    plt.close(fig)

    print(f"SVG saved to {svg_path}")
    return webbrowser.open(svg_path)

# Specify the SVG path and the LaTeX formula
svg_path = "result.svg"
latex_formula = "M_{Rd} = \\frac{W_{el,y} \\cdot 10 \\cdot f_y}{\\gamma_{M0}}"

# Save the LaTeX formula as an SVG
svg_path = latex_to_svg(latex_formula, svg_path)

# Optionally, open the SVG in the default web browser
#webbrowser.open(svg_path)
