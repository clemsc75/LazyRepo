#!/usr/bin/env python3
"""
Launcher script for the File Selector Tool
Script de lancement pour l'Outil de Sélection de Fichier
"""

import sys
import os
from pathlib import Path

def main():
    """Main launcher function."""
    print("=== Sélecteur de Fichier / File Selector ===")
    print("Lancement de l'application... / Starting application...")
    print()
    
    # Check if file_selector.py exists
    script_dir = Path(__file__).parent
    file_selector_path = script_dir / "file_selector.py"
    
    if not file_selector_path.exists():
        print("❌ Erreur: file_selector.py non trouvé / Error: file_selector.py not found")
        print(f"Recherché dans / Looked in: {script_dir}")
        return 1
    
    # Check if tkinter is available
    try:
        import tkinter
        print("✅ tkinter disponible / tkinter available")
    except ImportError:
        print("❌ Erreur: tkinter non disponible / Error: tkinter not available")
        print("Installation requise / Installation required:")
        print("  Ubuntu/Debian: sudo apt install python3-tk")
        print("  macOS: brew install python-tk")
        print("  Windows: tkinter est généralement inclus / usually included")
        return 1
    
    # Import and run the application
    try:
        # Add the current directory to Python path
        sys.path.insert(0, str(script_dir))
        
        # Import and run the file selector
        from file_selector import main as run_file_selector
        print("🚀 Ouverture de l'interface... / Opening interface...")
        print()
        
        run_file_selector()
        
    except KeyboardInterrupt:
        print("\n👋 Application fermée par l'utilisateur / Application closed by user")
        return 0
    except Exception as e:
        print(f"❌ Erreur lors du lancement / Error during launch: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)