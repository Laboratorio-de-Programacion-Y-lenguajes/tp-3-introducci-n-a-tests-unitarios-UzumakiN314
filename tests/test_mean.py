"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---

@pytest.mark.parametrize("lista, expected", [
    ([10], 10.0),
    ([-2, -4, -6], -4.0),
    ([1.5, 2.5, 5.0], 3.0),
    ([1, 2, 3, 4, 5], 3.0),
    ([0, 0, 0], 0.0)
])
def test_mean_parametrizado(lista, expected):
    """Prueba el promedio con distintos tipos de listas."""
    assert mean(lista) == pytest.approx(expected)

def test_mean_lista_vacia():
    """Verifica que una lista vacía lance ValueError."""
    with pytest.raises(ValueError):
        mean([])

# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento) / check
#   - Lista con números negativos / check
#   - Lista con números decimales (float) / check
#   - Lista vacía → debe lanzar ValueError / check
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
