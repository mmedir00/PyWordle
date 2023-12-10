a = ['abeja', 'banco', 'casas', 'dobla', 'subir', 'carro', 'grano', 'huevo', 'igual', 'joven',
    'peral', 'luces', 'madre', 'tabla', 'aureo', 'papel', 'queso', 'radio', 'silla', 'audio',
    'pulpo', 'barco', 'clima', 'ducha', 'casco', 'globo', 'hojas', 'islas', 'jugar', 'lugar', 
    'llama', 'mundo', 'naran', 'sonda', 'potro', 'verde', 'perro', 'cable', 'amigo', 'botas', 
    'rueda', 'danza', 'cuero', 'flota', 'giras', 'hongo', 'juego', 'lince', 'mambo', 'nunca', 
    'oasis', 'pasta', 'ronda', 'tango', 'hueso', 'volar', 'setas', 'bello', 'crudo', 'demon', 
    'etnia', 'fuego', 'gusto', 'monja', 'ileso', 'huida', 'leche', 'noble', 'oruga', 'pista', 
    'roble', 'salsa', 'terno', 'uvita', 'abraz', 'buche', 'cuota', 'delta', 'ejejo', 'fruta', 
    'gafas', 'herir', 'izote', 'jorco', 'mujer', 'nopal', 'ojear', 'meter', 'sable', 'tinta', 
    'umbra', 'parce', 'bache', 'metro', 'reloj', 'medro', 'cabal', 'monte', 'lente', 'azote', 
    'ceibo', 'fosil', 'nacer', 'aleta', 'monta', 'elevo', 'cerco', 'alojo', 'maple', 'merlo', 
    'broma', 'limar', 'carpa', 'temor', 'carne', 'pelar', 'miedo', 'selva', 'aroma', 'besar', 
    'anexo', 'risco', 'hedor', 'craso', 'foral', 'sueco', 'hogar', 'sogas', 'balsa', 'hablo', 
    'tomar', 'barro', 'yogur', 'sordo', 'horno', 'regio', 'huele', 'naveo', 'roper', 'falsa', 
    'minar', 'capaz', 'brote', 'marco', 'virus', 'coser', 'manar', 'vario', 'zafio', 'pieza', 
    'tiara', 'matiz', 'trago', 'tirar', 'islar', 'tesor', 'fieza', 'larva', 'samba', 'vuela', 
    'latir', 'torpe', 'ruedo', 'timar', 'tumba', 'pilar', 'saber', 'desde', 'jorar', 'oliva', 
    'quedo', 'cinta', 'trono', 'pared', 'largo', 'sutil', 'salto', 'helio', 'estor', 'bicho', 
    'fumar', 'plomo', 'ducho', 'siete', 'cenar', 'letra', 'doble']

b = []

c = []

for i in a:
    if "á" in i:
        c.append(i)
    elif "ó" in i:
        c.append(i)
    elif "é" in i:
        c.append(i)
    elif "í" in i:
        c.append(i)
    elif "ú" in i:
        c.append(i)
    elif len (i) != 5:    
        c.append(i)
    elif i not in b:
        b.append(i)


print(b)
print(c)
