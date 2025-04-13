import argparse
import sys

class RomanError(Exception):
    """Excepción personalizada para errores relacionados con números romanos o medidas."""
    pass

class NumRom:
    """Clase para manejar números romanos, incluyendo fracciones."""

    # Valores romanos básicos (sin overline)
    _valores_romanos = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
    ]

    # Fracciones romanas (basadas en uncia = 1/12)
    _valores_fracciones = [
        ('S', 6/12), ('·', 1/12), ('··', 2/12), ('···', 3/12),
        ('····', 4/12), ('·····', 5/12)
    ]

    @staticmethod
    def _valida_romano(roman: str) -> None:
        """Valida que un número romano sea correcto según las reglas romanas."""
        roman = roman.upper()
        invalid_sequences = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
        for seq in invalid_sequences:
            if seq in roman:
                raise RomanError(f"Secuencia inválida encontrada: {seq}")
        if any(f[0] in roman for f in NumRom._valores_fracciones):
            for i, char in enumerate(roman):
                if char in 'S·' and i < len(roman) - 6:
                    raise RomanError("Las fracciones deben estar al final del número romano.")

    @staticmethod
    def a_decimal(roman: str) -> float:
        """
        Convierte un número romano (con posibles fracciones) a decimal.

        Ejemplo: "XII·" → 12.0833
        """
        if not roman or not isinstance(roman, str):
            raise RomanError("Entrada inválida: debe ser una cadena no vacía.")

        roman = roman.upper()
        NumRom._valida_romano(roman)

        result = 0
        i = 0

        # Números estándar
        for symbol, value in NumRom._valores_romanos:
            while i < len(roman) and roman.startswith(symbol, i):
                result += value
                i += len(symbol)

        # Fracciones
        for symbol, value in NumRom._valores_fracciones:
            if roman.endswith(symbol):
                result += value
                i += len(symbol)
                break

        if i != len(roman):
            raise RomanError(f"Número romano inválido: {roman}")

        return result

    @staticmethod
    def a_romano(decimal: float) -> str:
        """
        Convierte un número decimal a romano, incluyendo fracciones (1 a 3999.5).

        Ejemplo: 12.25 → "XII···"
        """
        if not isinstance(decimal, (int, float)) or decimal < 0 or decimal > 3999.5:
            raise RomanError("Número fuera de rango: debe estar entre 0 y 3999.5.")

        integer_part = int(decimal)
        fractional_part = decimal - integer_part

        result = ""
        # Números estándar
        if integer_part > 0:
            for symbol, value in NumRom._valores_romanos:
                while integer_part >= value:
                    result += symbol
                    integer_part -= value

        # Fracciones
        if fractional_part > 0:
            closest_fraction = min(NumRom._valores_fracciones,
                                   key=lambda x: abs(x[1] - fractional_part))
            if closest_fraction[1] > 0.01:
                result += closest_fraction[0]

        return result if result else "Nihil"

class MedRom:
    """Clase para manejar el sistema de medidas romano con conversiones."""

    _medidas = {
        "pes": 0.296,         # Longitud: Pie romano (metros)
        "passus": 1.48,       # Paso romano (5 pies)
        "stadium": 185,       # Estadio romano (125 passus)
        "mille_passus": 1480, # Milla romana (1000 passus)
        "libra": 0.3289,      # Peso: Libra romana (kg)
        "uncia": 0.3289 / 12, # Onza romana (1/12 libra, ~0.027408333333333334 kg)
        "amphora": 26.2,      # Capacidad: Ánfora romana (litros)
        "sextarius": 0.546,   # Sextario (1/48 ánfora)
    }

    @staticmethod
    def a_modernas(value: float, unit: str) -> float:
        """Convierte una medida romana a su equivalente moderno."""
        unit = unit.lower()
        if unit not in MedRom._medidas:
            raise RomanError(f"Unidad desconocida: {unit}. Unidades válidas: {list(MedRom._medidas.keys())}")
        if not isinstance(value, (int, float)) or value < 0:
            raise RomanError("El valor debe ser un número no negativo.")
        return value * MedRom._medidas[unit]

    @staticmethod
    def a_unidad_romana(value: float, unit: str) -> float:
        """Convierte una medida moderna a su equivalente romano."""
        unit = unit.lower()
        if unit not in MedRom._medidas:
            raise RomanError(f"Unidad desconocida: {unit}. Unidades válidas: {list(MedRom._medidas.keys())}")
        if not isinstance(value, (int, float)) or value < 0:
            raise RomanError("El valor debe ser un número no negativo.")
        return value / MedRom._medidas[unit]

    @staticmethod
    def conversion_unidades(value: float, from_unit: str, to_unit: str) -> float:
        """Convierte entre dos unidades romanas."""
        from_unit, to_unit = from_unit.lower(), to_unit.lower()
        if from_unit not in MedRom._medidas or to_unit not in MedRom._medidas:
            raise RomanError(f"Unidades inválidas. Unidades válidas: {list(MedRom._medidas.keys())}")
        modern_value = MedRom.a_modernas(value, from_unit)
        return MedRom.a_unidad_romana(modern_value, to_unit)

    @staticmethod
    def unidades_disponibles() -> list:
        """Devuelve las unidades romanas disponibles."""
        return list(MedRom._medidas.keys())

def cli():
    """Interfaz de línea de comandos para la biblioteca."""
    parser = argparse.ArgumentParser(description="Utilidad para números romanos y medidas.")
    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")

    # Conversión de romano a decimal
    roman_parser = subparsers.add_parser("a_decimal", help="Convierte número romano a decimal")
    roman_parser.add_argument("roman", type=str, help="Número romano (ej. XII·)")

    # Conversión de decimal a romano
    decimal_parser = subparsers.add_parser("a_romano", help="Convierte decimal a número romano")
    decimal_parser.add_argument("decimal", type=float, help="Número decimal (ej. 12.25)")

    # Conversión de medidas
    measure_parser = subparsers.add_parser("conversion_unidades", help="Convierte medidas romanas")
    measure_parser.add_argument("value", type=float, help="Valor numérico")
    measure_parser.add_argument("from_unit", type=str, help="Unidad de origen")
    measure_parser.add_argument("to_unit", type=str, help="Unidad de destino (o 'modern' para metros/kg/litros)")

    args = parser.parse_args()

    try:
        if args.command == "a_decimal":
            print(NumRom.a_decimal(args.roman))
        elif args.command == "a_romano":
            print(NumRom.a_romano(args.decimal))
        elif args.command == "conversion_unidades":
            if args.to_unit.lower() == "modern":
                print(MedRom.a_modernas(args.value, args.from_unit))
            else:
                print(MedRom.conversion_unidades(args.value, args.from_unit, args.to_unit))
        else:
            parser.print_help()
    except RomanError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    cli()