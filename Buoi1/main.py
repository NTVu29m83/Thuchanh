import tkinter as tk
import numpy as np

def giai_he_phuong_trinh():
    try:
        n = int(n_entry.get())
        A_entries, b_entries = tao_bang_nhap_lieu(n)  # Gọi hàm tạo bảng
        A = np.array([[float(entry.get()) for entry in row] for row in A_entries])
        b = np.array([float(entry.get()) for entry in b_entries])

        if A.shape == (n, n) and b.shape == (n,):
            x = np.linalg.solve(A, b)
            ket_qua_label.config(text=f"Nghiệm:\n{x}")
        else:
            ket_qua_label.config(text="Sai kích thước ma trận hoặc vector.")
    except ValueError:
        ket_qua_label.config(text="Dữ liệu nhập vào không hợp lệ.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính")

# Nhập số lượng phương trình
n_label = tk.Label(root, text="Số lượng phương trình (n):")
n_label.grid(row=0, column=0, padx=5, pady=5)
n_entry = tk.Entry(root)
n_entry.grid(row=0, column=1, padx=5, pady=5)

# Nút giải hệ phương trình
giai_button = tk.Button(root, text="Giải hệ phương trình", command=giai_he_phuong_trinh)
giai_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Hiển thị kết quả nghiệm
ket_qua_label = tk.Label(root, text="")
ket_qua_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Hàm tạo bảng nhập liệu A và b
def tao_bang_nhap_lieu(n):
    # Nhập ma trận hệ số (A)
    A_label = tk.Label(root, text="Ma trận hệ số (A):")
    A_label.grid(row=3, column=0, padx=5, pady=5)

    A_entries = []
    for i in range(n):
        row_entries = []
        for j in range(n):
            entry = tk.Entry(root)
            entry.grid(row=i + 4, column=j, padx=5, pady=5)
            row_entries.append(entry)
        A_entries.append(row_entries)

    # Nhập vector cột (b)
    b_label = tk.Label(root, text="Vector cột (b):")
    b_label.grid(row=3 + n + 1, column=0, padx=5, pady=5)

    b_entries = []
    for i in range(n):
        entry = tk.Entry(root)
        entry.grid(row=i + 4 + n + 1, column=0, padx=5, pady=5)
        b_entries.append(entry)

    return A_entries, b_entries  # Trả về A_entries và b_entries

root.mainloop()