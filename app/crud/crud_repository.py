class CrudBurguer:
    def __init__(
        self, name_hamburger: str, price_hamburger: float, data_hamburguers: list
    ):
        self.name_hamburger = name_hamburger
        self.price_hamburger = price_hamburger
        self.data_hamburguers = data_hamburguers

    def add_hamburger(self):
        """function that take and add name_hamburger and price_hamburger to data_hamburgers list"""
        humburguer = {"name": self.name_hamburger, "price": self.price_hamburger}
        self.data_hamburguers.append(humburguer)
        return humburguer

    def adding_hamburguers(self):
        while True:
            self.name_hamburger = input(
                "Digite o nome do hamburguer que deseja adicionar: "
            )
            if self.name_hamburger.isdigit():
                print(
                    "Nome inválido. O nome deve ser uma string, não um número. Tente novamente."
                )
                continue
            else:
                break
        while True:
            try:
                self.price_hamburger = float(input("Digite o valor do hamburger: "))
                return self.add_hamburger()
            except ValueError:
                print(
                    "Valor inválido. Por favor, insira um número para o preço do hambúrguer."
                )

    def list_hamburgers(self):
        """Function show all hamburgers in list."""
        if not self.data_hamburguers:
            print("Nenhum hambúrguer cadastrado.")
            return
        print(f"lista de hamburguers cadastrados: ")
        for i, hamburger in enumerate(self.data_hamburguers, start=1):
            print(f'{i} - {hamburger["name"]} - Price: R${hamburger["price"]:.2f}')

    def remove_hamburger(self, index: int) -> dict | None:
        """Remove the hamburger by the index, and return the removed item."""
        if index < 0 or index >= len(self.data_hamburguers):
            return None
        return self.data_hamburguers.pop(index)

    def delete_hamburguer(self):
        """Requests to user which hamburger should be excluded from the list."""
        try:
            self.list_hamburgers()
            if not self.data_hamburguers:
                print("Não há hambúrgueres para excluir.")
                return
            index = int(input("Digite o número do hamburger que deseja excluir: "))
            if index < 1 or index > len(self.data_hamburguers):
                print("Número inválido. Por favor, escolha um número válido da lista.")
                return
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            return

        deleted = self.remove_hamburger(index - 1)
        if deleted is None:
            print("Erro inesperado ao excluir.")
            return
        print(
            f"Hambúrguer excluído: {deleted['name']} - Preço: R${deleted['price']:.2f}"
        )
        self.list_hamburgers()

    def show_menu(self):
        print(f"\n --- MENU HAMBURGARIA ---")
        print(f"1. ADDING a hambuguer")
        print(f"2. LIST a hambuguer")
        print(f"3. UPDATE a hambuguer")
        print(f"4. DELETE a hambuger")
        print(f"5. Leave")

    def update_hamburger(
        self, index: int, new_name: str, new_price: float
    ) -> dict | None:
        """Update the index and return the updated item."""
        if index < 0 or index >= len(self.data_hamburguers):
            return None
        self.data_hamburguers[index] = {"name": new_name, "price": new_price}
        return self.data_hamburguers[index]

    def update_hamburger_interactive(self):
        """ "Requests the user which hamburger to update and applies the changes."""

        try:
            index = (
                int(input("Digite o número do hambúrguer que deseja atualizar: ")) - 1
            )
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            return

        if index < 0 or index >= len(self.data_hamburguers):
            print(
                f"Número inválido. Escolha um número entre 1 e {len(self.data_hamburguers)}."
            )
            return

        new_name = input("Digite o nome do novo hambúrguer: ")
        try:
            new_price = float(input("Digite o novo preço: "))
        except ValueError:
            print("Preço inválido. Digite um número válido.")
            return

        updated = self.update_hamburger(index, new_name, new_price)
        if updated:
            print("Hambúrguer atualizado com sucesso!")
            print(
                f'Hambúrguer atualizado: {updated["name"]} - Preço: R${updated["price"]:.2f}'
            )
