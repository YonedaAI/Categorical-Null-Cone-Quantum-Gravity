# /// script
# requires-python = ">=3.10"
# dependencies = ["scipy==1.14.1"]
# ///
"""Reproduce the ordered amplitudes and optical areas in the marked-cut supplement."""
from cmath import exp, isclose
from math import inf, pi, sin, sinh, sqrt

from scipy.integrate import quad_vec, solve_ivp


def check_orders(a, b, center, momentum, width):
    # The numerical examples use units with hbar = 1.
    if width <= 0:
        raise ValueError("A normalizable Gaussian needs a positive width")

    def state(q):
        offset = q - center
        return (2 * pi * width**2) ** (-0.25) * exp(
            -offset**2 / (4 * width**2) + 1j * momentum * offset
        )

    expected = exp(
        -a**2 / (8 * width**2) - (width * b) ** 2 / 2
        + 1j * (b * (center - a / 2) + momentum * a)
    )
    for name, shift, exact in (("M U", 0, expected), ("U M", a, exp(1j * a * b) * expected)):
        def integrand(q):
            return state(q).conjugate() * exp(1j * b * (q + shift)) * state(q + a)

        value, error, info = quad_vec(integrand, -inf, inf, epsabs=1e-12, epsrel=1e-12,
                                      full_output=True)
        if not info.success or not isclose(value, exact, rel_tol=1e-10, abs_tol=1e-10):
            raise ValueError(f"{name} integral {value}, expected {exact}, estimated error {error}")
        print(f"{name} expectation {value:.12g}")


def check_optics(kappa, inner, outer):
    if kappa < 0 or not 0 < inner < outer or kappa * outer >= pi:
        raise ValueError("Choose nonnegative curvature scale and regular cuts before the caustic")

    # B'' = diag(kappa², -kappa²) B with vertex data B(0) = 0 and B'(0) = I.
    def derivatives(u, state):
        x, dx, y, dy = state
        return dx, kappa**2 * x, dy, -kappa**2 * y

    cuts = (inner, outer)
    solution = solve_ivp(derivatives, (0, outer), (0, 1, 0, 1), t_eval=cuts, method="DOP853",
                         rtol=1e-12, atol=1e-14)
    if not solution.success:
        raise ValueError(solution.message)
    areas = solution.y[0] * solution.y[2]
    for cut, area in zip(cuts, areas, strict=True):
        exact = cut**2 if kappa == 0 else sinh(kappa * cut) * sin(kappa * cut) / kappa**2
        if not isclose(area, exact, rel_tol=1e-10, abs_tol=1e-12):
            raise ValueError(f"Jacobi determinant at {cut} is {area}, expected {exact}")
    print(f"kappa={kappa:g}, cuts {inner:g}, {outer:g}: area ratio {areas[1] / areas[0]:.12g}")


if __name__ == "__main__":
    check_orders(sqrt(pi), sqrt(pi), 0, 0, 1)
    check_orders(0.51, -0.38, 0.4, 1.1, 0.85)
    check_optics(0, 0.5, 1.25)
    check_optics(0.4, 0.5, 1.25)
    check_optics(1, 0.3, 1.6)
