from data.data import data_hamburguers

def update_hamburguer():
    """Atualiza um hambúrguer existente pelo índice"""
    try:
        if not data_hamburguers:
            return {"status": "erro", "mensagem": "Nenhum hambúrguer cadastrado."}
        
        # Lista hambúrgueres disponíveis
        hamburguers_list = []
        for i, hamburguers in enumerate(data_hamburguers):
            hamburguers_list.append(f'{i} - {hamburguers["name"]} - R${hamburguers["price"]:.2f}')
        
        index = int(input(f'Digite o índice do hambúrguer a atualizar (0-{len(data_hamburguers)-1}): '))
        
        if index < 0 or index >= len(data_hamburguers):
            return {"status": "erro", "mensagem": "Índice inválido."}
        
        new_name = str(input('Digite o novo nome do hambúrguer: '))
        new_price = float(input('Digite o novo preço do hambúrguer: '))
        
        old_hamburguer = data_hamburguers[index].copy()
        data_hamburguers[index] = {'name': new_name, 'price': new_price}
        
        return {
            "status": "sucesso",
            "mensagem": "Hambúrguer atualizado com sucesso!",
            "anterior": old_hamburguer,
            "novo": data_hamburguers[index]
        }
        
    except ValueError:
        return {"status": "erro", "mensagem": "Valor inválido. Por favor, insira dados corretos."}
    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao atualizar hambúrguer: {e}"}
