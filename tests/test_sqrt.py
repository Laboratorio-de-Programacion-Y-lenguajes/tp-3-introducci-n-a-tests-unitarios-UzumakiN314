"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---

@pytest.mark.parametrize("x, expected", [
    (0, 0.0),            # Raíz de cero
    (2, 1.41421356),     # No es cuadrado perfecto (decimal)
    (0.25, 0.5),         # Raíz de un decimal
    (1, 1.0)             # Raíz de uno
])
def test_sqrt_casos_varios(x, expected):
    """Prueba raíces comunes y decimales."""
    assert sqrt(x) == pytest.approx(expected)

def test_sqrt_negativo():
    """Verifica que la raíz de un negativo lance ValueError."""
    with pytest.raises(ValueError):
        sqrt(-4)

# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0) / check
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal) / check
#   - Raíz de un número negativo → debe lanzar ValueError / check
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)
