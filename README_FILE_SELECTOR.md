# Sélecteur de Fichier - File Selector Tool

Un outil GUI simple basé sur tkinter pour sélectionner des fichiers depuis l'ordinateur et les copier dans un répertoire Output.

A simple tkinter-based GUI tool to select files from the computer and copy them to an Output directory.

## Installation et Utilisation / Installation and Usage

### Prérequis / Prerequisites

- Python 3.x
- tkinter (généralement inclus avec Python / usually included with Python)

### Installation des dépendances / Installing dependencies

```bash
# Si tkinter n'est pas installé / If tkinter is not installed
# Sur Ubuntu/Debian:
sudo apt install python3-tk

# Sur macOS avec Homebrew:
brew install python-tk

# Sur Windows, tkinter est généralement inclus avec Python
```

### Utilisation / Usage

1. **Lancer l'application / Run the application:**
   ```bash
   python3 file_selector.py
   ```

2. **Interface utilisateur / User interface:**
   - Cliquez sur "Parcourir..." pour sélectionner un fichier
   - Click "Parcourir..." to select a file
   - Le fichier sélectionné apparaîtra dans l'interface
   - The selected file will appear in the interface
   - Cliquez sur "Copier vers Output" pour copier le fichier
   - Click "Copier vers Output" to copy the file
   - Le fichier sera copié dans le dossier `Output`
   - The file will be copied to the `Output` folder

3. **Gestion des conflits de noms / Name conflict handling:**
   - Si un fichier avec le même nom existe déjà, un suffixe numérique sera ajouté
   - If a file with the same name already exists, a numeric suffix will be added
   - Exemple / Example: `document.txt` → `document_1.txt`

## Fonctionnalités / Features

- ✅ Interface graphique intuitive / Intuitive graphical interface
- ✅ Sélection de fichiers avec dialogue natif / File selection with native dialog
- ✅ Gestion automatique des conflits de noms / Automatic name conflict handling
- ✅ Création automatique du dossier Output / Automatic Output folder creation
- ✅ Feedback utilisateur (messages de succès/erreur) / User feedback (success/error messages)
- ✅ Ouverture du dossier de destination / Open destination folder
- ✅ Support multi-plateforme / Cross-platform support

## Structure du projet / Project structure

```
LazyRepo/
├── file_selector.py    # Application principale / Main application
├── Output/            # Dossier de destination / Destination folder
├── test_file.txt      # Fichier de test / Test file
└── README_FILE_SELECTOR.md  # Cette documentation / This documentation
```

## Types de fichiers supportés / Supported file types

L'outil accepte tous types de fichiers, avec des filtres prédéfinis pour :
The tool accepts all file types, with predefined filters for:

- Tous les fichiers / All files (`*.*`)
- Documents texte / Text documents (`.txt`)
- Images (`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`)
- Documents PDF (`.pdf`)
- Documents Word (`.doc`, `.docx`)
- Feuilles de calcul / Spreadsheets (`.xls`, `.xlsx`)
- Archives (`.zip`, `.rar`, `.7z`)

## Exemple d'utilisation / Usage example

1. Lancez l'application / Launch the application
2. Cliquez sur "Parcourir..." / Click "Parcourir..."
3. Sélectionnez un fichier dans votre système / Select a file from your system
4. Cliquez sur "Copier vers Output" / Click "Copier vers Output"
5. Le fichier est maintenant disponible dans le dossier Output / The file is now available in the Output folder

## Messages d'erreur courants / Common error messages

- **"Aucun fichier sélectionné"** : Vous devez d'abord sélectionner un fichier
- **"Erreur lors de la copie"** : Vérifiez les permissions et l'espace disque
- **"No file selected"** : You must first select a file
- **"Copy error"** : Check permissions and disk space