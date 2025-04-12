```markdown
# PyRomano

**PyRomano** es una biblioteca de Python para trabajar con números romanos y medidas romanas. Convierte fácilmente entre números romanos y decimales (incluyendo fracciones), y maneja unidades romanas de longitud, peso y capacidad con conversiones a unidades modernas o entre sí. Incluye una interfaz de línea de comandos (CLI) para uso rápido. Es ideal para proyectos educativos, históricos o aplicaciones que requieran cálculos romanos precisos.

## Características principales
- **Conversión de números romanos**: Transforma números romanos a decimales (ej. "XII·" → 12.0833) y decimales a romanos (ej. 12.5 → "XIIS"), con soporte para fracciones.
- **Medidas romanas**: Convierte unidades como `pes`, `libra` o `amphora` a metros, kilogramos o litros, o entre unidades romanas (ej. 1 stadium → 125 passus).
- **Validación estricta**: Detecta números romanos mal formados (como "IIII" o "VV").
- **Interfaz CLI**: Ejecuta conversiones directamente desde la terminal.
- **Simplicidad**: Usa solo caracteres estándar (`I`, `V`, `X`, `L`, `C`, `D`, `M`, `S`, `·`), fáciles de escribir.

## Instalación
Instala `PyRomano` desde PyPI con pip:

```bash
pip install PyRomano
```

Requiere Python 3.7 o superior. No tiene dependencias externas.

## Uso básico
`PyRomano` ofrece dos clases principales: `NumRom` para números romanos y `MedRom` para medidas romanas. A continuación, algunos ejemplos:

### Convertir números romanos
```python
from PyRomano import NumRom, MedRom

# Romano a decimal
print(NumRom.a_decimal("XII·"))      # 12.083333333333334
print(NumRom.a_decimal("MMMCMXCIX")) # 3999.0

# Decimal a romano
print(NumRom.a_romano(2023))         # MMXXIII
print(NumRom.a_romano(12.5))         # XIIS
```

### Manejar medidas romanas
```python
# Convertir a unidades modernas (metros, kg, litros)
print(MedRom.a_modernas(2, "passus"))  # 2.96
print(MedRom.a_modernas(1, "libra"))   # 0.3289

# Convertir a unidades romanas
print(MedRom.a_unidad_romana(1.0, "pes"))  # 3.378378378378378

# Conversión entre unidades romanas
print(MedRom.conversion_unidades(1, "stadium", "passus"))  # 125.0
```

### Listar unidades disponibles
```python
print(MedRom.unidades_disponibles())  # ['pes', 'passus', 'stadium', 'mille_passus', 'libra', 'uncia', 'amphora', 'sextarius']
```

## Uso desde la línea de comandos (CLI)
`PyRomano` incluye una CLI para conversiones rápidas:

- **Romano a decimal**:
  ```bash
  python -m PyRomano roman-to-decimal "XII·"
  # Salida: 12.083333333333334
  ```

- **Decimal a romano**:
  ```bash
  python -m PyRomano decimal-to-roman 12.5
  # Salida: XIIS
  ```

- **Conversión de medidas**:
  ```bash
  python -m PyRomano convert-measure 1 stadium passus
  # Salida: 125.0
  python -m PyRomano convert-measure 2 passus modern
  # Salida: 2.96
  ```

## Unidades soportadas
- **Longitud**:
  - `pes` (~0.296 m)
  - `passus` (~1.48 m)
  - `stadium` (~185 m)
  - `mille_passus` (~1480 m)
- **Peso**:
  - `libra` (~0.3289 kg)
  - `uncia` (~0.027408333333333334 kg)
- **Capacidad**:
  - `amphora` (~26.2 L)
  - `sextarius` (~0.546 L)

## Limitaciones y notas
- **Rango de números**: Soporta números de 0 a 3999.5, acorde con el sistema romano tradicional.
- **Fracciones**: Limitadas a doceavas (1/12 a 6/12), usando "S" (1/2) y "·" (1/12 y múltiplos).
- **Medidas**: Las conversiones son aproximadas según valores históricos, excepto libra-uncia (exacta: 1 libra = 12 uncias).
- **Entrada**: Solo caracteres básicos (`I`, `V`, `X`, `L`, `C`, `D`, `M`, `S`, `·`) para facilitar el uso.
- **Exportación a LaTeX**: Actualmente no implementada, pero planeada para futuras versiones.

## Contribuir
¿Quieres mejorar `PyRomano`? Envía sugerencias o reportes de errores a contacto@criptogalicia.com.

## Licencia
Distribuida bajo la [Licencia MIT](LICENSE). Usa, modifica y comparte libremente esta biblioteca.

## Contacto
Para soporte o preguntas, contacta con José Luis Alvarez Gago en contacto@criptogalicia.com.
```