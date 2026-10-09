
"""
Calderon Hello 🚀
A tiny Python package to greet people and
make your first Python projects more fun.
"""

__version__ = "0.1.0"


def saludar(nombre: str) -> str:
    """Return a personalized greeting."""
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    return f"👋 Hello, {nombre}! Welcome to the Python world 🚀"


def despedir(nombre: str) -> str:
    """Return a friendly goodbye."""
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    return f"👋 Goodbye, {nombre}! Keep coding 💻"


def motivar(nombre: str) -> str:
    """Return a motivational message."""
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    return (
        f"🔥 {nombre}, every expert was once a beginner. "
        "Keep learning and building!"
    )


def acerca_de() -> str:
    """Return package information."""
    return (
        f"Calderon Hello v{__version__} | "
        "Your first step into Python packaging 🚀"
    )