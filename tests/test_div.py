"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 2.5),
    (-10, 2, -5.0),
    (10, -2, -5.0),
    (-10, -2, 5.0),
    (0, 5, 0.0)
])
def test_div_parametrizado(a, b, expected):
    """Prueba divisiones comunes y con signos."""
    assert div(a, b) == pytest.approx(expected)

def test_div_por_cero():
    """Verifica que dividir por cero lance la excepción correcta."""
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float) /check
#   - División con números negativos /check
#   - División por cero → debe lanzar ZeroDivisionError/check
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
