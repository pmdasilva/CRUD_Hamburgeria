from crud.crud_repository import CrudBurguer
import utils.clear_terminal


def application():

    crud = CrudBurguer(name_hamburger="", price_hamburger=0.0, data_hamburguers=[])
    option = 0
    while option != 5:
        crud.show_menu()
        option = int(input("Digite a opção desejada: "))

        if option == 1:
            utils.clear_terminal.clear_terminal()
            crud.adding_hamburguers()
        elif option == 2:
            utils.clear_terminal.clear_terminal()
            crud.list_hamburgers()
        elif option == 3:
            utils.clear_terminal.clear_terminal()
            crud.update_hamburger_interactive()
        elif option == 4:
            utils.clear_terminal.clear_terminal()
            crud.delete_hamburguer()
        elif option == 5:
            utils.clear_terminal.clear_terminal()
            print("Saindo do programa...")
        else:
            utils.clear_terminal.clear_terminal()
            print("Opção inválida. Por favor, escolha uma opção válida.")


application()
