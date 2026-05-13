import os
# O código busca a senha no ambiente (Cofre)
senha_do_banco = os.getenv('SENHA_BANCO', 'NAO_CONFIGURADA')
print("--- 🏦 SISTEMA DO BANCO DIGITAL ---")
if senha_do_banco == '12345':
    print("✅ Senha Correta! Acesso liberado ao cofre.")
else:
    print("❌ ACESSO NEGADO! Chave de segurança não encontrada.")
