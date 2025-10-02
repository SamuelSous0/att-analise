import pandas as pd
import matplotlib.pyplot as plt

# ajuste o caminho se necessário
arquivo = "baseEnade17_Sistemas (1).xlsx"
df = pd.read_excel(arquivo)

candidates = [c for c in df.columns if c.lower() in (
    'categoriaadm','catadmin','categoria_adm','categoria adm','categoria')]
if not candidates:
    candidates = [c for c in df.columns if 'categoria' in c.lower() or 'cat' in c.lower() or 'adm' in c.lower()]

if not candidates:
    print("Não encontrei coluna de categoria administrativa. Colunas disponíveis:")
    print(df.columns.tolist())
    raise KeyError("Coluna de categoria administrativa não encontrada.")

category_col = candidates[0]
print(f"Usando coluna: '{category_col}'")
print("Valores únicos:", df[category_col].unique())

counts = df[category_col].value_counts(dropna=False)
plt.figure(figsize=(6,4))
bars = plt.bar(counts.index.astype(str), counts.values)
plt.title("Distribuição por Categoria Administrativa")
plt.xlabel("Categoria")
plt.ylabel("Quantidade de alunos")
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6)

for rect in bars:
    h = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2, h + 0.5, int(h), ha='center', va='bottom')

plt.tight_layout()
plt.show()

if 'NOTA_GERAL' not in df.columns:
    print("A coluna 'NOTA_GERAL' não foi encontrada. Colunas disponíveis:", df.columns.tolist())
else:
    stats = df.groupby(category_col)['NOTA_GERAL'].agg(['count','mean','median','std']).reset_index()
    print("\nEstatísticas por categoria:")
    print(stats)

    plt.figure(figsize=(6,4))
    plt.bar(stats[category_col].astype(str), stats['mean'], yerr=stats['std'], capsize=6)
    plt.title("Média da NOTA_GERAL por Categoria Administrativa")
    plt.xlabel("Categoria")
    plt.ylabel("Média NOTA_GERAL")
    for i, v in enumerate(stats['mean']):
        plt.text(i, v + 0.5, f"{v:.2f}", ha='center')
    plt.tight_layout()
    plt.show()
