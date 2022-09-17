# python

Ejemplos, ejercicios y notas usando el lenguaje de programación Python

## Índice

- [`print` - Mostrar en Pantalla (`stdout`)](./01_print)
- [`input` - Leer valores del teclado (`stdin`)](./02_input)
- [Práctica 1](./03_activities_1)
- [`while` - Ciclo `while`](./04_loops)
- [Práctica 2](./05_activities_2)

## Reglas (Dont's)

Existen algunas prácticas que no se aceptan en la elaboración de los
algoritmos.

1. No se deben forzar ejecuciones a un ciclo `while`.

### Do

```python
numero = int(input('Ingrese un número: '))

while condicional % 2 != 0:
  numero = int(input('Ingrese un número: '))
```

> Notese que el `while` se puede evitar sí el usuario ingresa un número par.

### Don't

```python
numero = 1
while condicional % 2 != 0:
  numero = int(input('Ingrese un número: '))
```

> Notese que el `while` se ejecutará al menos 1na vez. (Se está forzando a correr)

2. No esta permitido el uso de `break` y/o `continue`
