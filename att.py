import pandas as pd
import matplotlib.pyplot as plt

arquivo = "baseEnade17_Sistemas (1).xlsx"
df = pd.read_excel(arquivo)

# ==========================
# 1) GRÁFICOS DE BARRAS
# ==========================



# --- Sexo
sexo_counts = df["SEXO"].value_counts()
plt.figure(figsize=(5,4))
plt.bar(sexo_counts.index, sexo_counts.values, color=["skyblue","lightcoral"])
plt.title("Distribuição de alunos por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Quantidade")
plt.show()

# --- Turno
turno_counts = df["TURNO"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(turno_counts.index.astype(str), turno_counts.values, color="orange")
plt.title("Distribuição de alunos por Turno")
plt.xlabel("Turno (códigos)")
plt.ylabel("Quantidade")
plt.show()

# --- Modalidade
modalidade_counts = df["MODALIDADE"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(modalidade_counts.index.astype(str), modalidade_counts.values, color="green")
plt.title("Distribuição de alunos por Modalidade")
plt.xlabel("Modalidade (0 = Presencial, 1 = EAD)")  # ajustar conforme o dicionário
plt.ylabel("Quantidade")
plt.show()

# ==========================
# 2) TABELA DE CONTINGÊNCIA
# ==========================
contingencia = pd.crosstab(df["MODALIDADE"], df["TURNO"])
print("\nTabela de Contingência (Modalidade x Turno):\n")
print(contingencia)

# ==========================
# 3) ANÁLISE DESCRITIVA DAS NOTAS
# ==========================

media = df["NOTA_GERAL"].mean()
mediana = df["NOTA_GERAL"].median()
desvio = df["NOTA_GERAL"].std()
cv = desvio / media

print("\nEstatísticas NOTA_GERAL:")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desvio Padrão: {desvio:.2f}")
print(f"Coeficiente de Variação: {cv:.2f}")

# Histograma das notas
plt.figure(figsize=(7,4))
plt.hist(df["NOTA_GERAL"].dropna(), bins=12, color="skyblue", edgecolor="black")
plt.title("Distribuição das Notas (Histograma)")
plt.xlabel("Nota Geral")
plt.ylabel("Frequência")
plt.show()

# Boxplot das notas por modalidade
plt.figure(figsize=(7,4))
data = [df[df["MODALIDADE"]==m]["NOTA_GERAL"].dropna() for m in df["MODALIDADE"].unique()]
labels = [str(m) for m in df["MODALIDADE"].unique()]
plt.boxplot(data, labels=labels)
plt.title("Notas por Modalidade")
plt.xlabel("Modalidade (0 = Presencial, 1 = EAD)")
plt.ylabel("Nota Geral")
plt.show()
