# Sistema Especialista – Biblioteca Universitária

Trabalho da disciplina de Sistemas Especialistas

## Grupo

- Diogo Gualberto Martins Prudencio – 1250112212
- Felipe Damaceno Geraldo – 1250124679
- Gabriel Lopes de Sousa Ramos – 1250113021
- Gabriel Soares Araújo – 1250122173
- Pedro Luis dos Santos Nascimento – 1250120537

## Descrição

Sistema especialista que decide por forward chaining se um empréstimo de livro pode ser autorizado para um aluno da biblioteca de uma universidade. A decisão é baseada em uma base de conhecimento com fatos sobre o aluno e sobre o livro solicitado, avaliados por 5 regras sequenciais. O processamento é interrompido assim que a primeira regra falha, e o sistema mantém uma trilha explicando o raciocínio até a decisão final.

## Base de Conhecimento (resumo)

**Parâmetros:** `max_emprestimos_aluno = 5`, `prazo_dias_padrao = 14`

**Regras:**
- **R1** – Validação de Matrícula (`matricula_ativa`)
- **R2** – Verificação de Atrasos (`possui_atraso`)
- **R3** – Controle de Cota/Limite (`emprestimos_atuais < max_emprestimos_aluno`)
- **R4** – Verificação de Disponibilidade (`disponivel`)
- **R5** – Autorização Final (R1 AND R2 AND R3 AND R4)

## Protótipo de Telas (Figma)

[https://www.figma.com/proto/XEQcJO2Wr63hO2AE6zg5xS/SISTEMA-BIBLIOTECA--c%C3%B3pia-?node-id=0-1&t=qIEmDoA8eJZcLAsi-1](https://www.figma.com/proto/XEQcJO2Wr63hO2AE6zg5xS/SISTEMA-BIBLIOTECA--c%C3%B3pia-?node-id=0-1&t=qIEmDoA8eJZcLAsi-1)
