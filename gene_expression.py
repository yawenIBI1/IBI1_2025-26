import matplotlib.pyplot as plt

# 1. Create gene expression dictionary
gene_expr = {
    "TP53": 12.4,
    "EGFR": 15.1,
    "BRCA1": 8.2,
    "PTEN": 5.3,
    "ESR1": 10.7
}
print("Initial gene expression dictionary:")
print(gene_expr)


# 2. Add MYC
gene_expr["MYC"] = 11.6
print("\nAfter adding MYC:")
print(gene_expr)

# 3. Query selected gene
# Modify gene_selected to any gene name (e.g., "TP53", "MYC")
gene_selected = "EGFR" # can be modified as "TP53" / "MYC" / any gene
if gene_selected in gene_expr:
    print(f"\nExpression value of {gene_selected}:{gene_expr[gene_selected]}")
else:
    print(f"\nError: {gene_selected} is not in the dataset")

# 4. Calculate average expression
avg_expr = sum(gene_expr.values()) / len(gene_expr)
print(f"\nAverage expression value of all genes: {avg_expr:.2f}")

# 5. Plot bar chart
genes = list(gene_expr.keys())
values = list(gene_expr.values())

plt.figure(figsize=(10, 5))
plt.bar(genes, values, color="skyblue", edgecolor="black")
plt.title("Gene Expression Levels", fontsize=14)
plt.xlabel("Genes", fontsize=12)
plt.ylabel("Expression Value", fontsize=12)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
