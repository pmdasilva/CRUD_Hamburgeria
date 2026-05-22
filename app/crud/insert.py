from data.data import data_hamburguers

def adding_hamburguers(name_hamburguer, price_hamburguer):
    """Adiciona um novo hambúrguer à lista"""
    try:
        data_hamburguers.append({'name': name_hamburguer, 'price': price_hamburguer})
        return {
            "status": "sucesso",
            "mensagem": "Hambúrguer adicionado com sucesso!",
            "dados": {'name': name_hamburguer, 'price': price_hamburguer}
        }
    except ValueError:
        return {
            "status": "erro",
            "mensagem": "Valor inválido. Por favor, insira um número para o preço do hambúrguer."
        }


def list_humburguers():
    try:
        if not data_hamburguers:
            print('Nenhum hambúrguer cadastrado.')
        else:
            print(f'lista de hamburguers cadastrados: ')
            for i, hamburguers in enumerate(data_hamburguers):
                print(f'{i + 1} - {hamburguers["name"]} - Price: R${hamburguers["price"]:.2f}')
                
    except Exception as e:
        print(f'Ocorreu um erro ao listar os hambúrgueres: {e}')
      
  