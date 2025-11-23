algo = input("Digite algo: ")
print(f"o tipo primitvo desse valor é {type(algo)}")
print(f"É em número? {algo.isnumeric()}") ## só números
print(f"É alfanumérico? {algo.isalnum()}") ## letras e números
print(f"É alfabético? {algo.isalpha()}") ## só letras
print(f"É ASCII? {algo.isascii()}") ## só letras, números e símbolos
print(f"É decimal? {algo.isdecimal()}") ## só números decimais
print(f"É digito? {algo.isdigit()}") ## só números (índices)
print(f"É identificador? {algo.isidentifier()}") ## nome válido para variavel
print(f"É printavel? {algo.isprintable()}") ## só letras, números, símbolos e espaços
print(f"Está minuscula? {algo.islower()}") ## só letras minusculas
print(f"É só de espaço? {algo.isspace()}") ## só espaços
print(f"É capitalizada? {algo.istitle()}") ## palavra com a primeira letra maiuscula
print(f"Está maiúscula? {algo.isupper()}") ## só letras maiusculas