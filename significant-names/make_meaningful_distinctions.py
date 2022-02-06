# Usar numéros sequenciais em nomes é o posatos de seleção de nomes expressivos, eles não geram confusão,
# mas não oferecem infoprmação alguma ou nenhuma indicação sobre a inteção do criador, por exemplo:

def copy_chars(a1: list, a2: list):
    for i in range(0, len(a1)):
        a2[i] = a1[i]


# Fica muito mais fácil ler essa função quando é utilizado "source" e "destination" nos paramêtros:
def copy_chars(source: list, destination: list):
    for i in range(0, len(source)):
        destination[i] = source[i]


# Em python seria interessante usar a seguinte abordagem:
def copy_chars(source: list):
    destination = [char for char in source]
    return destination


# Ou utilizar da função Map:
def copy_chars(source: list) -> list:
    destination = list(map(lambda char: char, source))
    return destination

# A palavra comuns são reduntantes, não podendo nunca conter o nome de "variável".
# Imagine uma classe chamada Customer e outra CustomerObject, consegue identificar a diferença entre elas?
# Podendo conter nomes reduntantes de parecidos fica inviável saber qual chamar, exemplo:
# get_active_account()
# get_active_accounts()
# get_active_accounts_info()

# Na ausência de uma convenção não há como diferenciar o moneyAmount de money, customer_info de customer,
# account_data de account e the_message de message.
# Fazer essas distinções fará que seu código sera compreendido pelos leitores de forma mais concisa.
