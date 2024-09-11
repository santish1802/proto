import sqlite3

# Conectar a la base de datos (la creará si no existe)
conn = sqlite3.connect('nombre.db')
cursor = conn.cursor()

# Crear la tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS saludos
(nombre TEXT PRIMARY KEY, mensaje TEXT)
''')

# Insertar algunos datos de ejemplo
datos = [
    ('Alice', '¡Hola Alice! ¿Cómo está tu proyecto de IA?'),
    ('Bob', 'Hey Bob, ¿listo para el partido de fútbol?'),
    ('Charlie', 'Charlie, tu informe del mes pasado fue excelente.'),
    ('Default', 'Hola, es un placer conocerte.')
]

cursor.executemany('INSERT OR REPLACE INTO saludos VALUES (?, ?)', datos)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada y poblada con éxito.")