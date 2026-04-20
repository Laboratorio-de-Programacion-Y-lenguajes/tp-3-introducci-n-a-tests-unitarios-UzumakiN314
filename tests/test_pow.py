"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8

# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (5, 0, 1.0),       # Cualquier número elevado a 0 es 1
    (8, 1, 8.0),       # Número elevado a 1 es el mismo número
    (-2, 2, 4.0),      # Base negativa con exponente par (positivo)
    (-2, 3, -8.0),     # Base negativa con exponente impar (negativo)
    (9, 0.5, 3.0),     # Exponente decimal (equivale a raíz cuadrada)
    (2, -1, 0.5)       # Exponente negativo (1/2)
])
def test_pow_parametrizado(a, b, expected):
    """Prueba diferentes casos de potencia."""
    assert pow_(a, b) == pytest.approx(expected)

# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
