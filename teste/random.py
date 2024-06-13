#%%
import random
import string


#%%
def generate_random_code(length=5):
    # Definir os caracteres possíveis (números e letras maiúsculas e minúsculas)
    characters = string.ascii_letters + string.digits
    # Gerar um código aleatório de 6 dígitos
    random_code = ''.join(random.choices(characters, k=length))
    return random_code


#%%
# Exemplo de uso
code = generate_random_code()
print(f"Código gerado: {code}")