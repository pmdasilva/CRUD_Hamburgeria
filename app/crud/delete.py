from data.data import data_hamburguers

def delete_hamburguer():
    """Deleta um hambúrguer existente pelo índice"""
    try:
        if not data_hamburguers:
            return {"status": "erro", "mensagem": "Nenhum hambúrguer cadastrado."}
        
        # Lista hambúrgueres disponíveis
        hamburguers_list = []
        for i, hamburguers in enumerate(data_hamburguers):
            hamburguers_list.append(f'{i} - {hamburguers["name"]} - R${hamburguers["price"]:.2f}')
        
        index = int(input(f'Digite o índice do hambúrguer a deletar (0-{len(data_hamburguers)-1}): '))
        
        if index < 0 or index >= len(data_hamburguers):
            return {"status": "erro", "mensagem": "Índice inválido."}
        
        hamburguer_deletado = data_hamburguers.pop(index)
        
        return {
            "status": "sucesso",
            "mensagem": "Hambúrguer deletado com sucesso!",
            "hamburguer_deletado": hamburguer_deletado
        }
        
    except ValueError:
        return {"status": "erro", "mensagem": "Valor inválido. Por favor, insira um número válido."}
    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao deletar hambúrguer: {e}"}
