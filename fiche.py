from fpdf import FPDF
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class ModernFichePDF(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 10, self.title, ln=True, align="C", fill=True)
        self.ln(5)

    def add_box(self, title, content):
        self.set_font("Helvetica", "B", 12)
        self.set_fill_color(245, 245, 245)
        self.multi_cell(0, 8, title, border=1, fill=True)
        self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 8, content, border=1)
        self.ln(3)

def creer_interface():
    def exporter_pdf():
        titre = titre_entry.get().strip()
        if not titre:
            messagebox.showerror("Erreur", "Le titre est requis.")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Enregistrer la fiche PDF",
            initialfile=f"{titre}.pdf"
        )
        if not filepath:
            return

        pdf = ModernFichePDF(f"Fiche de révision - Texte {texte_num.get()}")
        pdf.add_page()

        pdf.add_box("INTRODUCTION", intro_text.get("1.0", "end").strip())
        pdf.add_box("MOUVEMENTS", mouvements_text.get("1.0", "end").strip())
        pdf.add_box("L'EXTRAIT PARLE DE", sujet_text.get("1.0", "end").strip())
        pdf.add_box("PROBLÉMATIQUE", probl_text.get("1.0", "end").strip())
        pdf.add_box("PROCÉDÉS RELEVÉS", proce_text.get("1.0", "end").strip())
        pdf.add_box("CONCLUSION", concl_text.get("1.0", "end").strip())
        pdf.add_box("OUVERTURE", ouverture_text.get("1.0", "end").strip())

        pdf.output(filepath)
        messagebox.showinfo("Succès", f"PDF enregistré sous : {filepath}")

    root = tk.Tk()
    root.title("Fiche Bac Français")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Segoe UI", 11))
    style.configure("TButton", font=("Segoe UI", 10), padding=6)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)

    ttk.Label(main_frame, text="Numéro du texte :").grid(row=0, column=0, sticky="w")
    texte_num = ttk.Combobox(main_frame, values=[str(i) for i in range(1, 17)], width=5)
    texte_num.grid(row=0, column=1, sticky="w")

    ttk.Label(main_frame, text="Titre de la fiche :").grid(row=0, column=2, padx=(20, 0), sticky="w")
    titre_entry = ttk.Entry(main_frame, width=40)
    titre_entry.grid(row=0, column=3, sticky="w")

    def add_field(label, row):
        ttk.Label(main_frame, text=label + " :").grid(row=row, column=0, columnspan=4, sticky="w", pady=(15, 0))
        text_widget = tk.Text(main_frame, height=4, width=100, wrap="word", font=("Segoe UI", 10))
        text_widget.grid(row=row + 1, column=0, columnspan=4, sticky="w")
        return text_widget

    intro_text = add_field("Introduction éléments", 1)
    mouvements_text = add_field("Mouvements du texte", 3)
    sujet_text = add_field("Résumé du texte", 5)
    probl_text = add_field("Problématique", 7)
    proce_text = add_field("Procédés importants", 9)
    concl_text = add_field("Conclusion", 11)
    ouverture_text = add_field("Ouverture", 13)

    export_btn = ttk.Button(main_frame, text="📄・Exporter en PDF", command=exporter_pdf)
    export_btn.grid(row=15, column=0, columnspan=4, pady=20)

    root.mainloop()

creer_interface()
