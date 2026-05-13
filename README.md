# 🏦 Meu Banco Seguro - Projeto de Versionamento e Segurança

Este projeto foi desenvolvido como parte do material de apoio para o **3º Ano do Ensino Médio - Desenvolvimento de Sistemas**. O objetivo principal é aprender a proteger informações sensíveis utilizando **GitHub Secrets** e a recuperar sistemas após erros críticos utilizando **Git Tags (Rollback)**.

## 🚀 Tecnologias e Conceitos Utilizados

- **Python**: Linguagem base para o sistema do banco.
- **Git & GitHub**: Controle de versão e hospedagem do código.
- **GitHub Secrets**: Cofre de segurança para chaves de API e senhas.
- **Git Tags**: Marcação de versões estáveis do software.
- **Rollback**: Processo de reversão para um estado anterior seguro.

## 🛠️ Funcionalidades do Sistema

O arquivo `app.py` simula o acesso a um cofre digital. Em vez de salvar a senha diretamente no código (o que seria um risco de segurança), o sistema a busca em uma variável de ambiente chamada `SENHA_BANCO`.

### Como rodar localmente
Para testar o acesso liberado, defina a variável de ambiente antes de executar:
```powershell
$env:SENHA_BANCO='12345'; python app.py
```

## 🏷️ Gestão de Versões (Tags)

Neste projeto, utilizamos a tag `v1.0` para marcar o momento em que o sistema estava funcionando perfeitamente. Caso ocorra um erro em produção (como simulado na Etapa 4), podemos retornar rapidamente a este ponto:

```bash
git checkout v1.0
```

## 🔒 Segurança em Primeiro Lugar

Aprendemos que nunca devemos realizar o `push` de senhas ou chaves privadas. O uso de **Secrets** garante que apenas o ambiente de execução tenha acesso a essas informações, mantendo o histórico do Git limpo e seguro.

---
**Professor:** [Insira o Nome do Professor aqui]  
**Aluno:** João Pedro Rocha Vidigal
