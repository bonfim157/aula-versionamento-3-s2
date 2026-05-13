import os
# O código busca a senha no ambiente (Cofre)
senha_do_banco = os.getenv('SENHA_BANCO', 'NAO_CONFIGURADA')
print("--- [BANCO DIGITAL] ---")
if senha_do_banco == '12345':
    print("OK: Senha Correta! Acesso liberado ao cofre.")
else:
    print("ERRO: ACESSO NEGADO! Chave de segurança não encontrada.")
