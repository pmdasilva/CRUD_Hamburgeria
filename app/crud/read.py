from data.data import data_hamburguers

def show_menu():
    print(f'\n --- MENU HAMBURGARIA ---')
    print(f'1. ADDING a hambuguer')
    print(f'2. LIST a hambuguer')
    print(f'3. UPDATE a hambuguer')
    print(f'4. DELETE a hambuger')
    print(f'5. Leave')

def list_humburguers():
    """Lista todos os hambúrgueres cadastrados"""
    try:
        if not data_hamburguers:
            return {
                "status": "info",
                "mensagem": "Nenhum hambúrguer cadastrado."
            }
        else:
            hamburguers_list = []
            for i, hamburguers in enumerate(data_hamburguers):
                hamburguers_list.append({
                    "indice": i + 1,
                    "name": hamburguers["name"],
                    "price": hamburguers["price"]
                })
            return {
                "status": "sucesso",
                "dados": hamburguers_list,
                "total": len(hamburguers_list)
            }
    except Exception as e:
        return {
            "status": "erro",
            "mensagem": f"Ocorreu um erro ao listar os hambúrgueres: {e}"
        }