import gerenciamento_biblioteca.defs as defs
import interfaces

def buscar_livro():
    defs.limpar_terminal()
    interfaces.itf_buscarLivros()
    with open("gerenciamento_biblioteca/biblioteca.txt","r+") as buscar_r:
        linhas = buscar_r.readlines()
        livro_buscado = str(input("Nome do Livro: ")).lower().strip()

        count=0
        
        for linha in linhas[1:]:
            linha_split = linha.split(";")[2].strip()
            linha_split = str(linha_split)
            if linha_split == livro_buscado:
                count+=1
                break 
            else:
                count=0
        if count==1:
            defs.limpar_terminal()
            interfaces.itf_buscarLivros()
            print("--encontrado--")
            print("\n"+linhas[0])
            print(linha+"\n")
            def opcoes():
                busca = int(input("[1] buscar outro livro [2] voltar ao menu: "))
                if busca ==1:
                    buscar_r.close()
                    buscar_livro()
                elif busca ==2:
                    buscar_r.close()
                    __main__()
                else:
                    print("Opcao Invalida!")
                    buscar_r.close()
                    opcoes()
            opcoes()

            
        else:
            print("Livro nao cadastrado!")
            buscar_r.close()

def emprestimo():
    defs.limpar_terminal()
    interfaces.itf_emprestimo()
    with open("gerenciamento_biblioteca/biblioteca.txt","r+") as lista_r:
        linhas = lista_r.readlines()
        livro_buscado = input("Nome do livro: ").lower()
        i=0

        for linha in linhas[1:]:
            i+=1
            linha_split = linha.split(";")[2].strip()
            
            if livro_buscado == linha_split:
                linhas[i] = linha.replace("Nao", "Sim")
                print("Cadastro de emprestimo de "+ livro_buscado +" realizado!")
                
                def emprestimo_opcao():
                    opcao = int(input("\n[1] Cadastrar outro emprestimo [2] Voltar ao menu: "))
                    match opcao:
                        case 1:
                            lista_r.close()
                            emprestimo()
                        case 2:
                            lista_r.close()
                            __main__()
                        case _:
                            print("\nOpcao invalida!\n")
                emprestimo_opcao()
        else:
            print("Livro nao encontrado ou ja emprestado!")
                
        lista_r.seek(0)
        lista_r.writelines(linhas)
                

def adicionar_livro():
    defs.limpar_terminal()
    interfaces.itf_adicionarLivro()

    with open("gerenciamento_biblioteca/biblioteca.txt","r+") as lista_r:
        linhas = lista_r.readlines()
        
        if len(linhas) > 0:
            id_maior=0
            for linha in linhas[1:]:
                id_split = linha.split(";")[0].strip()
                if id_split.isdigit():
                    id_aux = int(id_split)
                    if id_aux > id_maior:
                        id_maior = id_aux
        
            id = str(id_maior+1)
        else:
            id="1"

        novo_livro = input("Nome do Livro: ").lower()
        disponivel = "Nao"
        lista_r.write("\n{};      {};     {}".format(id, disponivel, novo_livro))
        print("\nLivro adicionado com suceeso!\n")
        lista_r.close()
        def opcao():
            opcao = int(input("[1] adicionar outro livro [2] voltar ao menu: "))
            match opcao:
                case 1:
                    adicionar_livro()
                case 2:
                    defs.limpar_terminal()
                    __main__()
                case _:
                    print("\nOpcao invalida!")
        opcao()

def excluir_livro():
    defs.limpar_terminal()
    interfaces.itf_excluirLivro()
    
                        
    with open("gerenciamento_biblioteca/biblioteca.txt","r+") as excluir_r:

        linhas = excluir_r.readlines()
        novas_linhas = []

        id_busca = int(input("id do livro: "))
        count=0
        
        for linha in linhas[1:]:
            id_split = linha.split(";")[0].strip()
            if id_split.isdigit():
                id = int(id_split)
                if id == id_busca:
                    count+=1
                else:
                    novas_linhas.append(linha)
        print(novas_linhas)
        
        if count==1:
            with open("gerenciamento_biblioteca/biblioteca.txt","w") as excluir_w:
                excluir_w.write(linhas[0])
                for linha in novas_linhas:
                    excluir_w.write(linha)
                excluir_w.close()
            defs.limpar_terminal()
            print("   -----------\nLivro excluido com sucesso!\n   -----------")
            __main__()

        elif count==0:
            defs.limpar_terminal()
            print("Livro nao encontrado!")
            __main__()
            

            

def editar_cadastro():
    with open("gerenciamento_biblioteca/biblioteca.txt","r+") as editar_r:
        linhas = editar_r.readlines()
        i=0

        id_digitado = str(input("id do livro:"))
        if id_digitado:   
            for linha in linhas[1:]:
                i+=1
                id_split = linha.split(";")[0].strip()
                if id_digitado == id_split:
                    nome_split = linha.split(";")[2].strip()
                    novo_nome = input("\nNome atual '"+nome_split+"'\n Novo nome: ").strip().lower()
                    linhas[i] = linha.replace(nome_split, novo_nome)
                    if novo_nome:
                        defs.limpar_terminal()
                        print("\nNome alterado com sucesso!")
                        __main__()
                        break
                    else:
                        print("Livro nao encontrado!")
                        break

        editar_r.seek(0)
        editar_r.writelines(linhas)


def __main__():
    opcao_menu = int(input("\n------BIBLIOTECA VIRTUAL------\n[1] Buscar Livro\n[2] Emprestimo\n[3] Adicionar Livro\n[4] Excluir Livro\n[5] Editar Cadastro\n[6] Sair\n\nEscolha uma opcao: "))
    match opcao_menu:
        case 1:
            buscar_livro()
        case 2:
            emprestimo()
        case 3: 
            adicionar_livro()
        case 4:
            excluir_livro()
        case 5:
            editar_cadastro()
        case 6:
            exit()
__main__()