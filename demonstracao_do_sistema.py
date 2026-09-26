from datetime import datetime, timedelta

class BaseConhecimento:
    def __init__(self):
        self.regras = {
            "r1": "Se matricula_ativa == False ENTÃO nega_emprestimo (Matrícula inativa)",
            "r2": "Se possui_atraso == True ENTÃO nega_emprestimo (Bloqueado por atrasos/débitos)",
            "r3": "Se emprestimos_atuais >= max_emprestimos_aluno ENTÃO nega_emprestimo (Cota máxima atingida)",
            "r4": "Se disponivel == False ENTÃO nega_emprestimo (Livro indisponível)",
            "r5": "Se R1 AND R2 AND R3 AND R4 ENTÃO aprova_emprestimo"
        }

        self.parametros = {
            "max_emprestimos_aluno": 5,
            "prazo_dias_padrao": 14
        }

class MotorInferencia:
    def __init__(self, base_conhecimento):
        self.bc = base_conhecimento
        self.trilha = []

    def inferir(self, fatos):
        self.trilha = []

        if not fatos.get('matricula_ativa', False):
            self.trilha.append("❌ R1 FALHOU: Matrícula inativa")
            return "NEGADO", "Matrícula inativa"
        self.trilha.append("✅ R1 PASSOU: Matrícula ativa")

        if fatos.get('possui_atraso', False):
            self.trilha.append("❌ R2 FALHOU: Bloqueado por atrasos/débitos")
            return "NEGADO", "Bloqueado por atrasos/débitos"
        self.trilha.append("✅ R2 PASSOU: Sem atrasos")

        max_emp = self.bc.parametros['max_emprestimos_aluno']
        if fatos.get('emprestimos_atuais', 0) >= max_emp:
            self.trilha.append(f"❌ R3 FALHOU: Cota máxima de {max_emp} empréstimos atingida")
            return "NEGADO", "Cota máxima atingida"
        self.trilha.append("✅ R3 PASSOU: Dentro do limite")

        if not fatos.get('disponivel', False):
            self.trilha.append("❌ R4 FALHOU: Livro indisponível")
            return "NEGADO", "Livro indisponível"
        self.trilha.append("✅ R4 PASSOU: Livro disponível")

        self.trilha.append("✅ R5 ATIVADA: todas as condições satisfeitas — APROVANDO empréstimo")
        return "APROVADO", None

class SistemaEspecialistaDemo:
    def __init__(self):
        self.bc = BaseConhecimento()
        self.motor = MotorInferencia(self.bc)

    def processar_emprestimo(self, aluno_nome, matricula, fatos, livro):
        # 'livro' aqui é um dicionario com os fatos definidos na Base de Conhecimento (1.3):
        # {'titulo': str, 'disponivel': bool}
        fatos_completos = dict(fatos)
        fatos_completos['disponivel'] = livro.get('disponivel', False)

        print(f"\n{'='*70}")
        print(f"📚 SOLICITAÇÃO DE EMPRÉSTIMO #{fatos.get('id', 0)}")
        print(f"{'='*70}")
        print(f"\n👤 Aluno: {aluno_nome}")
        print(f"📋 Matrícula: {matricula}")
        print(f"📖 Livro: {livro.get('titulo', '—')}")
        print(f"\n🔍 STATUS DO ALUNO:")
        print(f"   Matrícula Ativa: {'✅ Sim' if fatos_completos['matricula_ativa'] else '❌ Não'}")
        print(f"   Possui Atraso: {'⚠️  Sim' if fatos_completos['possui_atraso'] else '✅ Não'}")
        print(f"   Empréstimos Atuais: {fatos_completos['emprestimos_atuais']}/{self.bc.parametros['max_emprestimos_aluno']}")
        print(f"\n📗 STATUS DO LIVRO:")
        print(f"   Disponível: {'✅ Sim' if fatos_completos['disponivel'] else '❌ Não'}")

        print(f"\n🧠 MOTOR DE INFERÊNCIA (Forward Chaining):")
        print(f"{'-'*70}")

        decisao, motivo = self.motor.inferir(fatos_completos)

        for i, passo in enumerate(self.motor.trilha, 1):
            print(f"   {i}. {passo}")

        print(f"\n🎯 DECISÃO FINAL: {decisao}")

        if decisao == "APROVADO":
            prazo = (datetime.now() + timedelta(days=self.bc.parametros['prazo_dias_padrao'])).strftime("%d/%m/%Y")
            print(f"✅ Empréstimo aprovado até {prazo}")
        else:
            print(f"❌ Empréstimo negado. Motivo: {motivo}")

print("\n" + "█"*70)
print("█" + " "*68 + "█")
print("█" + "  DEMONSTRAÇÃO: SISTEMA ESPECIALISTA PARA BIBLIOTECA".center(68) + "█")
print("█" + " "*68 + "█")
print("█"*70)

se = SistemaEspecialistaDemo()

# Teste 1: aprovação plena (R1 a R5 passam)
se.processar_emprestimo(
    aluno_nome="João Silva",
    matricula="2024001",
    fatos={'id': 1, 'matricula_ativa': True, 'possui_atraso': False, 'emprestimos_atuais': 2},
    livro={'titulo': "Estrutura de Dados em Python", 'disponivel': True}
)

# Teste 2: negado em R2 (possui atraso)
se.processar_emprestimo(
    aluno_nome="Maria Santos",
    matricula="2024002",
    fatos={'id': 2, 'matricula_ativa': True, 'possui_atraso': True, 'emprestimos_atuais': 1},
    livro={'titulo': "Algoritmos Avançados", 'disponivel': True}
)

# Teste 3: negado em R3 (cota máxima atingida)
se.processar_emprestimo(
    aluno_nome="Pedro Costa",
    matricula="2024003",
    fatos={'id': 3, 'matricula_ativa': True, 'possui_atraso': False, 'emprestimos_atuais': 5},
    livro={'titulo': "Banco de Dados", 'disponivel': True}
)

# Teste 4: negado em R1 (matrícula inativa)
se.processar_emprestimo(
    aluno_nome="Ana Oliveira",
    matricula="2024004",
    fatos={'id': 4, 'matricula_ativa': False, 'possui_atraso': False, 'emprestimos_atuais': 0},
    livro={'titulo': "Programação Web", 'disponivel': True}
)

# Teste 5: negado em R4 (livro indisponível) — aluno OK em tudo, mas o livro não está disponível
se.processar_emprestimo(
    aluno_nome="Carlos Mendes",
    matricula="2024005",
    fatos={'id': 5, 'matricula_ativa': True, 'possui_atraso': False, 'emprestimos_atuais': 0},
    livro={'titulo': "Inteligência Artificial", 'disponivel': False}
)
