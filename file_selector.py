#!/usr/bin/env python3
"""
File Selector Tool - Outil de Sélection de Fichier

A simple tkinter-based GUI tool to select files from the computer
and copy them to an Output directory.

Un outil GUI simple basé sur tkinter pour sélectionner des fichiers
depuis l'ordinateur et les copier dans un répertoire Output.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import shutil
import os
from pathlib import Path


class FileSelector:
    """Main class for the file selector application."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sélecteur de Fichier - File Selector")
        self.root.geometry("500x350")
        self.root.resizable(True, True)
        
        # Create Output directory if it doesn't exist
        self.output_dir = Path("Output")
        self.output_dir.mkdir(exist_ok=True)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Sélecteur de Fichier", 
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Description
        desc_label = ttk.Label(
            main_frame,
            text="Sélectionnez un fichier pour le copier dans le dossier Output",
            font=("Arial", 10)
        )
        desc_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="Sélection de fichier", padding="10")
        file_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        file_frame.columnconfigure(1, weight=1)
        
        # Select file button
        self.select_btn = ttk.Button(
            file_frame, 
            text="Parcourir...", 
            command=self.select_file
        )
        self.select_btn.grid(row=0, column=0, padx=(0, 10))
        
        # Selected file label
        self.file_label = ttk.Label(
            file_frame, 
            text="Aucun fichier sélectionné", 
            foreground="gray"
        )
        self.file_label.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        # Copy button
        self.copy_btn = ttk.Button(
            main_frame, 
            text="Copier vers Output", 
            command=self.copy_file,
            state="disabled"
        )
        self.copy_btn.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        # Output directory info
        output_frame = ttk.LabelFrame(main_frame, text="Destination", padding="10")
        output_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        output_frame.columnconfigure(0, weight=1)
        
        output_path = os.path.abspath(self.output_dir)
        output_info = ttk.Label(
            output_frame,
            text=f"Dossier de destination: {output_path}",
            font=("Arial", 9)
        )
        output_info.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Open output folder button
        open_folder_btn = ttk.Button(
            output_frame,
            text="Ouvrir le dossier Output",
            command=self.open_output_folder
        )
        open_folder_btn.grid(row=1, column=0, pady=(10, 0))
        
        # Status label
        self.status_label = ttk.Label(
            main_frame, 
            text="Prêt", 
            foreground="green",
            font=("Arial", 9)
        )
        self.status_label.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        
        # Store selected file path
        self.selected_file = None
        
    def select_file(self):
        """Open file dialog to select a file."""
        filetypes = [
            ("Tous les fichiers", "*.*"),
            ("Documents texte", "*.txt"),
            ("Images", "*.png *.jpg *.jpeg *.gif *.bmp"),
            ("Documents PDF", "*.pdf"),
            ("Documents Word", "*.doc *.docx"),
            ("Feuilles de calcul", "*.xls *.xlsx"),
            ("Archives", "*.zip *.rar *.7z")
        ]
        
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier",
            filetypes=filetypes
        )
        
        if file_path:
            self.selected_file = file_path
            filename = os.path.basename(file_path)
            self.file_label.config(text=filename, foreground="black")
            self.copy_btn.config(state="normal")
            self.status_label.config(text=f"Fichier sélectionné: {filename}", foreground="blue")
        
    def copy_file(self):
        """Copy the selected file to the Output directory."""
        if not self.selected_file:
            messagebox.showerror("Erreur", "Aucun fichier sélectionné")
            return
            
        try:
            # Get filename
            filename = os.path.basename(self.selected_file)
            destination = self.output_dir / filename
            
            # Handle file name conflicts
            counter = 1
            original_stem = destination.stem
            original_suffix = destination.suffix
            
            while destination.exists():
                new_name = f"{original_stem}_{counter}{original_suffix}"
                destination = self.output_dir / new_name
                counter += 1
            
            # Copy the file
            shutil.copy2(self.selected_file, destination)
            
            # Show success message
            success_msg = f"Fichier copié avec succès:\n{destination.name}"
            messagebox.showinfo("Succès", success_msg)
            
            # Update status
            self.status_label.config(
                text=f"Copié: {destination.name}", 
                foreground="green"
            )
            
        except Exception as e:
            error_msg = f"Erreur lors de la copie:\n{str(e)}"
            messagebox.showerror("Erreur", error_msg)
            self.status_label.config(text="Erreur lors de la copie", foreground="red")
    
    def open_output_folder(self):
        """Open the Output folder in the system file manager."""
        try:
            output_path = os.path.abspath(self.output_dir)
            
            # Platform-specific folder opening
            import platform
            system = platform.system()
            
            if system == "Windows":
                os.startfile(output_path)
            elif system == "Darwin":  # macOS
                os.system(f"open '{output_path}'")
            else:  # Linux and others
                os.system(f"xdg-open '{output_path}'")
                
        except Exception as e:
            messagebox.showwarning(
                "Information", 
                f"Impossible d'ouvrir le dossier automatiquement.\n"
                f"Chemin: {os.path.abspath(self.output_dir)}"
            )


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = FileSelector(root)
    root.mainloop()


if __name__ == "__main__":
    main()