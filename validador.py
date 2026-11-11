# Valida se todas as configurações obrigatórias de segurança estão presentes no sistema

#Funções
def revisar_configuracoes():
    configuracoes = ("MFA", "Firewall", "Backup", "Antivirus", "VPN")
    return configuracoes

def remover_duplicatas(dados):
    unicos = set(dados)
    return unicos

def comparacao(obrigatorias, presentes):
    faltantes = []
    for item in obrigatorias:
        if item not in presentes:
            faltantes.append(item)
    return faltantes

if __name__ == "__main__":
    log = ["MFA", "Backup", "MFA", "VPN", "Backup", "MFA"]
    revisar = revisar_configuracoes()
    duplicatas = remover_duplicatas(log)
    resultado = comparacao(revisar, duplicatas)
    if not resultado:
        print("Todas as configurações obrigatórias estão presentes!")
    else:
        print(f"As seguintes configurações obrigatórias estão faltando: {resultado}")