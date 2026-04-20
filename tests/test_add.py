"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# --- TU TURNO ---

@pytest.mark.parametrize("a, b, expected", [
    (-1, -2, -3.0),    # Sumar dos números negativos
    (5, -2, 3.0),      # Sumar un número positivo y uno negativo
    (10, 0, 10.0),     # Sumar con cero
    (0, 0, 0.0),       # Caso borde: doble cero
    (2.5, 3.1, 5.6),   # Sumar dos números decimales (float)
    (-1.5, 0.5, -1.0)  # Decimales con signo
])
def test_add_casos_varios(a, b, expected):
    """Prueba múltiples combinaciones de suma."""
    assert add(a, b) == expected



# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos / check
#   - Sumar un número positivo y uno negativo / check
#   - Sumar con cero / check
#   - Sumar dos números decimales (float) / check
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected
