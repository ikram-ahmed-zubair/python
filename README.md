Biomedical Unit Converter

A simple command-line tool for converting common biomedical measurement units.

Conversions


Celsius → Fahrenheit
Fahrenheit → Celsius
Centimeter → Meter
Meter → Centimeter
Kilogram → Gram
Gram → Kilogram


Usage

Run the script from the terminal:

bashpython biomedical_unit_converter.py

Choose an option from the menu (1–6), then enter the value you want to convert.

Example

=================================
 Biomedical Unit Converter
=================================
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Centimeter → Meter
4. Meter → Centimeter
5. Kilogram → Gram
6. Gram → Kilogram
Enter your choice: 1
Enter Celsius: 37
37.0°C = 98.6°F

Project Structure

python/
│
├── biomedical_unit_converter.py
├── README.md
└── .gitignore

Notes


Each conversion is implemented as its own function.
Results are rounded to 2 decimal places with round().
Entering a menu number outside 1–6 triggers an else block with an error message.
