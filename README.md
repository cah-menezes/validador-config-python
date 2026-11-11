# ✅ Validador de Configurações de Segurança

Script em Python que valida se todas as configurações obrigatórias de segurança estão presentes em um sistema, comparando uma lista de requisitos fixos com um log de configurações detectadas.

## ⚙️ Funcionalidades

- Define configurações obrigatórias usando **tuple** (imutável)
- Remove duplicatas do log de configurações usando **set**
- Compara os dois e lista o que está faltando

## 🚀 Como executar

```bash
git clone https://github.com/cah-menezes/validador-config-python.git
cd validador-config-python
python3 validador.py
```