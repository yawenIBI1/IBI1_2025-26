# generate_random.py
import random

# 20种标准氨基酸列表
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")
# 生成和人/小鼠序列等长（289aa）的随机序列
random_protein = "".join(random.choice(amino_acids) for _ in range(289))

# 保存为FASTA格式，和其他文件放在同一个文件夹
with open("random_DLX5.fasta", "w") as f:
    f.write(">Random_DLX5_Control (289 aa)\n")
    f.write(random_protein)