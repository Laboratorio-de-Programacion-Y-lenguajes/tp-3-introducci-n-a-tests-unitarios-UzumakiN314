"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (10, 0, 0.0),      # Multiplicar por cero
    (-3, -4, 12.0),    # Multiplicar dos negativos
    (5, -2, -10.0),    # Positivo por negativo
    (8, 1, 8.0),       # Elemento neutro (1)
    (0.5, 2.0, 1.0),   # Decimales
    (2.5, 2.5, 6.25)   # Más decimales
])
def test_mul_parametrizado(a, b, expected):
    """Prueba diferentes casos de multiplicación."""
    assert mul(a, b) == pytest.approx(expected)

# Agregá tests para los siguientes casos:
#   - Multiplicar por cero / check
#   - Multiplicar dos números negativos (resultado positivo) / check
#   - Multiplicar un positivo y un negativo (resultado negativo) / check
#   - Multiplicar por 1 (elemento neutro) / check
#   - Multiplicar dos decimales (float) / check
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
