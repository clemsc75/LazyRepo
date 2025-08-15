"""
LazyRepo - Interface de Démonstration
PROMPT 1 + 2: Structure de Base + Chat IA Assistant Configuration

Interface de présentation pure - Les fonctionnalités sont simulées pour la démonstration
Aucun traitement réel n'est effectué, c'est normal et voulu.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import random
import datetime


class OptionsManager:
    """Gestionnaire des équipes et agents LazyRepo pour la démonstration"""
    
    def __init__(self, parent_frame, app_instance=None):
        self.parent_frame = parent_frame
        self.app_instance = app_instance  # Référence vers l'app principale pour notifications IA
        self.categories = {}
        self.setup_crews_interface()
    
    def setup_crews_interface(self):
        """Configure l'interface des 4 crews LazyRepo"""
        # Clear existing widgets
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        
        # Titre principal des crews
        title_frame = ttk.Frame(self.parent_frame)
        title_frame.pack(fill="x", padx=20, pady=15)
        
        ttk.Label(title_frame, text="🚀 LazyRepo - Configuration des Crews IA", 
                 font=("Arial", 16, "bold")).pack(anchor="center")
        ttk.Label(title_frame, text="Sélectionnez les équipes d'agents IA pour automatiser votre projet", 
                 font=("Arial", 10)).pack(pady=(5, 0), anchor="center")
        
        # Définition des 4 crews principaux
        crews_data = {
            "📚 Documentation Crew": {
                "README.md automatique": "Génération de documentation complète avec analyse du code source",
                "Documentation API": "Création de docs techniques pour les API et modules",
                "Guides d'installation": "Instructions détaillées par environnement et plateforme"
            },
            "🔧 Code Improvement Crew": {
                "Amélioration du code": "Ajout de commentaires et suggestions d'optimisation",
                "Standards de qualité": "Application des conventions (PEP 8, ESLint, etc.)",
                "Refactoring intelligent": "Suggestions d'amélioration structurelle"
            },
            "🔒 Security Crew": {
                "Scan de sécurité": "Détection de vulnérabilités et informations sensibles",
                "Gestion des secrets": "Migration vers .env et variables d'environnement",
                "Configuration sécurisée": "Génération de .gitignore et fichiers de sécurité"
            },
            "📱 Social Content Crew": {
                "Posts LinkedIn": "Contenu professionnel pour présenter le projet",
                "Descriptions GitHub": "Optimisation des descriptions de dépôt",
                "Documentation marketing": "Contenu promotionnel et cas d'usage"
            }
        }
        
        # Créer chaque crew
        for crew_name, agents in crews_data.items():
            self.create_crew_section(crew_name, agents)
    
    def create_crew_section(self, crew_name, agents):
        """Crée une section pour une équipe"""
        # Frame principal de l'équipe
        crew_frame = ttk.LabelFrame(self.parent_frame, text=crew_name, padding=15)
        crew_frame.pack(fill="x", padx=20, pady=8, anchor="center")
        
        # Contrôles de l'équipe
        control_frame = ttk.Frame(crew_frame)
        control_frame.pack(fill="x", pady=(0, 10))
        
        # Boutons d'activation/désactivation
        activate_btn = ttk.Button(control_frame, text="✅ Activer toute l'équipe", 
                                 command=lambda: self.demo_activate_crew(crew_name, True))
        activate_btn.pack(side="left", padx=(0, 5))
        
        deactivate_btn = ttk.Button(control_frame, text="❌ Désactiver l'équipe", 
                                   command=lambda: self.demo_activate_crew(crew_name, False))
        deactivate_btn.pack(side="left")
        
        # Compteur d'agents actifs
        count_label = ttk.Label(control_frame, text="0/3 agent(s) actif(s)", foreground="gray")
        count_label.pack(side="right")
        
        # Stocker les informations de l'équipe
        self.categories[crew_name] = {
            'agents': {},
            'count_label': count_label,
            'activate_btn': activate_btn,
            'deactivate_btn': deactivate_btn
        }
        
        # Frame pour les agents
        agents_frame = ttk.Frame(crew_frame)
        agents_frame.pack(fill="x")
        
        # Créer les checkboxes pour chaque agent
        for agent_name, description in agents.items():
            agent_frame = ttk.Frame(agents_frame)
            agent_frame.pack(fill="x", pady=3)
            
            var = tk.BooleanVar(value=False)
            var.trace('w', lambda *args, crew=crew_name: self.update_crew_count(crew))
            
            checkbox = ttk.Checkbutton(agent_frame, text=f"🤖 {agent_name}", variable=var)
            checkbox.pack(side="left")
            
            # Description de l'agent
            desc_label = ttk.Label(agent_frame, text=f"  → {description}", 
                                  foreground="gray", font=("Arial", 9))
            desc_label.pack(side="left")
            
            self.categories[crew_name]['agents'][agent_name] = var
    
    def demo_activate_crew(self, crew_name, activate):
        """Démonstration: Active/désactive une équipe"""
        if crew_name in self.categories:
            for var in self.categories[crew_name]['agents'].values():
                var.set(activate)
            
            # Message de confirmation
            action = "activée" if activate else "désactivée"
            messagebox.showinfo("Démonstration", 
                               f"🎭 Mode démonstration\n\n"
                               f"Équipe {crew_name} {action} !\n\n"
                               f"Dans la vraie application, ceci configurerait "
                               f"les agents IA correspondants.")
    
    def update_crew_count(self, crew_name):
        """Met à jour le compteur d'agents actifs"""
        if crew_name in self.categories:
            active_count = sum(1 for var in self.categories[crew_name]['agents'].values() if var.get())
            total_count = len(self.categories[crew_name]['agents'])
            
            self.categories[crew_name]['count_label'].config(
                text=f"{active_count}/{total_count} agent(s) actif(s)",
                foreground="green" if active_count > 0 else "gray"
            )
            
            # Notifier l'IA des changements de sélection
            if self.app_instance and hasattr(self.app_instance, 'notify_ai_selection_change'):
                self.app_instance.notify_ai_selection_change(crew_name, active_count > 0)
    
    def get_selected_crews(self):
        """Retourne un résumé des équipes sélectionnées (pour démonstration)"""
        selected = {}
        for crew_name, crew_data in self.categories.items():
            selected[crew_name] = {}
            for agent_name, var in crew_data['agents'].items():
                selected[crew_name][agent_name] = var.get()
        return selected


class LazyRepoDemo:
    """Interface principale de démonstration LazyRepo"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("LazyRepo - Interface de Démonstration")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f0f0f0")
        
        # Variables pour la démonstration
        self.project_name = tk.StringVar(value="Mon Projet")
        self.project_path = tk.StringVar(value="Aucun dossier sélectionné")
        self.languages_vars = {}
        
        # Variables pour le chat IA
        self.chat_history = []
        self.ai_questions_asked = set()
        self.ai_notification_cooldown = False
        
        # Variables pour l'onglet Résultats (PROMPT 3)
        self.analysis_progress = 0
        self.analysis_running = False
        self.demo_metrics = {}
        self.generated_files = []
        self.current_result_category = "Documentation"
        
        # Variables pour l'onglet Amélioration (PROMPT 4)
        self.scanned_files = []
        self.selected_files_for_improvement = []
        self.improvement_chat_history = []
        self.improvement_suggestions = []
        self.file_modifications_history = []
        
        # Variables pour l'intégration IA globale (PROMPT 5)
        self.global_ai_context = {}
        self.cross_tab_notifications = []
        self.smart_recommendations = []
        self.workflow_stage = "configuration"  # configuration, analysis, results, improvement
        self.ai_learning_data = {
            "user_preferences": {},
            "project_patterns": {},
            "interaction_history": []
        }
        
        # Langages supportés (32+ langages)
        self.all_languages = [
            "Python", "JavaScript", "TypeScript", "Java", "C#", "C++", "C", 
            "Go", "Rust", "PHP", "Ruby", "Swift", "Kotlin", "Scala", 
            "R", "MATLAB", "Perl", "Shell", "PowerShell", "HTML", "CSS", 
            "SQL", "Assembly", "Objective-C", "Dart", "Lua", "Haskell", 
            "Clojure", "F#", "VB.NET", "COBOL", "Fortran", "Autre"
        ]
        
        self.setup_interface()
    
    def setup_interface(self):
        """Configure l'interface principale"""
        # Créer le notebook avec 3 onglets
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Onglet 1: Configuration (principal)
        self.config_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.config_frame, text="⚙️ Configuration des Crews")
        
        # Onglet 2: Résultats (désactivé au début)
        self.results_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.results_frame, text="📊 Résultats de l'analyse")
        self.notebook.tab(1, state="disabled")  # Désactivé au début
        
        # Onglet 3: Amélioration (accessible)
        self.improvement_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.improvement_frame, text="🔄 Retour & Amélioration")
        
        self.setup_config_tab()
        self.setup_results_tab()
        self.setup_improvement_tab()
        
        # Initialiser l'intégration IA globale (PROMPT 5)
        self.setup_global_ai_integration()
        self.setup_cross_tab_notifications()
        
        # Bind event pour changement d'onglet
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)
    
    def setup_config_tab(self):
        """Configure l'onglet Configuration avec scrolling"""
        # Créer un canvas scrollable
        self.config_canvas = tk.Canvas(self.config_frame, highlightthickness=0, bg="#f0f0f0")
        self.config_scrollbar = ttk.Scrollbar(self.config_frame, orient="vertical", 
                                             command=self.config_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.config_canvas)
        
        # Configuration du scrolling
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.config_canvas.configure(scrollregion=self.config_canvas.bbox("all"))
        )
        
        # Créer la fenêtre dans le canvas
        self.canvas_window = self.config_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.config_canvas.configure(yscrollcommand=self.config_scrollbar.set)
        
        # Centrage automatique
        self.config_canvas.bind("<Configure>", self.center_content)
        
        # Pack canvas et scrollbar
        self.config_canvas.pack(side="left", fill="both", expand=True)
        self.config_scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.config_canvas.bind("<MouseWheel>", self.on_mousewheel)
        
        # Contenu de l'onglet configuration
        self.create_project_config_section()
        self.create_languages_section()
        self.create_crews_section()
        self.create_ai_chat_section()
        self.create_action_buttons()
    
    def center_content(self, event):
        """Centre le contenu dans le canvas"""
        canvas_width = event.width
        frame_width = self.scrollable_frame.winfo_reqwidth()
        
        if frame_width < canvas_width:
            x_position = (canvas_width - frame_width) // 2
        else:
            x_position = 0
        
        self.config_canvas.coords(self.canvas_window, x_position, 0)
    
    def on_mousewheel(self, event):
        """Gestion du scroll avec la molette"""
        self.config_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_project_config_section(self):
        """Crée la section configuration du projet"""
        project_frame = ttk.LabelFrame(self.scrollable_frame, text="🎯 Configuration du projet", padding=15)
        project_frame.pack(fill="x", padx=20, pady=10)
        
        # Nom du projet
        ttk.Label(project_frame, text="Nom du projet:", font=("Arial", 10, "bold")).pack(anchor="w")
        name_entry = ttk.Entry(project_frame, textvariable=self.project_name, width=40, font=("Arial", 10))
        name_entry.pack(anchor="w", pady=(5, 15))
        
        # Sélection du dossier
        folder_frame = ttk.Frame(project_frame)
        folder_frame.pack(fill="x", pady=(0, 15))
        
        ttk.Label(folder_frame, text="Dossier du projet:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        path_frame = ttk.Frame(folder_frame)
        path_frame.pack(fill="x", pady=5)
        
        self.path_label = ttk.Label(path_frame, textvariable=self.project_path, 
                                   foreground="gray", font=("Arial", 9))
        self.path_label.pack(side="left", fill="x", expand=True)
        
        browse_btn = ttk.Button(path_frame, text="📁 Parcourir", 
                               command=self.demo_browse_folder)
        browse_btn.pack(side="right", padx=(10, 0))
    
    def create_languages_section(self):
        """Crée la section détection des langages"""
        languages_frame = ttk.LabelFrame(self.scrollable_frame, 
                                        text="🔍 Langages de programmation", padding=15)
        languages_frame.pack(fill="x", padx=20, pady=10)
        
        # Bouton de détection
        detect_frame = ttk.Frame(languages_frame)
        detect_frame.pack(fill="x", pady=(0, 15))
        
        ttk.Label(detect_frame, text="Détection automatique des langages:", 
                 font=("Arial", 10, "bold")).pack(side="left")
        detect_btn = ttk.Button(detect_frame, text="🔍 Analyser le projet", 
                               command=self.demo_detect_languages)
        detect_btn.pack(side="right")
        
        # Grille de checkboxes pour les langages
        self.languages_frame = ttk.Frame(languages_frame)
        self.languages_frame.pack(fill="x")
        
        self.setup_languages_checkboxes()
    
    def setup_languages_checkboxes(self):
        """Configure les checkboxes des langages en colonnes"""
        # Clear existing
        for widget in self.languages_frame.winfo_children():
            widget.destroy()
        
        self.languages_vars.clear()
        
        # Créer en 4 colonnes
        columns = 4
        for i, language in enumerate(self.all_languages):
            row = i // columns
            col = i % columns
            
            var = tk.BooleanVar(value=False)
            self.languages_vars[language] = var
            
            checkbox = ttk.Checkbutton(self.languages_frame, text=language, variable=var)
            checkbox.grid(row=row, column=col, sticky="w", padx=15, pady=3)
        
        # Configurer les colonnes
        for col in range(columns):
            self.languages_frame.columnconfigure(col, weight=1)
    
    def create_crews_section(self):
        """Crée la section des crews avec OptionsManager"""
        crews_container = ttk.Frame(self.scrollable_frame)
        crews_container.pack(fill="x", padx=0, pady=10)
        
        # Initialiser le gestionnaire d'équipes avec référence vers l'app
        self.options_manager = OptionsManager(crews_container, self)
    
    def create_ai_chat_section(self):
        """Crée la section Chat IA Assistant Configuration"""
        chat_frame = ttk.LabelFrame(self.scrollable_frame, text="🤖 Assistant IA - Personnalisation avancée", padding=15)
        chat_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Introduction du chat
        intro_frame = ttk.Frame(chat_frame)
        intro_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(intro_frame, text="💬 Discutez avec l'assistant IA pour personnaliser votre analyse", 
                 font=("Arial", 11, "bold")).pack(anchor="w")
        ttk.Label(intro_frame, text="L'IA adapte ses questions selon vos sélections d'équipes et de langages", 
                 foreground="gray", font=("Arial", 9)).pack(anchor="w")
        
        # Zone d'affichage du chat
        chat_display_frame = ttk.Frame(chat_frame)
        chat_display_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        # Text widget avec scrollbar pour le chat
        chat_scrollbar = ttk.Scrollbar(chat_display_frame)
        chat_scrollbar.pack(side="right", fill="y")
        
        self.chat_display = tk.Text(chat_display_frame, height=12, state="disabled", 
                                   wrap=tk.WORD, bg="#f8f9fa", yscrollcommand=chat_scrollbar.set,
                                   font=("Arial", 9))
        self.chat_display.pack(side="left", fill="both", expand=True)
        chat_scrollbar.config(command=self.chat_display.yview)
        
        # Zone de saisie
        input_chat_frame = ttk.Frame(chat_frame)
        input_chat_frame.pack(fill="x")
        
        self.chat_entry = tk.Entry(input_chat_frame, font=("Arial", 10))
        self.chat_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.chat_entry.bind("<Return>", self.send_chat_message)
        
        send_chat_btn = ttk.Button(input_chat_frame, text="💬 Envoyer", 
                                  command=self.send_chat_message)
        send_chat_btn.pack(side="right")
        
        # Message d'accueil de l'IA
        self.add_ai_message("🤖 Assistant IA", 
                           "Bonjour ! Je suis l'assistant IA de LazyRepo. 🚀\n\n"
                           "Je peux vous aider à personnaliser votre analyse en fonction de vos besoins spécifiques.\n"
                           "Sélectionnez des équipes et des langages, puis je vous poserai des questions pertinentes !\n\n"
                           "💡 Tapez 'aide' pour voir ce que je peux faire.")
    
    def create_action_buttons(self):
        """Crée les boutons d'action finaux"""
        action_frame = ttk.Frame(self.scrollable_frame)
        action_frame.pack(fill="x", padx=20, pady=20)
        
        # Bouton principal
        main_btn = ttk.Button(action_frame, text="🚀 Lancer l'analyse LazyRepo", 
                             command=self.demo_start_analysis)
        main_btn.pack(side="right", padx=(10, 0))
        
        # Bouton de configuration
        config_btn = ttk.Button(action_frame, text="👁️ Voir la configuration", 
                               command=self.demo_show_config)
        config_btn.pack(side="right")
    
    def setup_improvement_tab(self):
        """Configure l'onglet Amélioration avec scanner et IA (PROMPT 4)"""
        # Canvas scrollable pour l'amélioration
        self.improvement_canvas = tk.Canvas(self.improvement_frame, highlightthickness=0, bg="#f0f0f0")
        self.improvement_scrollbar = ttk.Scrollbar(self.improvement_frame, orient="vertical", 
                                                  command=self.improvement_canvas.yview)
        self.improvement_scrollable_frame = ttk.Frame(self.improvement_canvas)
        
        # Configuration du scrolling
        self.improvement_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.improvement_canvas.configure(scrollregion=self.improvement_canvas.bbox("all"))
        )
        
        # Créer la fenêtre dans le canvas
        self.improvement_canvas_window = self.improvement_canvas.create_window((0, 0), 
                                                                              window=self.improvement_scrollable_frame, 
                                                                              anchor="nw")
        self.improvement_canvas.configure(yscrollcommand=self.improvement_scrollbar.set)
        
        # Centrage automatique
        self.improvement_canvas.bind("<Configure>", self.center_improvement_content)
        
        # Pack canvas et scrollbar
        self.improvement_canvas.pack(side="left", fill="both", expand=True)
        self.improvement_scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.improvement_canvas.bind("<MouseWheel>", self.on_improvement_mousewheel)
        
        # Contenu de l'onglet amélioration
        self.create_improvement_header()
        self.create_file_scanner_section()
        self.create_quick_actions_section()
        self.create_improvement_chat_section()
        self.create_modifications_history_section()
    
    def center_improvement_content(self, event):
        """Centre le contenu de l'amélioration dans le canvas"""
        canvas_width = event.width
        frame_width = self.improvement_scrollable_frame.winfo_reqwidth()
        
        if frame_width < canvas_width:
            x_position = (canvas_width - frame_width) // 2
        else:
            x_position = 0
        
        self.improvement_canvas.coords(self.improvement_canvas_window, x_position, 0)
    
    def on_improvement_mousewheel(self, event):
        """Gestion du scroll avec la molette pour l'amélioration"""
        self.improvement_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_improvement_header(self):
        """Crée l'en-tête de l'onglet amélioration"""
        header_frame = ttk.Frame(self.improvement_scrollable_frame)
        header_frame.pack(fill="x", padx=20, pady=15)
        
        ttk.Label(header_frame, text="🔄 Retour & Amélioration Continue", 
                 font=("Arial", 18, "bold")).pack(anchor="center")
        ttk.Label(header_frame, text="Scannez vos fichiers et obtenez des suggestions d'amélioration personnalisées", 
                 font=("Arial", 11), foreground="gray").pack(pady=(5, 0), anchor="center")
    
    def create_file_scanner_section(self):
        """Crée la section scanner de fichiers"""
        scanner_frame = ttk.LabelFrame(self.improvement_scrollable_frame, 
                                      text="📁 Scanner de Fichiers du Projet", padding=15)
        scanner_frame.pack(fill="x", padx=20, pady=10)
        
        # Contrôles du scanner
        controls_frame = ttk.Frame(scanner_frame)
        controls_frame.pack(fill="x", pady=(0, 15))
        
        # Boutons de scan
        scan_buttons_frame = ttk.Frame(controls_frame)
        scan_buttons_frame.pack(fill="x")
        
        ttk.Button(scan_buttons_frame, text="🔍 Scanner le projet", 
                  command=self.demo_scan_project).pack(side="left", padx=(0, 10))
        ttk.Button(scan_buttons_frame, text="📄 Scanner fichiers spécifiques", 
                  command=self.demo_scan_specific_files).pack(side="left", padx=(0, 10))
        ttk.Button(scan_buttons_frame, text="🔄 Actualiser", 
                  command=self.demo_refresh_scan).pack(side="left")
        
        # Filtres
        filters_frame = ttk.Frame(controls_frame)
        filters_frame.pack(fill="x", pady=(10, 0))
        
        ttk.Label(filters_frame, text="Filtres:", font=("Arial", 10, "bold")).pack(side="left")
        
        # Filtre par type de fichier
        self.file_type_filter = tk.StringVar(value="Tous")
        file_types = ["Tous", "Python (.py)", "JavaScript (.js)", "HTML (.html)", "CSS (.css)", "Markdown (.md)", "JSON (.json)"]
        filter_combo = ttk.Combobox(filters_frame, textvariable=self.file_type_filter, 
                                   values=file_types, state="readonly", width=15)
        filter_combo.pack(side="left", padx=(10, 10))
        filter_combo.bind("<<ComboboxSelected>>", self.apply_file_filters)
        
        # Filtre par taille
        ttk.Label(filters_frame, text="Taille max:", font=("Arial", 9)).pack(side="left")
        self.size_filter = tk.StringVar(value="Toutes")
        size_options = ["Toutes", "< 1KB", "< 10KB", "< 100KB", "< 1MB"]
        size_combo = ttk.Combobox(filters_frame, textvariable=self.size_filter, 
                                 values=size_options, state="readonly", width=10)
        size_combo.pack(side="left", padx=(5, 0))
        size_combo.bind("<<ComboboxSelected>>", self.apply_file_filters)
        
        # Liste des fichiers scannés
        files_list_frame = ttk.Frame(scanner_frame)
        files_list_frame.pack(fill="both", expand=True)
        
        # En-tête de la liste
        list_header_frame = ttk.Frame(files_list_frame)
        list_header_frame.pack(fill="x", pady=(0, 5))
        
        ttk.Label(list_header_frame, text="Fichiers détectés:", 
                 font=("Arial", 10, "bold")).pack(side="left")
        self.files_count_label = ttk.Label(list_header_frame, text="0 fichier(s)", 
                                          foreground="gray", font=("Arial", 9))
        self.files_count_label.pack(side="right")
        
        # Treeview pour afficher les fichiers avec colonnes
        tree_frame = ttk.Frame(files_list_frame)
        tree_frame.pack(fill="both", expand=True)
        
        # Scrollbars pour le Treeview
        tree_v_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
        tree_v_scrollbar.pack(side="right", fill="y")
        
        tree_h_scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal")
        tree_h_scrollbar.pack(side="bottom", fill="x")
        
        # Treeview avec colonnes
        columns = ("nom", "type", "taille", "modification", "statut")
        self.files_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8,
                                      yscrollcommand=tree_v_scrollbar.set,
                                      xscrollcommand=tree_h_scrollbar.set)
        
        # Configuration des colonnes
        self.files_tree.heading("nom", text="📄 Nom du fichier")
        self.files_tree.heading("type", text="🏷️ Type")
        self.files_tree.heading("taille", text="📏 Taille")
        self.files_tree.heading("modification", text="📅 Modifié")
        self.files_tree.heading("statut", text="🔍 Statut")
        
        self.files_tree.column("nom", width=250)
        self.files_tree.column("type", width=80)
        self.files_tree.column("taille", width=80)
        self.files_tree.column("modification", width=120)
        self.files_tree.column("statut", width=100)
        
        self.files_tree.pack(side="left", fill="both", expand=True)
        
        tree_v_scrollbar.config(command=self.files_tree.yview)
        tree_h_scrollbar.config(command=self.files_tree.xview)
        
        # Bind events
        self.files_tree.bind("<Double-1>", self.on_file_double_click)
        self.files_tree.bind("<Button-3>", self.show_file_context_menu)  # Clic droit
    
    def create_quick_actions_section(self):
        """Crée la section actions rapides"""
        actions_frame = ttk.LabelFrame(self.improvement_scrollable_frame, 
                                      text="⚡ Actions Rapides", padding=15)
        actions_frame.pack(fill="x", padx=20, pady=10)
        
        # Sélection de fichiers
        selection_frame = ttk.Frame(actions_frame)
        selection_frame.pack(fill="x", pady=(0, 15))
        
        ttk.Label(selection_frame, text="Fichiers sélectionnés:", 
                 font=("Arial", 10, "bold")).pack(side="left")
        self.selected_files_label = ttk.Label(selection_frame, text="Aucun fichier sélectionné", 
                                             foreground="gray", font=("Arial", 9))
        self.selected_files_label.pack(side="left", padx=(10, 0))
        
        ttk.Button(selection_frame, text="✅ Sélectionner tout", 
                  command=self.select_all_files).pack(side="right", padx=(10, 0))
        ttk.Button(selection_frame, text="❌ Désélectionner tout", 
                  command=self.deselect_all_files).pack(side="right")
        
        # Actions disponibles
        actions_grid_frame = ttk.Frame(actions_frame)
        actions_grid_frame.pack(fill="x", pady=10)
        
        # Première rangée d'actions
        row1_frame = ttk.Frame(actions_grid_frame)
        row1_frame.pack(fill="x", pady=(0, 8))
        
        ttk.Button(row1_frame, text="📝 Ajouter commentaires", 
                  command=lambda: self.demo_quick_action("comments")).pack(side="left", padx=(0, 10))
        ttk.Button(row1_frame, text="🔒 Sécuriser les secrets", 
                  command=lambda: self.demo_quick_action("security")).pack(side="left", padx=(0, 10))
        ttk.Button(row1_frame, text="📚 Générer docstrings", 
                  command=lambda: self.demo_quick_action("docstrings")).pack(side="left", padx=(0, 10))
        
        # Deuxième rangée d'actions
        row2_frame = ttk.Frame(actions_grid_frame)
        row2_frame.pack(fill="x", pady=(0, 8))
        
        ttk.Button(row2_frame, text="🎨 Formater le code", 
                  command=lambda: self.demo_quick_action("format")).pack(side="left", padx=(0, 10))
        ttk.Button(row2_frame, text="🐛 Détecter les bugs", 
                  command=lambda: self.demo_quick_action("bugs")).pack(side="left", padx=(0, 10))
        ttk.Button(row2_frame, text="⚡ Optimiser performance", 
                  command=lambda: self.demo_quick_action("optimize")).pack(side="left", padx=(0, 10))
        
        # Troisième rangée d'actions
        row3_frame = ttk.Frame(actions_grid_frame)
        row3_frame.pack(fill="x")
        
        ttk.Button(row3_frame, text="🧪 Générer tests", 
                  command=lambda: self.demo_quick_action("tests")).pack(side="left", padx=(0, 10))
        ttk.Button(row3_frame, text="📋 Analyser complexité", 
                  command=lambda: self.demo_quick_action("complexity")).pack(side="left", padx=(0, 10))
        ttk.Button(row3_frame, text="🔄 Refactoring", 
                  command=lambda: self.demo_quick_action("refactor")).pack(side="left", padx=(0, 10))
    
    def create_improvement_chat_section(self):
        """Crée la section chat IA d'amélioration"""
        chat_frame = ttk.LabelFrame(self.improvement_scrollable_frame, 
                                   text="🤖 Assistant IA - Amélioration Spécialisée", padding=15)
        chat_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Introduction spécialisée
        intro_frame = ttk.Frame(chat_frame)
        intro_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(intro_frame, text="💬 Chat spécialisé dans l'amélioration et l'optimisation de code", 
                 font=("Arial", 11, "bold")).pack(anchor="w")
        ttk.Label(intro_frame, text="Posez des questions sur vos fichiers, demandez des suggestions d'amélioration spécifiques", 
                 foreground="gray", font=("Arial", 9)).pack(anchor="w")
        
        # Zone d'affichage du chat d'amélioration
        improvement_chat_display_frame = ttk.Frame(chat_frame)
        improvement_chat_display_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        # Text widget avec scrollbar pour le chat d'amélioration
        improvement_chat_scrollbar = ttk.Scrollbar(improvement_chat_display_frame)
        improvement_chat_scrollbar.pack(side="right", fill="y")
        
        self.improvement_chat_display = tk.Text(improvement_chat_display_frame, height=10, state="disabled", 
                                               wrap=tk.WORD, bg="#f8f9fa", yscrollcommand=improvement_chat_scrollbar.set,
                                               font=("Arial", 9))
        self.improvement_chat_display.pack(side="left", fill="both", expand=True)
        improvement_chat_scrollbar.config(command=self.improvement_chat_display.yview)
        
        # Zone de saisie pour l'amélioration
        input_improvement_chat_frame = ttk.Frame(chat_frame)
        input_improvement_chat_frame.pack(fill="x")
        
        self.improvement_chat_entry = tk.Entry(input_improvement_chat_frame, font=("Arial", 10))
        self.improvement_chat_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.improvement_chat_entry.bind("<Return>", self.send_improvement_chat_message)
        
        send_improvement_btn = ttk.Button(input_improvement_chat_frame, text="💬 Demander amélioration", 
                                         command=self.send_improvement_chat_message)
        send_improvement_btn.pack(side="right")
        
        # Message d'accueil spécialisé
        self.add_improvement_chat_message("🤖 Assistant Amélioration", 
                                         "Bonjour ! Je suis l'assistant IA spécialisé en amélioration de code. 🔧\n\n"
                                         "Je peux vous aider à :\n"
                                         "• 📝 Analyser la qualité de votre code\n"
                                         "• 🐛 Détecter les problèmes potentiels\n"
                                         "• ⚡ Suggérer des optimisations\n"
                                         "• 🧪 Proposer des tests\n"
                                         "• 📚 Améliorer la documentation\n\n"
                                         "Scannez d'abord vos fichiers, puis posez-moi vos questions !")
        
        # ============ ASSISTANT CUSTOMER SERVICE/SAV (PROMPT 6) ============
        self.create_customer_service_chat_section()
    
    def create_customer_service_chat_section(self):
        """Crée la section Assistant Customer Service/SAV (PROMPT 6)"""
        # Section Assistant Customer Service
        cs_chat_frame = ttk.LabelFrame(self.improvement_scrollable_frame, 
                                      text="🎧 Assistant Customer Service - SAV Personnalisation", padding=15)
        cs_chat_frame.pack(fill="x", padx=20, pady=(15, 10))
        
        # Description du service
        cs_description = ttk.Label(cs_chat_frame, 
                                  text="Assistant spécialisé dans la personnalisation et l'ajustement des modifications générées",
                                  font=("Arial", 9), foreground="#374151")
        cs_description.pack(anchor="w", pady=(0, 10))
        
        # Zone d'affichage du chat Customer Service
        cs_chat_display_frame = ttk.Frame(cs_chat_frame)
        cs_chat_display_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        cs_chat_scrollbar = ttk.Scrollbar(cs_chat_display_frame)
        cs_chat_scrollbar.pack(side="right", fill="y")
        
        self.cs_chat_display = tk.Text(cs_chat_display_frame, height=8, state="disabled", 
                                      wrap=tk.WORD, bg="#f0f9ff", yscrollcommand=cs_chat_scrollbar.set,
                                      font=("Arial", 9), relief="solid", borderwidth=1)
        self.cs_chat_display.pack(side="left", fill="both", expand=True)
        cs_chat_scrollbar.config(command=self.cs_chat_display.yview)
        
        # Zone de saisie pour Customer Service
        input_cs_chat_frame = ttk.Frame(cs_chat_frame)
        input_cs_chat_frame.pack(fill="x")
        
        self.cs_chat_entry = tk.Entry(input_cs_chat_frame, font=("Arial", 10))
        self.cs_chat_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.cs_chat_entry.bind("<Return>", self.send_cs_chat_message)
        
        send_cs_btn = ttk.Button(input_cs_chat_frame, text="🎧 Demander personnalisation", 
                                command=self.send_cs_chat_message)
        send_cs_btn.pack(side="right")
        
        # Boutons d'actions rapides Customer Service
        cs_quick_actions_frame = ttk.Frame(cs_chat_frame)
        cs_quick_actions_frame.pack(fill="x", pady=(10, 0))
        
        ttk.Label(cs_quick_actions_frame, text="Actions rapides :", 
                 font=("Arial", 9, "bold")).pack(side="left", padx=(0, 10))
        
        cs_quick_buttons = [
            ("🔧 Ajuster résultat", lambda: self.cs_quick_action("adjust")),
            ("📝 Modifier style", lambda: self.cs_quick_action("style")),
            ("🎯 Personnaliser", lambda: self.cs_quick_action("customize")),
            ("🔄 Refaire", lambda: self.cs_quick_action("redo")),
            ("💾 Sauvegarder préférences", lambda: self.cs_quick_action("save_prefs"))
        ]
        
        for button_text, button_command in cs_quick_buttons:
            btn = ttk.Button(cs_quick_actions_frame, text=button_text, command=button_command)
            btn.pack(side="left", padx=2)
        
        # Message d'accueil Customer Service
        self.add_cs_chat_message("🎧 Agent SAV", 
                                "Bienvenue au service personnalisation LazyRepo ! 👋\n\n"
                                "Je suis votre agent SAV dédié aux ajustements post-génération.\n\n"
                                "🎯 Je peux vous aider à :\n"
                                "• Modifier le style des fichiers générés\n"
                                "• Ajuster les paramètres selon vos préférences\n"
                                "• Personnaliser les templates utilisés\n"
                                "• Corriger des éléments spécifiques\n"
                                "• Sauvegarder vos préférences pour les prochaines analyses\n\n"
                                "💡 Décrivez-moi ce que vous souhaitez modifier ou utilisez les actions rapides !")
    
    def add_cs_chat_message(self, sender, message):
        """Ajoute un message au chat Customer Service"""
        self.cs_chat_display.config(state="normal")
        
        # Ajouter timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        # Ajouter le message avec styles différents
        if sender == "🎧 Agent SAV":
            self.cs_chat_display.insert(tk.END, f"[{timestamp}] {sender}:\n", "cs_sender")
            self.cs_chat_display.insert(tk.END, f"{message}\n\n", "cs_message")
        else:
            self.cs_chat_display.insert(tk.END, f"[{timestamp}] {sender}:\n", "cs_user_sender")
            self.cs_chat_display.insert(tk.END, f"{message}\n\n", "cs_user_message")
        
        # Configurer les tags pour le style Customer Service
        self.cs_chat_display.tag_configure("cs_sender", foreground="#7c3aed", font=("Arial", 9, "bold"))
        self.cs_chat_display.tag_configure("cs_message", foreground="#1f2937")
        self.cs_chat_display.tag_configure("cs_user_sender", foreground="#059669", font=("Arial", 9, "bold"))
        self.cs_chat_display.tag_configure("cs_user_message", foreground="#374151")
        
        self.cs_chat_display.config(state="disabled")
        self.cs_chat_display.see(tk.END)
    
    def send_cs_chat_message(self, event=None):
        """Envoie un message dans le chat Customer Service"""
        message = self.cs_chat_entry.get().strip()
        if not message:
            return
        
        # Ajouter le message de l'utilisateur
        self.add_cs_chat_message("👤 Vous", message)
        self.cs_chat_entry.delete(0, tk.END)
        
        # Générer la réponse du SAV avec délai
        self.root.after(700, lambda: self.generate_cs_ai_response(message))
    
    def generate_cs_ai_response(self, user_message):
        """Génère une réponse de l'agent Customer Service SAV"""
        user_message_lower = user_message.lower()
        
        # Vérifier le contexte des modifications
        has_modifications = hasattr(self, 'generated_files') and self.generated_files
        has_analysis = hasattr(self, 'analysis_progress') and self.analysis_progress > 0
        
        # Réponses spécialisées Customer Service/SAV
        if any(word in user_message_lower for word in ["aide", "help", "que peux-tu faire"]):
            response = ("🎧 Service Client LazyRepo à votre disposition !\n\n"
                       "Je suis spécialisé dans la personnalisation post-génération :\n\n"
                       "🔧 AJUSTEMENTS TECHNIQUES :\n"
                       "• Modifier les styles de code générés\n"
                       "• Changer les formats de documentation\n"
                       "• Ajuster les conventions de nommage\n\n"
                       "🎨 PERSONNALISATION :\n"
                       "• Adapter les templates à vos besoins\n"
                       "• Modifier les commentaires automatiques\n"
                       "• Personnaliser les structures de fichiers\n\n"
                       "💾 PRÉFÉRENCES :\n"
                       "• Sauvegarder vos choix pour les prochaines fois\n"
                       "• Créer des profils personnalisés\n"
                       "• Exporter vos configurations\n\n"
                       "Que souhaitez-vous personnaliser aujourd'hui ?")
        
        elif any(word in user_message_lower for word in ["style", "format", "présentation"]):
            if not has_modifications:
                response = ("🎨 Excellent ! Parlons de personnalisation de style.\n\n"
                           "Pour personnaliser le style, je dois d'abord analyser ce qui a été généré.\n\n"
                           "📋 ÉTAPES RECOMMANDÉES :\n"
                           "1. Lancez une analyse depuis l'onglet Configuration\n"
                           "2. Consultez les résultats générés\n"
                           "3. Revenez ici pour personnaliser le style\n\n"
                           "🎯 STYLES DISPONIBLES :\n"
                           "• Style corporate (formel)\n"
                           "• Style moderne (épuré)\n"
                           "• Style développeur (technique)\n"
                           "• Style startup (innovant)\n\n"
                           "Quel style préférez-vous ?")
            else:
                response = ("🎨 Parfait ! Je vois que vous avez des fichiers générés.\n\n"
                           "📊 ANALYSE DU STYLE ACTUEL :\n"
                           "• Documentation : Style technique détaillé\n"
                           "• Commentaires : Format standard\n"
                           "• Structure : Organisation classique\n\n"
                           "🔄 MODIFICATIONS POSSIBLES :\n"
                           "• Plus concis → Réduire la verbosité\n"
                           "• Plus formel → Ajouter du contexte business\n"
                           "• Plus moderne → Utiliser des emojis et sections\n"
                           "• Plus technique → Ajouter des détails d'implémentation\n\n"
                           "Quel ajustement souhaitez-vous appliquer ?")
        
        elif any(word in user_message_lower for word in ["modifier", "changer", "ajuster"]):
            response = ("🔧 Je comprends que vous voulez modifier quelque chose !\n\n"
                       "💡 ÉLÉMENTS MODIFIABLES :\n\n"
                       "📝 CONTENU :\n"
                       "• Titre et descriptions des fichiers\n"
                       "• Commentaires et documentation\n"
                       "• Structure des dossiers\n\n"
                       "🎨 APPARENCE :\n"
                       "• Format des fichiers (Markdown, HTML, etc.)\n"
                       "• Style des commentaires de code\n"
                       "• Organisation des sections\n\n"
                       "⚙️ CONFIGURATION :\n"
                       "• Langue des commentaires (FR/EN)\n"
                       "• Niveau de détail (basique/avancé)\n"
                       "• Templates personnalisés\n\n"
                       "Pouvez-vous me dire précisément ce que vous souhaitez modifier ?")
        
        elif any(word in user_message_lower for word in ["préférence", "sauvegarder", "profil"]):
            response = ("💾 Excellente idée ! La sauvegarde de préférences personnalisées.\n\n"
                       "🎯 PROFILS DISPONIBLES :\n\n"
                       "👔 PROFIL ENTREPRISE :\n"
                       "• Documentation formelle\n"
                       "• Commentaires détaillés\n"
                       "• Structure hiérarchique\n\n"
                       "🚀 PROFIL STARTUP :\n"
                       "• Style moderne et agile\n"
                       "• Documentation concise\n"
                       "• Focus sur l'innovation\n\n"
                       "💻 PROFIL DÉVELOPPEUR :\n"
                       "• Commentaires techniques\n"
                       "• Documentation code-first\n"
                       "• Exemples pratiques\n\n"
                       "📋 PROFIL PERSONNALISÉ :\n"
                       "• Vos propres préférences\n"
                       "• Templates sur mesure\n"
                       "• Configuration sauvegardée\n\n"
                       "Quel profil vous intéresse ?")
        
        elif any(word in user_message_lower for word in ["problème", "erreur", "bug", "ne marche pas"]):
            response = ("🔧 Service technique LazyRepo - Je vais vous aider !\n\n"
                       "🚨 DIAGNOSTIC RAPIDE :\n"
                       "Décrivez-moi le problème rencontré :\n\n"
                       "❓ QUESTIONS DE DIAGNOSTIC :\n"
                       "• À quelle étape cela se produit-il ?\n"
                       "• Quel était le résultat attendu ?\n"
                       "• Y a-t-il un message d'erreur ?\n\n"
                       "🛠️ SOLUTIONS COURANTES :\n"
                       "• Relancer l'analyse avec d'autres paramètres\n"
                       "• Vérifier la configuration des équipes\n"
                       "• Réinitialiser et recommencer\n\n"
                       "🎧 SUPPORT AVANCÉ :\n"
                       "• Analyse des logs détaillée\n"
                       "• Configuration personnalisée\n"
                       "• Assistance en temps réel\n\n"
                       "Détaillez-moi votre problème, je vais le résoudre !")
        
        elif any(word in user_message_lower for word in ["recommandation", "conseil", "suggestion"]):
            if has_analysis:
                response = ("💡 Recommandations personnalisées basées sur votre projet :\n\n"
                           "📊 ANALYSE DE VOTRE PROJET :\n"
                           "• Complexité détectée : Moyenne à élevée\n"
                           "• Langages principaux identifiés\n"
                           "• Style actuel : Technique standard\n\n"
                           "🎯 MES RECOMMANDATIONS :\n\n"
                           "1. 📚 DOCUMENTATION :\n"
                           "   → Ajouter plus d'exemples pratiques\n"
                           "   → Créer un guide de démarrage rapide\n\n"
                           "2. 🎨 STYLE :\n"
                           "   → Adopter un ton plus accessible\n"
                           "   → Ajouter des visuels (diagrammes)\n\n"
                           "3. 🔧 STRUCTURE :\n"
                           "   → Réorganiser par niveau de difficulté\n"
                           "   → Ajouter une section FAQ\n\n"
                           "Quelle recommandation vous intéresse le plus ?")
            else:
                response = ("💡 Je serais ravi de vous donner des recommandations !\n\n"
                           "Pour des conseils personnalisés, lancez d'abord une analyse.\n\n"
                           "🎯 RECOMMANDATIONS GÉNÉRALES :\n\n"
                           "🚀 POUR DÉBUTER :\n"
                           "• Commencez par l'équipe Documentation\n"
                           "• Ajoutez votre langage principal\n"
                           "• Testez avec un petit projet\n\n"
                           "📈 POUR OPTIMISER :\n"
                           "• Activez plusieurs équipes complémentaires\n"
                           "• Sauvegardez vos préférences\n"
                           "• Utilisez les actions rapides\n\n"
                           "🎨 POUR PERSONNALISER :\n"
                           "• Définissez votre style préféré\n"
                           "• Créez des templates personnalisés\n"
                           "• Configurez vos profils\n\n"
                           "Que souhaitez-vous optimiser en priorité ?")
        
        else:
            # Réponse contextuelle par défaut
            context_responses = [
                ("🎧 Je suis là pour vous aider avec la personnalisation !\n\n"
                 "Pouvez-vous être plus spécifique sur ce que vous souhaitez ajuster ?\n\n"
                 "Par exemple :\n"
                 "• 'Modifier le style de documentation'\n"
                 "• 'Changer le format des commentaires'\n"
                 "• 'Personnaliser les templates'\n"
                 "• 'Sauvegarder mes préférences'\n\n"
                 "Je suis spécialisé dans l'ajustement fin de vos résultats ! 🔧"),
                
                ("🤔 Intéressant ! Pour mieux vous aider, pourriez-vous préciser :\n\n"
                 "🎯 QUE VOULEZ-VOUS PERSONNALISER ?\n"
                 "• Le contenu généré ?\n"
                 "• Le style d'écriture ?\n"
                 "• La structure des fichiers ?\n"
                 "• Les paramètres de génération ?\n\n"
                 "Plus vous serez précis, mieux je pourrai vous assister ! 🎧"),
                
                ("💡 Service Client LazyRepo - Je vous écoute !\n\n"
                 "Votre demande m'intéresse. Pour vous proposer la meilleure solution :\n\n"
                 "📋 DÉCRIVEZ-MOI :\n"
                 "• Ce qui ne vous convient pas actuellement\n"
                 "• Le résultat que vous souhaitez obtenir\n"
                 "• Vos préférences de style/format\n\n"
                 "🚀 ENSEMBLE, nous trouverons la personnalisation parfaite ! 🎯")
            ]
            
            response = random.choice(context_responses)
        
        self.add_cs_chat_message("🎧 Agent SAV", response)
    
    def cs_quick_action(self, action_type):
        """Exécute une action rapide Customer Service"""
        action_messages = {
            "adjust": {
                "title": "🔧 Ajustement des Résultats",
                "message": ("Ajustement des résultats en cours...\n\n"
                           "📊 ÉLÉMENTS AJUSTÉS :\n"
                           "• Style de documentation : Plus concis\n"
                           "• Format des commentaires : Modernisé\n"
                           "• Structure des fichiers : Optimisée\n\n"
                           "✅ Ajustements appliqués avec succès !\n"
                           "Consultez vos fichiers pour voir les modifications.")
            },
            "style": {
                "title": "📝 Modification du Style",
                "message": ("Personnalisation du style en cours...\n\n"
                           "🎨 CHANGEMENTS APPLIQUÉS :\n"
                           "• Tone : Plus professionnel\n"
                           "• Format : Style moderne avec emojis\n"
                           "• Organisation : Sections mieux définies\n"
                           "• Lisibilité : Améliorée\n\n"
                           "✨ Votre style personnalisé est maintenant actif !")
            },
            "customize": {
                "title": "🎯 Personnalisation Avancée",
                "message": ("Lancement de la personnalisation avancée...\n\n"
                           "⚙️ OPTIONS DISPONIBLES :\n"
                           "• Templates personnalisés : Activés\n"
                           "• Préférences utilisateur : Chargées\n"
                           "• Configuration sur mesure : Appliquée\n"
                           "• Profil adaptatif : Configuré\n\n"
                           "🚀 Votre environnement est maintenant entièrement personnalisé !")
            },
            "redo": {
                "title": "🔄 Régénération Personnalisée",
                "message": ("Régénération avec vos préférences...\n\n"
                           "🔄 PROCESSUS EN COURS :\n"
                           "• Application de vos préférences sauvegardées\n"
                           "• Régénération avec le style personnalisé\n"
                           "• Intégration des ajustements précédents\n"
                           "• Optimisation selon votre profil\n\n"
                           "⏱️ Estimation : 30 secondes...\n"
                           "✅ Régénération terminée avec vos personnalisations !")
            },
            "save_prefs": {
                "title": "💾 Sauvegarde des Préférences",
                "message": ("Sauvegarde de vos préférences personnalisées...\n\n"
                           "💾 ÉLÉMENTS SAUVEGARDÉS :\n"
                           "• Style de documentation préféré\n"
                           "• Format des commentaires personnalisé\n"
                           "• Organisation des fichiers optimisée\n"
                           "• Profil utilisateur complet\n"
                           "• Templates sur mesure\n\n"
                           "✅ Profil personnalisé sauvegardé !\n"
                           "Vos préférences seront appliquées automatiquement lors des prochaines analyses.")
            }
        }
        
        action_info = action_messages.get(action_type, {
            "title": "Action Customer Service",
            "message": "Action exécutée avec succès !"
        })
        
        # Afficher le message dans le chat
        self.add_cs_chat_message("🎧 Agent SAV", 
                                f"{action_info['title']}\n\n{action_info['message']}")
        
        # Notification globale
        self.show_notification(
            f"✅ {action_info['title']} - Action terminée avec succès !",
            duration=4000
        )
        
        # Ajouter à l'historique des modifications
        timestamp = datetime.datetime.now().strftime("%H:%M")
        modification_entry = f"[{timestamp}] Customer Service - {action_info['title']}"
        
        if hasattr(self, 'modifications_listbox'):
            if self.modifications_listbox.size() == 1 and "Aucune modification" in self.modifications_listbox.get(0):
                self.modifications_listbox.delete(0)
                self.modifications_listbox.config(foreground="black")
            
            self.modifications_listbox.insert(0, modification_entry)
            
            # Limiter l'historique à 20 entrées
            if self.modifications_listbox.size() > 20:
                self.modifications_listbox.delete(20, tk.END)
    
    def create_modifications_history_section(self):
        """Crée la section historique des modifications"""
        history_frame = ttk.LabelFrame(self.improvement_scrollable_frame, 
                                      text="📋 Historique des Modifications", padding=15)
        history_frame.pack(fill="x", padx=20, pady=(10, 20))
        
        # En-tête de l'historique
        history_header_frame = ttk.Frame(history_frame)
        history_header_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(history_header_frame, text="Dernières modifications suggérées:", 
                 font=("Arial", 10, "bold")).pack(side="left")
        ttk.Button(history_header_frame, text="🗑️ Vider l'historique", 
                  command=self.clear_modifications_history).pack(side="right")
        
        # Liste des modifications
        modifications_list_frame = ttk.Frame(history_frame)
        modifications_list_frame.pack(fill="both", expand=True)
        
        # Scrollbar pour l'historique
        history_scrollbar = ttk.Scrollbar(modifications_list_frame)
        history_scrollbar.pack(side="right", fill="y")
        
        # Listbox pour l'historique
        self.modifications_listbox = tk.Listbox(modifications_list_frame, height=6,
                                               yscrollcommand=history_scrollbar.set,
                                               font=("Arial", 9))
        self.modifications_listbox.pack(side="left", fill="both", expand=True)
        history_scrollbar.config(command=self.modifications_listbox.yview)
        
        self.modifications_listbox.bind("<Double-Button-1>", self.view_modification_details)
        
        # Placeholder initial
        self.modifications_listbox.insert(0, "📝 Aucune modification effectuée pour le moment")
        self.modifications_listbox.config(foreground="gray")
    
    def setup_results_tab(self):
        """Configure l'onglet Résultats avec simulation et métriques (PROMPT 3)"""
        # Canvas scrollable pour les résultats
        self.results_canvas = tk.Canvas(self.results_frame, highlightthickness=0, bg="#f0f0f0")
        self.results_scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", 
                                              command=self.results_canvas.yview)
        self.results_scrollable_frame = ttk.Frame(self.results_canvas)
        
        # Configuration du scrolling
        self.results_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox("all"))
        )
        
        # Créer la fenêtre dans le canvas
        self.results_canvas_window = self.results_canvas.create_window((0, 0), 
                                                                      window=self.results_scrollable_frame, 
                                                                      anchor="nw")
        self.results_canvas.configure(yscrollcommand=self.results_scrollbar.set)
        
        # Centrage automatique
        self.results_canvas.bind("<Configure>", self.center_results_content)
        
        # Pack canvas et scrollbar
        self.results_canvas.pack(side="left", fill="both", expand=True)
        self.results_scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.results_canvas.bind("<MouseWheel>", self.on_results_mousewheel)
        
        # Contenu de l'onglet résultats
        self.create_analysis_header()
        self.create_progress_section()
        self.create_metrics_section()
        self.create_results_navigation()
        self.create_generated_files_section()
        self.create_results_actions()
    
    def center_results_content(self, event):
        """Centre le contenu des résultats dans le canvas"""
        canvas_width = event.width
        frame_width = self.results_scrollable_frame.winfo_reqwidth()
        
        if frame_width < canvas_width:
            x_position = (canvas_width - frame_width) // 2
        else:
            x_position = 0
        
        self.results_canvas.coords(self.results_canvas_window, x_position, 0)
    
    def on_results_mousewheel(self, event):
        """Gestion du scroll avec la molette pour les résultats"""
        self.results_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def create_analysis_header(self):
        """Crée l'en-tête de l'analyse"""
        header_frame = ttk.Frame(self.results_scrollable_frame)
        header_frame.pack(fill="x", padx=20, pady=15)
        
        ttk.Label(header_frame, text="📊 Résultats de l'Analyse LazyRepo", 
                 font=("Arial", 18, "bold")).pack(anchor="center")
        
        # Informations du projet
        self.project_info_frame = ttk.Frame(header_frame)
        self.project_info_frame.pack(pady=10)
        
        self.project_info_label = ttk.Label(self.project_info_frame, 
                                           text="Projet non analysé", 
                                           font=("Arial", 11), foreground="gray")
        self.project_info_label.pack()
    
    def create_progress_section(self):
        """Crée la section de progression de l'analyse"""
        progress_frame = ttk.LabelFrame(self.results_scrollable_frame, 
                                       text="🔄 Progression de l'analyse", padding=15)
        progress_frame.pack(fill="x", padx=20, pady=10)
        
        # Barre de progression
        progress_container = ttk.Frame(progress_frame)
        progress_container.pack(fill="x", pady=(0, 10))
        
        ttk.Label(progress_container, text="Progression globale:", 
                 font=("Arial", 10, "bold")).pack(anchor="w")
        
        self.progress_bar = ttk.Progressbar(progress_container, mode='determinate', length=400)
        self.progress_bar.pack(fill="x", pady=5)
        
        self.progress_label = ttk.Label(progress_container, text="0% - En attente de démarrage", 
                                       foreground="gray")
        self.progress_label.pack(anchor="w")
        
        # Étapes de l'analyse
        steps_frame = ttk.Frame(progress_frame)
        steps_frame.pack(fill="x", pady=10)
        
        ttk.Label(steps_frame, text="Étapes d'analyse:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        self.steps_frame = ttk.Frame(steps_frame)
        self.steps_frame.pack(fill="x", pady=5)
        
        # Créer les étapes
        self.analysis_steps = [
            "🔍 Scan des fichiers du projet",
            "📋 Analyse des langages détectés", 
            "🤖 Configuration des agents IA",
            "📚 Génération de la documentation",
            "🔧 Analyse du code et améliorations",
            "🔒 Scan de sécurité",
            "📱 Création du contenu social",
            "✅ Finalisation et rapport"
        ]
        
        self.step_labels = []
        for i, step in enumerate(self.analysis_steps):
            step_label = ttk.Label(self.steps_frame, text=f"⏳ {step}", foreground="gray")
            step_label.pack(anchor="w", pady=2)
            self.step_labels.append(step_label)
    
    def create_metrics_section(self):
        """Crée la section des métriques et statistiques"""
        metrics_frame = ttk.LabelFrame(self.results_scrollable_frame, 
                                      text="📈 Métriques de l'analyse", padding=15)
        metrics_frame.pack(fill="x", padx=20, pady=10)
        
        # Grille de métriques 2x3
        metrics_grid = ttk.Frame(metrics_frame)
        metrics_grid.pack(fill="x")
        
        # Métriques de base
        self.metrics_widgets = {}
        metrics_data = [
            ("📁 Fichiers analysés", "0", 0, 0),
            ("💻 Lignes de code", "0", 0, 1),
            ("🌐 Langages détectés", "0", 1, 0),
            ("🤖 Agents actifs", "0", 1, 1),
            ("📄 Fichiers générés", "0", 2, 0),
            ("⏱️ Temps d'analyse", "0s", 2, 1)
        ]
        
        for label, value, row, col in metrics_data:
            metric_frame = ttk.Frame(metrics_grid)
            metric_frame.grid(row=row, column=col, padx=15, pady=8, sticky="w")
            
            ttk.Label(metric_frame, text=label, font=("Arial", 9)).pack(anchor="w")
            value_label = ttk.Label(metric_frame, text=value, font=("Arial", 12, "bold"), 
                                   foreground="#2563eb")
            value_label.pack(anchor="w")
            
            self.metrics_widgets[label] = value_label
        
        # Configurer les colonnes
        metrics_grid.columnconfigure(0, weight=1)
        metrics_grid.columnconfigure(1, weight=1)
    
    def create_results_navigation(self):
        """Crée la navigation entre les résultats des équipes"""
        nav_frame = ttk.LabelFrame(self.results_scrollable_frame, 
                                  text="🗂️ Navigation des résultats", padding=15)
        nav_frame.pack(fill="x", padx=20, pady=10)
        
        # Boutons de navigation par équipe
        nav_buttons_frame = ttk.Frame(nav_frame)
        nav_buttons_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(nav_buttons_frame, text="Voir les résultats par équipe:", 
                 font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 8))
        
        buttons_container = ttk.Frame(nav_buttons_frame)
        buttons_container.pack(fill="x")
        
        self.nav_buttons = {}
        nav_categories = [
            ("📚", "Documentation", "#3b82f6"),
            ("🔧", "Code Improvement", "#10b981"),
            ("🔒", "Security", "#ef4444"),
            ("📱", "Social Content", "#8b5cf6")
        ]
        
        for icon, category, color in nav_categories:
            btn = ttk.Button(buttons_container, text=f"{icon} {category}",
                           command=lambda cat=category: self.show_category_results(cat))
            btn.pack(side="left", padx=(0, 10))
            self.nav_buttons[category] = btn
        
        # Zone d'affichage des résultats de la catégorie sélectionnée
        self.category_results_frame = ttk.Frame(nav_frame)
        self.category_results_frame.pack(fill="both", expand=True, pady=10)
        
        # Placeholder initial
        self.category_placeholder = ttk.Label(self.category_results_frame, 
                                             text="Sélectionnez une équipe pour voir ses résultats",
                                             foreground="gray", font=("Arial", 10))
        self.category_placeholder.pack(pady=20)
    
    def create_generated_files_section(self):
        """Crée la section des fichiers générés"""
        files_frame = ttk.LabelFrame(self.results_scrollable_frame, 
                                    text="📄 Fichiers générés", padding=15)
        files_frame.pack(fill="x", padx=20, pady=10)
        
        # Liste des fichiers avec aperçu
        files_container = ttk.Frame(files_frame)
        files_container.pack(fill="both", expand=True)
        
        # En-tête
        header_files = ttk.Frame(files_container)
        header_files.pack(fill="x", pady=(0, 10))
        
        ttk.Label(header_files, text="Fichiers créés et modifiés:", 
                 font=("Arial", 10, "bold")).pack(anchor="w")
        ttk.Label(header_files, text="Cliquez sur un fichier pour prévisualiser son contenu",
                 foreground="gray", font=("Arial", 9)).pack(anchor="w")
        
        # Zone scrollable pour la liste des fichiers
        files_scroll_frame = ttk.Frame(files_container)
        files_scroll_frame.pack(fill="both", expand=True)
        
        # Listbox avec scrollbar pour les fichiers
        files_list_frame = ttk.Frame(files_scroll_frame)
        files_list_frame.pack(fill="both", expand=True)
        
        files_scrollbar = ttk.Scrollbar(files_list_frame)
        files_scrollbar.pack(side="right", fill="y")
        
        self.files_listbox = tk.Listbox(files_list_frame, height=6, 
                                       yscrollcommand=files_scrollbar.set,
                                       font=("Consolas", 9))
        self.files_listbox.pack(side="left", fill="both", expand=True)
        files_scrollbar.config(command=self.files_listbox.yview)
        
        self.files_listbox.bind("<Double-Button-1>", self.preview_generated_file)
        
        # Zone de prévisualisation
        preview_frame = ttk.Frame(files_container)
        preview_frame.pack(fill="both", expand=True, pady=(10, 0))
        
        ttk.Label(preview_frame, text="Aperçu du fichier sélectionné:", 
                 font=("Arial", 10, "bold")).pack(anchor="w")
        
        preview_scroll = ttk.Scrollbar(preview_frame)
        preview_scroll.pack(side="right", fill="y")
        
        self.file_preview = tk.Text(preview_frame, height=8, state="disabled",
                                   yscrollcommand=preview_scroll.set,
                                   font=("Consolas", 8), bg="#f8f9fa")
        self.file_preview.pack(side="left", fill="both", expand=True)
        preview_scroll.config(command=self.file_preview.yview)
    
    def create_results_actions(self):
        """Crée les boutons d'action pour les résultats"""
        actions_frame = ttk.Frame(self.results_scrollable_frame)
        actions_frame.pack(fill="x", padx=20, pady=20)
        
        # Boutons principaux
        ttk.Button(actions_frame, text="📥 Télécharger tous les fichiers",
                  command=self.demo_download_files).pack(side="left", padx=(0, 10))
        
        ttk.Button(actions_frame, text="🔄 Relancer l'analyse",
                  command=self.demo_restart_analysis).pack(side="left", padx=(0, 10))
        
        ttk.Button(actions_frame, text="📊 Rapport complet",
                  command=self.demo_show_full_report).pack(side="left", padx=(0, 10))
        
        # Bouton pour passer à l'amélioration
        ttk.Button(actions_frame, text="➡️ Aller à l'amélioration",
                  command=lambda: self.notebook.select(2)).pack(side="right")
    
    def demo_browse_folder(self):
        """Démonstration: Sélection de dossier"""
        folder = filedialog.askdirectory(title="Sélectionner le dossier du projet (démonstration)")
        if folder:
            self.project_path.set(folder)
            self.path_label.configure(foreground="black")
            messagebox.showinfo("Démonstration", 
                               f"🎭 Mode démonstration\n\n"
                               f"Dossier sélectionné: {os.path.basename(folder)}\n\n"
                               f"Dans la vraie application, LazyRepo analyserait ce dossier.")
    
    def demo_detect_languages(self):
        """Démonstration: Détection des langages"""
        if self.project_path.get() == "Aucun dossier sélectionné":
            # Sélection aléatoire pour la démo
            num_langs = random.randint(2, 6)
            selected_langs = random.sample(self.all_languages[:-1], num_langs)
            
            # Reset et sélection
            for var in self.languages_vars.values():
                var.set(False)
            for lang in selected_langs:
                self.languages_vars[lang].set(True)
            
            messagebox.showinfo("Démonstration - Mode aléatoire", 
                               f"🎭 Mode démonstration\n\n"
                               f"Langages détectés (simulation): {', '.join(selected_langs)}\n\n"
                               f"Sélectionnez un dossier pour une vraie analyse.")
        else:
            # Simulation avec dossier
            demo_langs = ["Python", "JavaScript", "HTML", "CSS"]
            for var in self.languages_vars.values():
                var.set(False)
            for lang in demo_langs:
                if lang in self.languages_vars:
                    self.languages_vars[lang].set(True)
            
            messagebox.showinfo("Démonstration", 
                               f"🎭 Mode démonstration\n\n"
                               f"Langages détectés: {', '.join(demo_langs)}\n\n"
                               f"Dans la vraie application, LazyRepo analyserait le code source.")
    
    def demo_start_analysis(self):
        """Démonstration: Lancement de l'analyse"""
        selected_crews = self.options_manager.get_selected_crews()
        selected_langs = [lang for lang, var in self.languages_vars.items() if var.get()]
        
        # Vérifier les sélections
        has_crews = any(any(agents.values()) for agents in selected_crews.values())
        
        if not has_crews:
            response = messagebox.askyesno("Mode démonstration", 
                                         "Aucune équipe n'est activée.\n\n"
                                         "Voulez-vous activer automatiquement des équipes "
                                         "pour la démonstration ?")
            if response:
                self.demo_random_crew_selection()
        
        if not selected_langs:
            response = messagebox.askyesno("Mode démonstration", 
                                         "Aucun langage n'est sélectionné.\n\n"
                                         "Voulez-vous sélectionner automatiquement des langages "
                                         "pour la démonstration ?")
            if response:
                self.demo_detect_languages()
        
        # Message de lancement
        messagebox.showinfo("Analyse LazyRepo", 
                           f"🎭 Mode démonstration\n\n"
                           f"Projet: {self.project_name.get()}\n"
                           f"Équipes: {len([c for c in selected_crews.keys()])}\n"
                           f"Langages: {len(selected_langs)}\n\n"
                           f"Dans la vraie application, l'analyse démarrerait maintenant !\n"
                           f"L'onglet Résultats s'activerait automatiquement.")
        
        # Démarrer la simulation d'analyse (PROMPT 3)
        self.start_demo_analysis()
    
    def demo_show_config(self):
        """Démonstration: Affichage de la configuration"""
        selected_crews = self.options_manager.get_selected_crews()
        selected_langs = [lang for lang, var in self.languages_vars.items() if var.get()]
        
        config_text = [f"Configuration LazyRepo - {self.project_name.get()}"]
        config_text.append(f"Dossier: {self.project_path.get()}")
        config_text.append(f"Langages: {', '.join(selected_langs) if selected_langs else 'Aucun'}")
        config_text.append("")
        config_text.append("Équipes activées:")
        
        for crew_name, agents in selected_crews.items():
            active_agents = [name for name, active in agents.items() if active]
            if active_agents:
                config_text.append(f"\n{crew_name}:")
                for agent in active_agents:
                    config_text.append(f"  • {agent}")
            else:
                config_text.append(f"\n{crew_name}: Aucun agent activé")
        
        messagebox.showinfo("Configuration LazyRepo", "\n".join(config_text))
    
    def demo_random_crew_selection(self):
        """Sélection aléatoire d'équipes pour la démo"""
        for crew_name, crew_data in self.options_manager.categories.items():
            # Sélectionner aléatoirement 1-3 agents
            num_agents = random.randint(1, 3)
            agents_list = list(crew_data['agents'].keys())
            selected_agents = random.sample(agents_list, min(num_agents, len(agents_list)))
            
            # Reset puis activation
            for var in crew_data['agents'].values():
                var.set(False)
            for agent in selected_agents:
                crew_data['agents'][agent].set(True)
    
    # ============ NOUVELLES FONCTIONNALITÉS CHAT IA (PROMPT 2) ============
    
    def add_ai_message(self, sender, message):
        """Ajoute un message de l'IA au chat avec timestamps et couleurs"""
        self.chat_display.config(state="normal")
        
        # Ajouter timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        # Ajouter le message
        if sender == "🤖 Assistant IA":
            self.chat_display.insert(tk.END, f"[{timestamp}] {sender}:\n", "ai_sender")
            self.chat_display.insert(tk.END, f"{message}\n\n", "ai_message")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] {sender}:\n", "user_sender")
            self.chat_display.insert(tk.END, f"{message}\n\n", "user_message")
        
        # Configurer les tags pour le style
        self.chat_display.tag_configure("ai_sender", foreground="#2563eb", font=("Arial", 9, "bold"))
        self.chat_display.tag_configure("ai_message", foreground="#1f2937")
        self.chat_display.tag_configure("user_sender", foreground="#059669", font=("Arial", 9, "bold"))
        self.chat_display.tag_configure("user_message", foreground="#374151")
        
        self.chat_display.config(state="disabled")
        self.chat_display.see(tk.END)  # Scroll vers le bas
    
    def send_chat_message(self, event=None):
        """Envoie un message dans le chat"""
        message = self.chat_entry.get().strip()
        if not message:
            return
        
        # Ajouter le message de l'utilisateur
        self.add_ai_message("👤 Vous", message)
        self.chat_entry.delete(0, tk.END)
        
        # Générer la réponse de l'IA avec délai
        self.root.after(500, lambda: self.generate_ai_response(message))
    
    def notify_ai_selection_change(self, crew_name, has_selection):
        """Notifie l'IA des changements de sélection avec cooldown anti-spam"""
        if self.ai_notification_cooldown:
            return
        
        # Activer le cooldown pour éviter le spam
        self.ai_notification_cooldown = True
        self.root.after(3000, lambda: setattr(self, 'ai_notification_cooldown', False))
        
        # Messages de réaction de l'IA
        if has_selection:
            reactions = [
                f"👍 Excellent ! Vous avez activé {crew_name}. Cette équipe va faire du super travail !",
                f"🎯 Parfait ! {crew_name} est un excellent choix pour votre projet.",
                f"✨ Super sélection avec {crew_name} ! Voulez-vous que je vous pose des questions spécifiques ?"
            ]
        else:
            reactions = [
                f"🤔 Vous avez désactivé {crew_name}. Si vous changez d'avis, elle reste disponible !",
                f"👌 {crew_name} désactivée. Concentrons-nous sur vos autres équipes alors !"
            ]
        
        # Ajouter le message avec un délai pour que ce soit naturel
        self.root.after(1000, lambda: self.add_ai_message("🤖 Assistant IA", random.choice(reactions)))
    
    def generate_ai_response(self, user_message):
        """Génère une réponse intelligente de l'IA basée sur le contexte"""
        user_message_lower = user_message.lower()
        
        # Obtenir le contexte actuel
        selected_crews = self.get_selected_crews_summary()
        selected_languages = self.get_selected_languages()
        project_name = self.project_name.get()
        has_project_folder = self.project_path.get() != "Aucun dossier sélectionné"
        
        # Commandes spéciales
        if "aide" in user_message_lower or "help" in user_message_lower:
            response = ("🆘 Voici ce que je peux faire :\n\n"
                       "• 📊 Analyser vos sélections d'équipes\n"
                       "• 🔍 Suggérer des optimisations\n"
                       "• ❓ Poser des questions personnalisées\n"
                       "• 💡 Donner des conseils selon votre projet\n\n"
                       "Tapez 'suggestions' pour des recommandations !")
        
        elif "suggestion" in user_message_lower or "conseil" in user_message_lower:
            response = self.generate_suggestions(selected_crews, selected_languages, has_project_folder)
        
        elif "question" in user_message_lower:
            response = self.generate_contextual_questions(selected_crews, selected_languages)
        
        # Réponses contextuelles basées sur les sélections
        elif selected_crews and not self.ai_questions_asked:
            response = self.generate_contextual_questions(selected_crews, selected_languages)
        
        # Réponses génériques intelligentes
        elif any(word in user_message_lower for word in ["merci", "ok", "oui", "non"]):
            responses = [
                "Parfait ! Y a-t-il autre chose que vous aimeriez personnaliser ?",
                "Excellent ! Souhaitez-vous que je vous pose des questions plus spécifiques ?",
                "Super ! Tapez 'suggestions' pour des recommandations personnalisées."
            ]
            response = random.choice(responses)
        
        elif any(word in user_message_lower for word in ["python", "javascript", "java", "code"]):
            if selected_languages:
                lang_text = ", ".join(selected_languages[:3])
                response = (f"Excellent choix avec {lang_text} ! 🐍\n\n"
                           f"Pour ces langages, je recommande particulièrement :\n"
                           f"• 📚 Documentation automatique des APIs\n"
                           f"• 🔒 Scan de sécurité approfondi\n"
                           f"• 🔧 Optimisation des performances\n\n"
                           f"Avez-vous des frameworks spécifiques en tête ?")
            else:
                response = ("Les langages que vous mentionnez sont excellents ! 💻\n\n"
                           "N'hésitez pas à les sélectionner dans la section ci-dessus, "
                           "je pourrai alors vous donner des conseils plus précis !")
        
        else:
            # Réponses par défaut intelligentes
            default_responses = [
                f"Intéressant ! Pour votre projet '{project_name}', cela pourrait être très utile. 🤔",
                "Je vois ! Cela m'aide à mieux comprendre vos besoins. Continuez à me parler de votre projet ! 💡",
                "Merci pour cette information ! Cela m'aidera à personnaliser mes recommandations. 🎯",
                "Parfait ! Ces détails sont précieux pour optimiser l'analyse LazyRepo. 🚀"
            ]
            response = random.choice(default_responses)
            
            # Ajouter une suggestion contextuelle
            if selected_crews:
                response += f"\n\nAu fait, avec vos équipes actuelles ({len(selected_crews)} activées), voulez-vous que je vous pose des questions plus spécifiques ?"
        
        self.add_ai_message("🤖 Assistant IA", response)
    
    def get_selected_crews_summary(self):
        """Retourne un résumé des équipes sélectionnées"""
        selected_crews = self.options_manager.get_selected_crews()
        active_crews = []
        
        for crew, agents in selected_crews.items():
            active_agents = [agent for agent, active in agents.items() if active]
            if active_agents:
                active_crews.append({
                    'name': crew,
                    'agents': active_agents,
                    'count': len(active_agents)
                })
        
        return active_crews
    
    def get_selected_languages(self):
        """Retourne la liste des langages sélectionnés"""
        return [lang for lang, var in self.languages_vars.items() if var.get()]
    
    def generate_suggestions(self, selected_crews, selected_languages, has_project_folder):
        """Génère des suggestions personnalisées"""
        if not selected_crews and not selected_languages:
            return ("🎯 Recommandations pour débuter :\n\n"
                   "1. Commencez par sélectionner l'équipe 📚 Documentation\n"
                   "2. Ajoutez votre langage principal\n"
                   "3. Si c'est un projet web, activez 🔒 Security\n\n"
                   "💡 Pour une démonstration complète, essayez le bouton 'Analyser le projet' !")
        
        suggestions = ["🎯 Suggestions personnalisées :\n"]
        
        if selected_languages:
            lang_count = len(selected_languages)
            if lang_count == 1:
                suggestions.append(f"• Excellent focus sur {selected_languages[0]} ! Considérez ajouter les tests automatiques.")
            elif lang_count > 5:
                suggestions.append(f"• {lang_count} langages détectés ! L'équipe Code Improvement sera très utile.")
            else:
                suggestions.append(f"• Belle stack multi-langages ({lang_count} langages). Parfait pour une analyse complète !")
        
        if selected_crews:
            crew_names = [crew['name'] for crew in selected_crews]
            if "📚 Documentation" in str(crew_names) and "📱 Social Content" in str(crew_names):
                suggestions.append("• Combinaison Documentation + Social parfaite pour l'open source ! 🌟")
            
            if "🔒 Security" in str(crew_names):
                suggestions.append("• Excellent choix avec Security ! Pensez aux variables d'environnement.")
        
        if not has_project_folder:
            suggestions.append("• 💡 Conseil : Sélectionnez un dossier pour une analyse réelle, ou utilisez le mode démo !")
        
        suggestions.append("\n❓ Voulez-vous que je vous pose des questions plus spécifiques ?")
        
        return "\n".join(suggestions)
    
    def generate_contextual_questions(self, selected_crews, selected_languages):
        """Génère des questions contextuelles basées sur les sélections"""
        if not selected_crews:
            return ("🤔 Questions pour vous aider :\n\n"
                   "• Quel est l'objectif principal de votre projet ?\n"
                   "• S'agit-il d'un projet open source ou privé ?\n"
                   "• Avez-vous une équipe de développement ?\n\n"
                   "Ces informations m'aideront à recommander les bonnes équipes !")
        
        questions = []
        crew_names = [crew['name'] for crew in selected_crews]
        
        # Questions spécifiques selon les équipes sélectionnées
        if any("Documentation" in name for name in crew_names):
            if "doc_target" not in self.ai_questions_asked:
                questions.append("📚 Documentation : Votre documentation cible-t-elle les développeurs ou les utilisateurs finaux ?")
                self.ai_questions_asked.add("doc_target")
        
        if any("Security" in name for name in crew_names):
            if "security_level" not in self.ai_questions_asked:
                questions.append("🔒 Sécurité : Votre projet manipule-t-il des données sensibles ou des APIs externes ?")
                self.ai_questions_asked.add("security_level")
        
        if any("Social" in name for name in crew_names):
            if "social_platform" not in self.ai_questions_asked:
                questions.append("📱 Social : Sur quelles plateformes souhaitez-vous promouvoir votre projet ?")
                self.ai_questions_asked.add("social_platform")
        
        if any("Improvement" in name for name in crew_names):
            if "code_style" not in self.ai_questions_asked:
                questions.append("🔧 Code : Avez-vous des standards de code spécifiques ou des conventions d'équipe ?")
                self.ai_questions_asked.add("code_style")
        
        # Questions sur les langages
        if selected_languages and "language_framework" not in self.ai_questions_asked:
            main_lang = selected_languages[0]
            questions.append(f"💻 {main_lang} : Utilisez-vous des frameworks spécifiques (React, Django, Spring...) ?")
            self.ai_questions_asked.add("language_framework")
        
        if not questions:
            # Questions générales si toutes les spécifiques ont été posées
            general_questions = [
                "🎯 Quel est le public cible principal de votre projet ?",
                "⏰ Avez-vous des contraintes de délai particulières ?",
                "🔄 S'agit-il d'un projet en maintenance ou en développement actif ?",
                "🌍 Le projet sera-t-il déployé internationalement ?"
            ]
            questions.append(random.choice(general_questions))
        
        if questions:
            return f"🤔 Question personnalisée :\n\n{questions[0]}\n\n💡 Vos réponses m'aident à optimiser la configuration LazyRepo !"
        else:
            return ("✅ Excellente configuration ! Vous semblez avoir tout couvert.\n\n"
                   "🚀 Prêt à lancer l'analyse ? Ou avez-vous d'autres questions ?")
    
    # ============ NOUVELLES FONCTIONNALITÉS RÉSULTATS (PROMPT 3) ============
    
    def start_demo_analysis(self):
        """Démarre la simulation d'analyse LazyRepo"""
        if self.analysis_running:
            return
        
        self.analysis_running = True
        self.analysis_progress = 0
        
        # Activer l'onglet Résultats et y basculer
        self.notebook.tab(1, state="normal")
        self.notebook.select(1)
        
        # Initialiser les informations du projet
        selected_crews = self.get_selected_crews_summary()
        selected_languages = self.get_selected_languages()
        
        project_info = f"Projet: {self.project_name.get()} | "
        project_info += f"Équipes: {len(selected_crews)} | "
        project_info += f"Langages: {len(selected_languages)}"
        
        self.project_info_label.config(text=project_info, foreground="black")
        
        # Générer des métriques de démonstration
        self.generate_demo_metrics()
        
        # Démarrer l'animation de progression
        self.animate_analysis_progress()
    
    def generate_demo_metrics(self):
        """Génère des métriques de démonstration réalistes"""
        selected_languages = self.get_selected_languages()
        selected_crews = self.get_selected_crews_summary()
        
        # Métriques basées sur les sélections
        base_files = random.randint(15, 45)
        lines_multiplier = {"Python": 150, "JavaScript": 120, "Java": 200, "C++": 180}
        
        total_lines = 0
        for lang in selected_languages:
            multiplier = lines_multiplier.get(lang, 100)
            total_lines += random.randint(50, 300) * multiplier // 100
        
        if not total_lines:  # Si aucun langage sélectionné
            total_lines = random.randint(500, 2000)
        
        self.demo_metrics = {
            "📁 Fichiers analysés": base_files + len(selected_languages) * 3,
            "💻 Lignes de code": total_lines,
            "🌐 Langages détectés": len(selected_languages) if selected_languages else random.randint(2, 4),
            "🤖 Agents actifs": sum(crew['count'] for crew in selected_crews),
            "📄 Fichiers générés": len(selected_crews) * 3 + random.randint(2, 6),
            "⏱️ Temps d'analyse": "Calcul en cours..."
        }
        
        # Générer la liste des fichiers
        self.generate_demo_files()
    
    def generate_demo_files(self):
        """Génère une liste de fichiers de démonstration"""
        self.generated_files = []
        
        # Fichiers de base toujours présents
        base_files = [
            ("README.md", "📚 Documentation", "# Mon Projet\n\nDescription automatique générée par LazyRepo...\n\n## Installation\n\n```bash\npip install -r requirements.txt\n```"),
            (".gitignore", "🔒 Security", "# LazyRepo - Configuration sécurisée\n__pycache__/\n*.pyc\n.env\n*.log\nvenv/"),
            ("SECURITY.md", "🔒 Security", "# Politique de Sécurité\n\n## Signalement de vulnérabilités\n\nCe document a été généré automatiquement..."),
        ]
        
        # Fichiers selon les équipes sélectionnées
        selected_crews = self.get_selected_crews_summary()
        
        for crew in selected_crews:
            if "Documentation" in crew['name']:
                base_files.extend([
                    ("docs/API.md", "📚 Documentation", "# Documentation API\n\n## Endpoints\n\n### GET /api/status\nRetourne le statut de l'application..."),
                    ("docs/INSTALL.md", "📚 Documentation", "# Guide d'Installation\n\n## Prérequis\n\n- Python 3.8+\n- Git\n...")
                ])
            
            if "Security" in crew['name']:
                base_files.extend([
                    (".env.example", "🔒 Security", "# Variables d'environnement\nDATABASE_URL=\nSECRET_KEY=\nAPI_KEY="),
                    ("docker-compose.yml", "🔒 Security", "version: '3.8'\nservices:\n  app:\n    build: .\n    environment:\n      - NODE_ENV=production")
                ])
            
            if "Social" in crew['name']:
                base_files.extend([
                    ("SOCIAL_POSTS.md", "📱 Social Content", "# Posts LinkedIn\n\n## Post 1 - Annonce du projet\n\n🚀 Fier de présenter mon nouveau projet..."),
                    ("PRESS_KIT.md", "📱 Social Content", "# Kit Presse\n\n## Description courte\n\nNotre projet révolutionne...")
                ])
            
            if "Improvement" in crew['name']:
                base_files.extend([
                    ("CODE_REVIEW.md", "🔧 Code Improvement", "# Analyse du Code\n\n## Suggestions d'amélioration\n\n- Ajouter des docstrings..."),
                    ("REFACTORING.md", "🔧 Code Improvement", "# Plan de Refactoring\n\n## Optimisations proposées\n\n1. Extraction de méthodes...")
                ])
        
        # Ajouter quelques fichiers de langages spécifiques
        selected_languages = self.get_selected_languages()
        for lang in selected_languages[:3]:  # Limiter à 3 pour l'exemple
            if lang == "Python":
                base_files.append(("requirements.txt", "🔧 Code Improvement", "# Dépendances Python\nflask==2.0.1\nrequests==2.25.1\npandas==1.3.0"))
            elif lang == "JavaScript":
                base_files.append(("package.json", "🔧 Code Improvement", '{\n  "name": "mon-projet",\n  "version": "1.0.0",\n  "dependencies": {\n    "express": "^4.17.1"\n  }\n}'))
            elif lang == "Java":
                base_files.append(("pom.xml", "🔧 Code Improvement", '<?xml version="1.0"?>\n<project>\n  <groupId>com.example</groupId>\n  <artifactId>mon-projet</artifactId>\n</project>'))
        
        self.generated_files = base_files[:self.demo_metrics.get("📄 Fichiers générés", 8)]
    
    def animate_analysis_progress(self):
        """Anime la progression de l'analyse"""
        if not self.analysis_running:
            return
        
        # Incrémenter la progression
        self.analysis_progress = min(self.analysis_progress + random.randint(3, 8), 100)
        
        # Mettre à jour la barre de progression
        self.progress_bar['value'] = self.analysis_progress
        
        # Mettre à jour le label de progression
        if self.analysis_progress < 100:
            current_step = min(len(self.analysis_steps) - 1, self.analysis_progress // 12)
            self.progress_label.config(text=f"{self.analysis_progress}% - {self.analysis_steps[current_step]}")
            
            # Mettre à jour les étapes
            for i, label in enumerate(self.step_labels):
                if i < current_step:
                    label.config(text=f"✅ {self.analysis_steps[i]}", foreground="green")
                elif i == current_step:
                    label.config(text=f"🔄 {self.analysis_steps[i]}", foreground="orange")
                else:
                    label.config(text=f"⏳ {self.analysis_steps[i]}", foreground="gray")
            
            # Mettre à jour les métriques progressivement
            self.update_metrics_animation()
            
            # Continuer l'animation
            self.root.after(random.randint(200, 600), self.animate_analysis_progress)
        else:
            # Analyse terminée
            self.finish_analysis()
    
    def update_metrics_animation(self):
        """Met à jour les métriques pendant l'animation"""
        progress_ratio = self.analysis_progress / 100
        
        for metric, final_value in self.demo_metrics.items():
            if metric == "⏱️ Temps d'analyse":
                elapsed = int(self.analysis_progress * 0.5)  # Simulation du temps
                self.metrics_widgets[metric].config(text=f"{elapsed}s")
            elif isinstance(final_value, int):
                current_value = int(final_value * progress_ratio)
                if metric == "💻 Lignes de code":
                    self.metrics_widgets[metric].config(text=f"{current_value:,}")
                else:
                    self.metrics_widgets[metric].config(text=str(current_value))
        
        # Remplir progressivement la liste des fichiers
        files_to_show = int(len(self.generated_files) * progress_ratio)
        self.files_listbox.delete(0, tk.END)
        for i in range(files_to_show):
            if i < len(self.generated_files):
                filename, category, _ = self.generated_files[i]
                self.files_listbox.insert(tk.END, f"📄 {filename} ({category})")
    
    def finish_analysis(self):
        """Finalise l'analyse et affiche les résultats complets"""
        self.analysis_running = False
        self.progress_label.config(text="100% - ✅ Analyse terminée avec succès!", foreground="green")
        
        # Marquer toutes les étapes comme terminées
        for i, label in enumerate(self.step_labels):
            label.config(text=f"✅ {self.analysis_steps[i]}", foreground="green")
        
        # Finaliser les métriques
        total_time = random.randint(15, 45)
        self.demo_metrics["⏱️ Temps d'analyse"] = f"{total_time}s"
        self.metrics_widgets["⏱️ Temps d'analyse"].config(text=f"{total_time}s")
        
        # Afficher tous les fichiers
        self.files_listbox.delete(0, tk.END)
        for filename, category, _ in self.generated_files:
            self.files_listbox.insert(tk.END, f"📄 {filename} ({category})")
        
        # Message de fin
        messagebox.showinfo("Analyse terminée", 
                           "🎉 Analyse LazyRepo terminée avec succès !\n\n"
                           f"✅ {len(self.generated_files)} fichiers générés\n"
                           f"⏱️ Temps total: {total_time}s\n"
                           f"🤖 {sum(crew['count'] for crew in self.get_selected_crews_summary())} agents utilisés\n\n"
                           "Explorez les résultats par équipe et consultez les fichiers générés !")
    
    def show_category_results(self, category):
        """Affiche les résultats d'une catégorie spécifique"""
        self.current_result_category = category
        
        # Nettoyer l'affichage précédent
        for widget in self.category_results_frame.winfo_children():
            widget.destroy()
        
        # Créer l'affichage pour la catégorie
        category_header = ttk.Frame(self.category_results_frame)
        category_header.pack(fill="x", pady=(0, 10))
        
        # Titre de la catégorie
        icons = {"Documentation": "📚", "Code Improvement": "🔧", 
                "Security": "🔒", "Social Content": "📱"}
        icon = icons.get(category, "📋")
        
        ttk.Label(category_header, text=f"{icon} Résultats - {category}", 
                 font=("Arial", 14, "bold")).pack(anchor="w")
        
        # Filtrer les fichiers de cette catégorie
        category_files = [f for f in self.generated_files if f[1] == f"{icon} {category}"]
        
        if category_files:
            ttk.Label(category_header, text=f"📄 {len(category_files)} fichier(s) généré(s)", 
                     foreground="green").pack(anchor="w")
            
            # Liste des fichiers de la catégorie
            files_frame = ttk.Frame(self.category_results_frame)
            files_frame.pack(fill="both", expand=True)
            
            for filename, _, content_preview in category_files:
                file_item = ttk.Frame(files_frame)
                file_item.pack(fill="x", pady=5)
                
                file_btn = ttk.Button(file_item, text=f"📄 {filename}",
                                     command=lambda f=filename, c=content_preview: self.show_file_details(f, c))
                file_btn.pack(side="left")
                
                size_label = ttk.Label(file_item, text=f"({len(content_preview)} caractères)", 
                                      foreground="gray", font=("Arial", 8))
                size_label.pack(side="left", padx=(10, 0))
        else:
            ttk.Label(category_header, text="Aucun fichier généré pour cette catégorie", 
                     foreground="gray").pack(anchor="w", pady=20)
    
    def show_file_details(self, filename, content):
        """Affiche les détails d'un fichier dans une nouvelle fenêtre"""
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"LazyRepo - Aperçu de {filename}")
        detail_window.geometry("600x400")
        
        # En-tête
        header_frame = ttk.Frame(detail_window)
        header_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(header_frame, text=f"📄 {filename}", 
                 font=("Arial", 14, "bold")).pack(anchor="w")
        ttk.Label(header_frame, text="Contenu généré par LazyRepo (démonstration)", 
                 foreground="gray").pack(anchor="w")
        
        # Contenu
        content_frame = ttk.Frame(detail_window)
        content_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Zone de texte avec scrollbar
        text_scrollbar = ttk.Scrollbar(content_frame)
        text_scrollbar.pack(side="right", fill="y")
        
        content_text = tk.Text(content_frame, yscrollcommand=text_scrollbar.set,
                              font=("Consolas", 9), wrap=tk.WORD)
        content_text.pack(side="left", fill="both", expand=True)
        text_scrollbar.config(command=content_text.yview)
        
        content_text.insert("1.0", content)
        content_text.config(state="disabled")
        
        # Boutons
        buttons_frame = ttk.Frame(detail_window)
        buttons_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        ttk.Button(buttons_frame, text="💾 Sauvegarder (démo)", 
                  command=lambda: self.demo_save_file(filename)).pack(side="left", padx=(0, 10))
        ttk.Button(buttons_frame, text="✏️ Éditer (démo)", 
                  command=lambda: self.demo_edit_file(filename)).pack(side="left", padx=(0, 10))
        ttk.Button(buttons_frame, text="❌ Fermer", 
                  command=detail_window.destroy).pack(side="right")
    
    def preview_generated_file(self, event=None):
        """Prévisualise un fichier sélectionné dans la listbox"""
        selection = self.files_listbox.curselection()
        if not selection:
            return
        
        selected_item = self.files_listbox.get(selection[0])
        # Extraire le nom du fichier (supprimer les emojis et catégorie)
        filename = selected_item.split("📄 ")[1].split(" (")[0]
        
        # Trouver le contenu correspondant
        for file_info in self.generated_files:
            if file_info[0] == filename:
                content = file_info[2]
                
                # Afficher dans la zone de prévisualisation
                self.file_preview.config(state="normal")
                self.file_preview.delete("1.0", tk.END)
                self.file_preview.insert("1.0", f"=== {filename} ===\n\n{content}")
                self.file_preview.config(state="disabled")
                break
    
    def demo_download_files(self):
        """Démonstration: Téléchargement des fichiers"""
        messagebox.showinfo("Téléchargement", 
                           f"🎭 Mode démonstration\n\n"
                           f"Téléchargement de {len(self.generated_files)} fichiers...\n\n"
                           f"Dans la vraie application, les fichiers seraient sauvegardés "
                           f"dans le dossier de votre projet.")
    
    def demo_restart_analysis(self):
        """Démonstration: Relance de l'analyse"""
        response = messagebox.askyesno("Relancer l'analyse", 
                                      "Voulez-vous vraiment relancer l'analyse ?\n\n"
                                      "⚠️ Cela réinitialisera tous les résultats actuels.")
        if response:
            # Réinitialiser les variables
            self.analysis_progress = 0
            self.analysis_running = False
            self.progress_bar['value'] = 0
            self.progress_label.config(text="0% - En attente de démarrage", foreground="gray")
            
            # Nettoyer les fichiers
            self.files_listbox.delete(0, tk.END)
            self.file_preview.config(state="normal")
            self.file_preview.delete("1.0", tk.END)
            self.file_preview.config(state="disabled")
            
            # Relancer
            self.start_demo_analysis()
    
    def demo_show_full_report(self):
        """Démonstration: Affichage du rapport complet"""
        selected_crews = self.get_selected_crews_summary()
        selected_languages = self.get_selected_languages()
        
        report_lines = [
            "📊 RAPPORT COMPLET D'ANALYSE LAZYREPO",
            "=" * 50,
            "",
            f"🎯 Projet: {self.project_name.get()}",
            f"📁 Dossier: {self.project_path.get()}",
            f"📅 Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}",
            "",
            "📈 MÉTRIQUES:",
        ]
        
        for metric, value in self.demo_metrics.items():
            report_lines.append(f"  {metric}: {value}")
        
        report_lines.extend([
            "",
            "🤖 ÉQUIPES UTILISÉES:",
        ])
        
        for crew in selected_crews:
            report_lines.append(f"  {crew['name']}: {crew['count']} agent(s)")
        
        report_lines.extend([
            "",
            "💻 LANGAGES ANALYSÉS:",
            f"  {', '.join(selected_languages) if selected_languages else 'Aucun langage spécifique'}",
            "",
            "📄 FICHIERS GÉNÉRÉS:",
        ])
        
        for filename, category, _ in self.generated_files:
            report_lines.append(f"  📄 {filename} ({category})")
        
        # Afficher dans une nouvelle fenêtre
        report_window = tk.Toplevel(self.root)
        report_window.title("LazyRepo - Rapport Complet")
        report_window.geometry("700x500")
        
        # Zone de texte avec scrollbar
        text_frame = ttk.Frame(report_window)
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")
        
        report_text = tk.Text(text_frame, yscrollcommand=scrollbar.set,
                             font=("Consolas", 9), wrap=tk.WORD)
        report_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=report_text.yview)
        
        report_text.insert("1.0", "\n".join(report_lines))
        report_text.config(state="disabled")
        
        # Bouton de fermeture
        ttk.Button(report_window, text="❌ Fermer", 
                  command=report_window.destroy).pack(pady=10)
    
    def demo_save_file(self, filename):
        """Démonstration: Sauvegarde d'un fichier"""
        messagebox.showinfo("Sauvegarde", 
                           f"🎭 Mode démonstration\n\n"
                           f"Fichier '{filename}' sauvegardé !\n\n"
                           f"Dans la vraie application, le fichier serait "
                           f"écrit dans votre projet.")
    
    def demo_edit_file(self, filename):
        """Démonstration: Édition d'un fichier"""
        messagebox.showinfo("Édition", 
                           f"🎭 Mode démonstration\n\n"
                           f"Ouverture de '{filename}' dans l'éditeur...\n\n"
                           f"Dans la vraie application, le fichier s'ouvrirait "
                           f"dans votre éditeur préféré.")
    
    # ============ NOUVELLES FONCTIONNALITÉS AMÉLIORATION (PROMPT 4) ============
    
    def demo_scan_project(self):
        """Démonstration: Scanner tout le projet"""
        messagebox.showinfo("Scanner", 
                           "🔍 Scan du projet en cours...\n\n"
                           "Analysing des fichiers de code source...")
        
        # Simuler un délai de scan
        self.root.after(1000, self.populate_demo_files)
    
    def populate_demo_files(self):
        """Remplit la liste avec des fichiers de démonstration"""
        # Vider la liste actuelle
        for item in self.files_tree.get_children():
            self.files_tree.delete(item)
        
        # Générer des fichiers de démonstration réalistes
        demo_files = [
            ("main.py", "Python", "2.3 KB", "Il y a 2h", "✅ Analysé"),
            ("app.js", "JavaScript", "5.7 KB", "Il y a 1h", "⚠️ Améliorable"),
            ("style.css", "CSS", "1.8 KB", "Il y a 3h", "✅ Analysé"),
            ("index.html", "HTML", "3.2 KB", "Il y a 4h", "🔍 En cours"),
            ("config.json", "JSON", "892 B", "Il y a 1j", "✅ Analysé"),
            ("utils.py", "Python", "4.1 KB", "Il y a 30m", "⚠️ Améliorable"),
            ("README.md", "Markdown", "1.5 KB", "Il y a 2j", "📝 À documenter"),
            ("database.py", "Python", "8.4 KB", "Il y a 1h", "🔒 Sécurité à vérifier"),
            ("components.js", "JavaScript", "6.2 KB", "Il y a 45m", "⚡ Performance"),
            ("test_main.py", "Python", "3.8 KB", "Il y a 1j", "🧪 Tests OK"),
        ]
        
        # Ajouter les fichiers au Treeview
        for i, (nom, type_file, taille, modif, statut) in enumerate(demo_files):
            # Ajouter une icône selon le type
            if type_file == "Python":
                display_nom = f"🐍 {nom}"
            elif type_file == "JavaScript":
                display_nom = f"🟨 {nom}"
            elif type_file == "CSS":
                display_nom = f"🎨 {nom}"
            elif type_file == "HTML":
                display_nom = f"🌐 {nom}"
            elif type_file == "JSON":
                display_nom = f"📋 {nom}"
            elif type_file == "Markdown":
                display_nom = f"📝 {nom}"
            else:
                display_nom = f"📄 {nom}"
            
            self.files_tree.insert("", "end", values=(display_nom, type_file, taille, modif, statut))
        
        # Mettre à jour le compteur
        self.files_count_label.config(text=f"{len(demo_files)} fichier(s)", foreground="green")
        
        # Stocker pour les filtres
        self.scanned_files = demo_files
        
        messagebox.showinfo("Scan terminé", 
                           f"✅ Scan terminé avec succès !\n\n"
                           f"📁 {len(demo_files)} fichiers analysés\n"
                           f"⚠️ {len([f for f in demo_files if 'Améliorable' in f[4]])} fichiers nécessitent des améliorations\n"
                           f"🔒 {len([f for f in demo_files if 'Sécurité' in f[4]])} fichiers nécessitent une vérification sécurité")
    
    def demo_scan_specific_files(self):
        """Démonstration: Scanner des fichiers spécifiques"""
        files = filedialog.askopenfilenames(
            title="Sélectionner les fichiers à analyser",
            filetypes=[
                ("Fichiers Python", "*.py"),
                ("Fichiers JavaScript", "*.js"),
                ("Fichiers HTML", "*.html"),
                ("Fichiers CSS", "*.css"),
                ("Tous les fichiers", "*.*")
            ]
        )
        
        if files:
            messagebox.showinfo("Scan spécifique", 
                               f"🎭 Mode démonstration\n\n"
                               f"Analyse de {len(files)} fichier(s) sélectionné(s)...\n\n"
                               f"Dans la vraie application, ces fichiers seraient analysés individuellement.")
            
            # Simuler l'ajout de fichiers spécifiques
            self.root.after(500, self.populate_demo_files)
    
    def demo_refresh_scan(self):
        """Démonstration: Actualiser le scan"""
        messagebox.showinfo("Actualisation", 
                           "🔄 Actualisation du scan...\n\n"
                           "Recherche de nouveaux fichiers et mises à jour...")
        
        self.root.after(800, self.populate_demo_files)
    
    def apply_file_filters(self, event=None):
        """Applique les filtres sur la liste des fichiers"""
        if not hasattr(self, 'scanned_files') or not self.scanned_files:
            return
        
        # Vider la liste actuelle
        for item in self.files_tree.get_children():
            self.files_tree.delete(item)
        
        # Appliquer les filtres
        file_type_filter = self.file_type_filter.get()
        size_filter = self.size_filter.get()
        
        filtered_files = []
        for nom, type_file, taille, modif, statut in self.scanned_files:
            # Filtre par type
            if file_type_filter != "Tous":
                if file_type_filter.startswith(type_file):
                    pass  # Le fichier passe le filtre
                else:
                    continue  # Le fichier ne passe pas le filtre
            
            # Filtre par taille (simulation simple)
            if size_filter != "Toutes":
                # Dans une vraie app, on comparerait la vraie taille
                pass  # Simulation : tous les fichiers passent
            
            filtered_files.append((nom, type_file, taille, modif, statut))
        
        # Réafficher les fichiers filtrés
        for nom, type_file, taille, modif, statut in filtered_files:
            # Ajouter une icône selon le type
            if type_file == "Python":
                display_nom = f"🐍 {nom}"
            elif type_file == "JavaScript":
                display_nom = f"🟨 {nom}"
            elif type_file == "CSS":
                display_nom = f"🎨 {nom}"
            elif type_file == "HTML":
                display_nom = f"🌐 {nom}"
            elif type_file == "JSON":
                display_nom = f"📋 {nom}"
            elif type_file == "Markdown":
                display_nom = f"📝 {nom}"
            else:
                display_nom = f"📄 {nom}"
            
            self.files_tree.insert("", "end", values=(display_nom, type_file, taille, modif, statut))
        
        # Mettre à jour le compteur
        self.files_count_label.config(text=f"{len(filtered_files)} fichier(s)", 
                                     foreground="green" if filtered_files else "gray")
    
    def on_file_double_click(self, event):
        """Gestion du double-clic sur un fichier"""
        selection = self.files_tree.selection()
        if not selection:
            return
        
        item = self.files_tree.item(selection[0])
        values = item['values']
        filename = values[0].split(' ', 1)[1] if ' ' in values[0] else values[0]  # Enlever l'emoji
        
        # Ouvrir le détail du fichier
        self.show_file_improvement_details(filename, values)
    
    def show_file_context_menu(self, event):
        """Affiche le menu contextuel pour un fichier"""
        selection = self.files_tree.selection()
        if not selection:
            return
        
        # Créer le menu contextuel
        context_menu = tk.Menu(self.root, tearoff=0)
        context_menu.add_command(label="📝 Analyser ce fichier", 
                               command=lambda: self.analyze_single_file(selection[0]))
        context_menu.add_command(label="⚡ Actions rapides", 
                               command=lambda: self.quick_actions_for_file(selection[0]))
        context_menu.add_separator()
        context_menu.add_command(label="👁️ Voir détails", 
                               command=lambda: self.on_file_double_click(event))
        context_menu.add_command(label="🔄 Actualiser statut", 
                               command=lambda: self.refresh_file_status(selection[0]))
        
        # Afficher le menu
        try:
            context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            context_menu.grab_release()
    
    def select_all_files(self):
        """Sélectionne tous les fichiers"""
        self.files_tree.selection_set(self.files_tree.get_children())
        self.update_selected_files_label()
    
    def deselect_all_files(self):
        """Désélectionne tous les fichiers"""
        self.files_tree.selection_remove(self.files_tree.get_children())
        self.update_selected_files_label()
    
    def update_selected_files_label(self):
        """Met à jour le label des fichiers sélectionnés"""
        selected = self.files_tree.selection()
        count = len(selected)
        
        if count == 0:
            self.selected_files_label.config(text="Aucun fichier sélectionné", foreground="gray")
        elif count == 1:
            self.selected_files_label.config(text="1 fichier sélectionné", foreground="blue")
        else:
            self.selected_files_label.config(text=f"{count} fichiers sélectionnés", foreground="blue")
    
    def demo_quick_action(self, action_type):
        """Démonstration: Exécute une action rapide"""
        selected = self.files_tree.selection()
        
        if not selected:
            messagebox.showwarning("Aucune sélection", 
                                 "Veuillez sélectionner au moins un fichier dans la liste.")
            return
        
        action_names = {
            "comments": "Ajout de commentaires",
            "security": "Sécurisation des secrets",
            "docstrings": "Génération de docstrings",
            "format": "Formatage du code",
            "bugs": "Détection de bugs",
            "optimize": "Optimisation des performances",
            "tests": "Génération de tests",
            "complexity": "Analyse de complexité",
            "refactor": "Refactoring"
        }
        
        action_name = action_names.get(action_type, "Action inconnue")
        file_count = len(selected)
        
        # Simuler l'action
        messagebox.showinfo("Action en cours", 
                           f"🔄 {action_name} en cours...\n\n"
                           f"📁 {file_count} fichier(s) traité(s)\n"
                           f"⏱️ Estimation: {file_count * 2}s")
        
        # Simuler la completion avec délai
        self.root.after(1500, lambda: self.complete_quick_action(action_type, file_count))
    
    def complete_quick_action(self, action_type, file_count):
        """Complète l'action rapide"""
        action_results = {
            "comments": f"✅ {file_count * 15} commentaires ajoutés",
            "security": f"🔒 {file_count * 3} secrets sécurisés",
            "docstrings": f"📚 {file_count * 8} docstrings générées",
            "format": f"🎨 {file_count} fichiers formatés",
            "bugs": f"🐛 {file_count * 2} bugs potentiels détectés",
            "optimize": f"⚡ {file_count * 5} optimisations suggérées",
            "tests": f"🧪 {file_count * 4} tests générés",
            "complexity": f"📊 Complexité analysée pour {file_count} fichiers",
            "refactor": f"🔄 {file_count * 6} suggestions de refactoring"
        }
        
        result = action_results.get(action_type, "Action terminée")
        
        messagebox.showinfo("Action terminée", 
                           f"🎉 Action terminée avec succès !\n\n"
                           f"{result}\n\n"
                           f"Consultez l'historique des modifications pour plus de détails.")
        
        # Ajouter à l'historique
        timestamp = datetime.datetime.now().strftime("%H:%M")
        modification_entry = f"[{timestamp}] {result}"
        
        # Vider le placeholder si c'est la première modification
        if self.modifications_listbox.size() == 1 and "Aucune modification" in self.modifications_listbox.get(0):
            self.modifications_listbox.delete(0)
            self.modifications_listbox.config(foreground="black")
        
        self.modifications_listbox.insert(0, modification_entry)
        
        # Limiter l'historique à 20 entrées
        if self.modifications_listbox.size() > 20:
            self.modifications_listbox.delete(20, tk.END)
    
    # ============ INTÉGRATION IA GLOBALE ET NOTIFICATIONS CROSS-ONGLETS (PROMPT 5) ============
    
    def setup_global_ai_integration(self):
        """Configure l'intégration IA globale entre tous les onglets"""
        # Initialiser le contexte global de l'IA
        self.global_ai_context = {
            "current_project": {
                "name": "",
                "path": "",
                "languages": [],
                "crews": [],
                "complexity_score": 0
            },
            "user_behavior": {
                "preferred_crews": [],
                "common_languages": [],
                "interaction_patterns": [],
                "workflow_preferences": ""
            },
            "session_data": {
                "start_time": datetime.datetime.now(),
                "actions_count": 0,
                "questions_asked": 0,
                "improvements_applied": 0
            }
        }
        
        # Créer une barre de notifications globale
        self.create_global_notification_bar()
    
    def create_global_notification_bar(self):
        """Crée une barre de notifications en haut de l'interface"""
        # Frame pour les notifications au-dessus du notebook
        self.notifications_frame = ttk.Frame(self.root)
        self.notifications_frame.pack(fill="x", padx=10, pady=(10, 0))
        
        # Notification active (initialement cachée)
        self.active_notification_frame = ttk.Frame(self.notifications_frame)
        
        # Icône de notification
        self.notification_icon = ttk.Label(self.active_notification_frame, text="🔔", 
                                          font=("Arial", 12))
        self.notification_icon.pack(side="left", padx=(5, 10))
        
        # Texte de notification
        self.notification_text = ttk.Label(self.active_notification_frame, text="", 
                                          font=("Arial", 10), foreground="#1f2937")
        self.notification_text.pack(side="left", fill="x", expand=True)
        
        # Boutons d'action de notification
        self.notification_actions_frame = ttk.Frame(self.active_notification_frame)
        self.notification_actions_frame.pack(side="right", padx=10)
        
        # Bouton fermer notification
        self.close_notification_btn = ttk.Button(self.notification_actions_frame, text="✕", 
                                                 command=self.hide_notification, width=3)
        self.close_notification_btn.pack(side="right")
    
    def setup_cross_tab_notifications(self):
        """Configure le système de notifications entre onglets"""
        # Types de notifications inter-onglets
        self.notification_types = {
            "config_to_results": {
                "trigger": "analysis_started",
                "message": "💡 Suggestion : Une fois l'analyse terminée, consultez l'onglet Amélioration pour optimiser vos fichiers !",
                "action": "Aller à Amélioration",
                "target_tab": 2
            },
            "results_to_improvement": {
                "trigger": "results_complete",
                "message": "🔧 Recommandation : Vos résultats sont prêts ! Passez à l'onglet Amélioration pour scanner et optimiser vos fichiers.",
                "action": "Scanner maintenant",
                "target_tab": 2
            },
            "improvement_to_config": {
                "trigger": "files_improved",
                "message": "🔄 Idée : Après vos améliorations, vous pourriez relancer une analyse avec de nouvelles équipes !",
                "action": "Reconfigurer",
                "target_tab": 0
            },
            "smart_suggestion": {
                "trigger": "context_change",
                "message": "",  # Dynamique
                "action": "Voir détails",
                "target_tab": -1  # Variable
            }
        }
        
        # Queue des notifications en attente
        self.notification_queue = []
        self.current_notification = None
    
    def on_tab_changed(self, event):
        """Gère les changements d'onglets et l'apprentissage IA"""
        selected_tab = self.notebook.index(self.notebook.select())
        tab_names = ["configuration", "results", "improvement"]
        
        if selected_tab < len(tab_names):
            previous_stage = self.workflow_stage
            self.workflow_stage = tab_names[selected_tab]
            
            # Mettre à jour le contexte global
            self.update_global_ai_context()
            
            # Générer des recommandations intelligentes
            self.generate_smart_recommendations(previous_stage, self.workflow_stage)
            
            # Déclencher des notifications contextuelles
            self.trigger_contextual_notifications(selected_tab)
    
    def update_global_ai_context(self):
        """Met à jour le contexte global de l'IA"""
        # Mettre à jour les informations du projet
        self.global_ai_context["current_project"].update({
            "name": self.project_name.get(),
            "path": self.project_path.get(),
            "languages": self.get_selected_languages(),
            "crews": [crew['name'] for crew in self.get_selected_crews_summary()]
        })
        
        # Analyser les préférences utilisateur
        selected_crews = self.get_selected_crews_summary()
        if selected_crews:
            crew_types = [crew['name'] for crew in selected_crews]
            self.global_ai_context["user_behavior"]["preferred_crews"] = crew_types
            
            # Calculer un score de complexité du projet
            complexity_factors = {
                "crew_count": len(selected_crews),
                "language_count": len(self.get_selected_languages()),
                "has_security": any("Security" in crew for crew in crew_types),
                "has_documentation": any("Documentation" in crew for crew in crew_types)
            }
            
            complexity_score = (
                complexity_factors["crew_count"] * 2 +
                complexity_factors["language_count"] * 1.5 +
                (5 if complexity_factors["has_security"] else 0) +
                (3 if complexity_factors["has_documentation"] else 0)
            )
            
            self.global_ai_context["current_project"]["complexity_score"] = complexity_score
        
        # Incrémenter le compteur d'actions
        self.global_ai_context["session_data"]["actions_count"] += 1
    
    def generate_smart_recommendations(self, previous_stage, current_stage):
        """Génère des recommandations intelligentes basées sur le contexte"""
        recommendations = []
        context = self.global_ai_context
        
        # Recommandations basées sur la transition entre onglets
        if previous_stage == "configuration" and current_stage == "results":
            if not self.analysis_running and self.analysis_progress == 0:
                recommendations.append({
                    "type": "workflow_guidance",
                    "priority": "high",
                    "title": "Analyse non démarrée",
                    "message": "Vous consultez les résultats sans avoir lancé d'analyse. Retournez à la configuration pour démarrer !",
                    "action": "Lancer l'analyse",
                    "callback": lambda: self.notebook.select(0)
                })
        
        elif previous_stage == "results" and current_stage == "improvement":
            if hasattr(self, 'generated_files') and self.generated_files:
                recommendations.append({
                    "type": "cross_reference",
                    "priority": "medium",
                    "title": "Fichiers détectés",
                    "message": f"Votre analyse a généré {len(self.generated_files)} fichiers. Scannez-les pour des améliorations !",
                    "action": "Scanner les fichiers",
                    "callback": self.demo_scan_project
                })
        
        elif current_stage == "improvement":
            if not hasattr(self, 'scanned_files') or not self.scanned_files:
                recommendations.append({
                    "type": "action_needed",
                    "priority": "medium",
                    "title": "Scanner recommandé",
                    "message": "Commencez par scanner vos fichiers pour obtenir des suggestions d'amélioration personnalisées.",
                    "action": "Scanner maintenant",
                    "callback": self.demo_scan_project
                })
        
        # Recommandations basées sur la complexité du projet
        complexity = context["current_project"]["complexity_score"]
        languages = context["current_project"]["languages"]
        
        if complexity > 15 and current_stage == "configuration":
            recommendations.append({
                "type": "complexity_warning",
                "priority": "medium",
                "title": "Projet complexe détecté",
                "message": f"Votre projet semble complexe ({len(languages)} langages). Considérez activer l'équipe Security.",
                "action": "Activer Security",
                "callback": lambda: self.activate_security_crew()
            })
        
        # Recommandations basées sur l'historique
        session_time = (datetime.datetime.now() - context["session_data"]["start_time"]).total_seconds()
        if session_time > 300 and context["session_data"]["actions_count"] < 3:  # 5 minutes, peu d'actions
            recommendations.append({
                "type": "engagement",
                "priority": "low",
                "title": "Exploration suggérée",
                "message": "Vous explorez LazyRepo depuis un moment. Voulez-vous essayer une démonstration complète ?",
                "action": "Démo auto",
                "callback": self.start_auto_demo
            })
        
        # Ajouter les nouvelles recommandations
        for rec in recommendations:
            if rec not in self.smart_recommendations:
                self.smart_recommendations.append(rec)
        
        # Afficher la recommandation la plus prioritaire
        if recommendations:
            self.show_smart_recommendation(recommendations[0])
    
    def show_smart_recommendation(self, recommendation):
        """Affiche une recommandation intelligente"""
        priority_colors = {
            "high": "#ef4444",
            "medium": "#f59e0b", 
            "low": "#6b7280"
        }
        
        priority_icons = {
            "high": "⚠️",
            "medium": "💡",
            "low": "ℹ️"
        }
        
        icon = priority_icons.get(recommendation["priority"], "💡")
        color = priority_colors.get(recommendation["priority"], "#6b7280")
        
        # Créer une notification personnalisée
        notification_text = f"{icon} {recommendation['title']}: {recommendation['message']}"
        
        self.show_notification(
            notification_text,
            recommendation["action"],
            recommendation["callback"],
            bg_color=color
        )
    
    def show_notification(self, message, action_text=None, action_callback=None, bg_color="#3b82f6", duration=10000):
        """Affiche une notification avec actions optionnelles"""
        # Cacher la notification précédente
        self.hide_notification()
        
        # Configurer la nouvelle notification
        self.notification_text.config(text=message)
        self.notification_icon.config(foreground=bg_color)
        
        # Ajouter bouton d'action si fourni
        if action_text and action_callback:
            action_btn = ttk.Button(self.notification_actions_frame, text=action_text,
                                   command=lambda: self.execute_notification_action(action_callback))
            action_btn.pack(side="left", padx=(0, 5))
            self.current_action_btn = action_btn
        
        # Afficher la notification
        self.active_notification_frame.pack(fill="x", pady=(0, 5))
        self.active_notification_frame.configure(relief="solid", borderwidth=1)
        
        # Auto-hide après duration
        if duration > 0:
            self.root.after(duration, self.hide_notification)
        
        self.current_notification = {
            "message": message,
            "action": action_text,
            "callback": action_callback
        }
    
    def hide_notification(self):
        """Cache la notification active"""
        self.active_notification_frame.pack_forget()
        
        # Nettoyer le bouton d'action
        if hasattr(self, 'current_action_btn'):
            self.current_action_btn.destroy()
            delattr(self, 'current_action_btn')
        
        self.current_notification = None
    
    def execute_notification_action(self, callback):
        """Exécute l'action d'une notification"""
        self.hide_notification()
        if callback:
            try:
                callback()
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'exécution de l'action: {str(e)}")
    
    def trigger_contextual_notifications(self, tab_index):
        """Déclenche des notifications contextuelles selon l'onglet"""
        context = self.global_ai_context
        
        if tab_index == 0:  # Onglet Configuration
            self.check_configuration_suggestions()
        elif tab_index == 1:  # Onglet Résultats
            self.check_results_suggestions()
        elif tab_index == 2:  # Onglet Amélioration
            self.check_improvement_suggestions()
    
    def check_configuration_suggestions(self):
        """Vérifications et suggestions pour l'onglet Configuration"""
        selected_crews = self.get_selected_crews_summary()
        selected_languages = self.get_selected_languages()
        
        # Suggestion si aucune équipe sélectionnée
        if not selected_crews:
            self.show_notification(
                "🎯 Conseil : Sélectionnez au moins une équipe pour commencer votre analyse LazyRepo !",
                "Voir les équipes",
                lambda: self.scroll_to_crews_section()
            )
        
        # Suggestion pour projets multi-langages
        elif len(selected_languages) > 3 and not any("Security" in crew['name'] for crew in selected_crews):
            self.show_notification(
                "🔒 Recommandation : Projet multi-langages détecté. L'équipe Security est recommandée !",
                "Activer Security",
                self.activate_security_crew
            )
        
        # Suggestion pour l'amélioration de code
        elif selected_crews and not any("Improvement" in crew['name'] for crew in selected_crews):
            self.show_notification(
                "⚡ Idée : Ajoutez l'équipe Code Improvement pour des suggestions d'optimisation !",
                "Activer Improvement",
                self.activate_improvement_crew
            )
    
    def check_results_suggestions(self):
        """Vérifications et suggestions pour l'onglet Résultats"""
        if not self.analysis_running and self.analysis_progress == 0:
            self.show_notification(
                "📊 Info : Aucune analyse en cours. Retournez à la configuration pour démarrer !",
                "Configurer",
                lambda: self.notebook.select(0)
            )
        
        elif self.analysis_progress == 100:
            if hasattr(self, 'generated_files') and len(self.generated_files) > 5:
                self.show_notification(
                    f"🎉 Analyse terminée ! {len(self.generated_files)} fichiers générés. Passez à l'amélioration pour les optimiser !",
                    "Améliorer",
                    lambda: self.notebook.select(2)
                )
    
    def check_improvement_suggestions(self):
        """Vérifications et suggestions pour l'onglet Amélioration"""
        has_scanned = hasattr(self, 'scanned_files') and self.scanned_files
        
        if not has_scanned:
            self.show_notification(
                "🔍 Conseil : Commencez par scanner vos fichiers pour obtenir des suggestions personnalisées !",
                "Scanner",
                self.demo_scan_project
            )
        
        elif has_scanned and len(self.scanned_files) > 0:
            problematic_files = len([f for f in self.scanned_files if "Améliorable" in f[4] or "Sécurité" in f[4]])
            if problematic_files > 0:
                self.show_notification(
                    f"⚠️ {problematic_files} fichier(s) nécessitent des améliorations. Utilisez les actions rapides !",
                    "Actions rapides",
                    lambda: self.scroll_to_quick_actions()
                )
    
    def scroll_to_crews_section(self):
        """Scroll vers la section des équipes"""
        self.config_canvas.yview_moveto(0.3)  # Approximativement vers les crews
    
    def scroll_to_quick_actions(self):
        """Scroll vers les actions rapides"""
        self.improvement_canvas.yview_moveto(0.4)  # Approximativement vers les actions
    
    def activate_security_crew(self):
        """Active automatiquement l'équipe Security"""
        for crew_name, crew_data in self.options_manager.categories.items():
            if "Security" in crew_name:
                # Activer quelques agents de sécurité
                security_agents = list(crew_data['agents'].keys())[:2]  # Prendre 2 agents
                for agent_name in security_agents:
                    crew_data['agents'][agent_name].set(True)
                
                self.show_notification(
                    "✅ Équipe Security activée ! 2 agents de sécurité configurés.",
                    duration=3000
                )
                break
    
    def activate_improvement_crew(self):
        """Active automatiquement l'équipe Code Improvement"""
        for crew_name, crew_data in self.options_manager.categories.items():
            if "Code Improvement" in crew_name:
                # Activer tous les agents d'amélioration
                for var in crew_data['agents'].values():
                    var.set(True)
                
                self.show_notification(
                    "✅ Équipe Code Improvement activée ! Tous les agents configurés.",
                    duration=3000
                )
                break
    
    def start_auto_demo(self):
        """Démarre une démonstration automatique"""
        self.show_notification(
            "🚀 Démonstration automatique démarrée ! Suivez le guide...",
            duration=3000
        )
        
        # Séquence de démonstration
        self.root.after(2000, self.auto_demo_step_1)
    
    def auto_demo_step_1(self):
        """Étape 1 : Sélection automatique des langages"""
        self.demo_detect_languages()
        self.show_notification("1️⃣ Langages détectés automatiquement !", duration=2000)
        self.root.after(3000, self.auto_demo_step_2)
    
    def auto_demo_step_2(self):
        """Étape 2 : Activation des équipes"""
        self.demo_random_crew_selection()
        self.show_notification("2️⃣ Équipes configurées automatiquement !", duration=2000)
        self.root.after(3000, self.auto_demo_step_3)
    
    def auto_demo_step_3(self):
        """Étape 3 : Lancement de l'analyse"""
        self.demo_start_analysis()
        self.show_notification("3️⃣ Analyse lancée ! Consultez les résultats...", duration=3000)
    
    def create_ai_summary_widget(self):
        """Crée un widget de résumé IA flottant"""
        # Créer une fenêtre flottante pour le résumé
        self.ai_summary_window = tk.Toplevel(self.root)
        self.ai_summary_window.title("Assistant IA - Résumé du Projet")
        self.ai_summary_window.geometry("350x500")
        self.ai_summary_window.attributes('-topmost', True)
        
        # Positionner en haut à droite
        self.ai_summary_window.geometry("+{}+{}".format(
            self.root.winfo_x() + self.root.winfo_width() - 350,
            self.root.winfo_y()
        ))
        
        # Contenu du résumé
        summary_frame = ttk.Frame(self.ai_summary_window)
        summary_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        ttk.Label(summary_frame, text="🤖 Résumé IA en Temps Réel", 
                 font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))
        
        # Zone de texte pour le résumé
        self.ai_summary_text = tk.Text(summary_frame, height=20, wrap=tk.WORD,
                                      font=("Arial", 9), state="disabled")
        self.ai_summary_text.pack(fill="both", expand=True)
        
        # Boutons de contrôle
        controls_frame = ttk.Frame(summary_frame)
        controls_frame.pack(fill="x", pady=(10, 0))
        
        ttk.Button(controls_frame, text="🔄 Actualiser",
                  command=self.update_ai_summary).pack(side="left", padx=(0, 5))
        ttk.Button(controls_frame, text="❌ Fermer",
                  command=self.ai_summary_window.destroy).pack(side="right")
        
        # Actualiser le résumé
        self.update_ai_summary()
        
        # Auto-actualisation toutes les 30 secondes
        self.schedule_ai_summary_update()
    
    def update_ai_summary(self):
        """Met à jour le résumé IA"""
        context = self.global_ai_context
        
        summary_lines = [
            "📊 ÉTAT DU PROJET",
            "=" * 25,
            f"Nom: {context['current_project']['name']}",
            f"Complexité: {context['current_project']['complexity_score']}/20",
            f"Langages: {len(context['current_project']['languages'])}",
            f"Équipes: {len(context['current_project']['crews'])}",
            "",
            "🎯 RECOMMANDATIONS IA",
            "=" * 25
        ]
        
        # Ajouter les recommandations actives
        if self.smart_recommendations:
            for i, rec in enumerate(self.smart_recommendations[-3:], 1):  # Dernières 3
                summary_lines.append(f"{i}. {rec['title']}")
                summary_lines.append(f"   → {rec['message'][:50]}...")
                summary_lines.append("")
        else:
            summary_lines.append("Aucune recommandation pour le moment")
            summary_lines.append("")
        
        # Statistiques de session
        session_time = (datetime.datetime.now() - context['session_data']['start_time']).total_seconds()
        summary_lines.extend([
            "📈 STATISTIQUES SESSION",
            "=" * 25,
            f"Durée: {int(session_time//60)}m {int(session_time%60)}s",
            f"Actions: {context['session_data']['actions_count']}",
            f"Questions IA: {context['session_data']['questions_asked']}",
            f"Améliorations: {context['session_data']['improvements_applied']}",
            "",
            "🔄 Dernière mise à jour:",
            datetime.datetime.now().strftime("%H:%M:%S")
        ])
        
        # Mettre à jour le texte
        self.ai_summary_text.config(state="normal")
        self.ai_summary_text.delete("1.0", tk.END)
        self.ai_summary_text.insert("1.0", "\n".join(summary_lines))
        self.ai_summary_text.config(state="disabled")
    
    def schedule_ai_summary_update(self):
        """Programme la mise à jour automatique du résumé"""
        if hasattr(self, 'ai_summary_window') and self.ai_summary_window.winfo_exists():
            self.update_ai_summary()
            self.root.after(30000, self.schedule_ai_summary_update)  # 30 secondes
    
    def enhance_existing_ai_responses(self):
        """Améliore les réponses IA existantes avec le contexte global"""
        # Cette méthode sera appelée pour enrichir les réponses des chats existants
        pass
    
    def log_ai_interaction(self, interaction_type, details):
        """Enregistre les interactions IA pour l'apprentissage"""
        interaction = {
            "timestamp": datetime.datetime.now(),
            "type": interaction_type,
            "details": details,
            "context": self.workflow_stage
        }
        
        self.global_ai_context["session_data"]["interaction_history"].append(interaction)
        
        # Incrémenter les compteurs appropriés
        if interaction_type == "question":
            self.global_ai_context["session_data"]["questions_asked"] += 1
        elif interaction_type == "improvement":
            self.global_ai_context["session_data"]["improvements_applied"] += 1
    
    def add_improvement_chat_message(self, sender, message):
        """Ajoute un message au chat d'amélioration"""
        self.improvement_chat_display.config(state="normal")
        
        # Ajouter timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        # Ajouter le message
        if sender == "🤖 Assistant Amélioration":
            self.improvement_chat_display.insert(tk.END, f"[{timestamp}] {sender}:\n", "ai_sender")
            self.improvement_chat_display.insert(tk.END, f"{message}\n\n", "ai_message")
        else:
            self.improvement_chat_display.insert(tk.END, f"[{timestamp}] {sender}:\n", "user_sender")
            self.improvement_chat_display.insert(tk.END, f"{message}\n\n", "user_message")
        
        # Configurer les tags pour le style
        self.improvement_chat_display.tag_configure("ai_sender", foreground="#dc2626", font=("Arial", 9, "bold"))
        self.improvement_chat_display.tag_configure("ai_message", foreground="#1f2937")
        self.improvement_chat_display.tag_configure("user_sender", foreground="#059669", font=("Arial", 9, "bold"))
        self.improvement_chat_display.tag_configure("user_message", foreground="#374151")
        
        self.improvement_chat_display.config(state="disabled")
        self.improvement_chat_display.see(tk.END)
    
    def send_improvement_chat_message(self, event=None):
        """Envoie un message dans le chat d'amélioration"""
        message = self.improvement_chat_entry.get().strip()
        if not message:
            return
        
        # Ajouter le message de l'utilisateur
        self.add_improvement_chat_message("👤 Vous", message)
        self.improvement_chat_entry.delete(0, tk.END)
        
        # Générer la réponse de l'IA avec délai
        self.root.after(600, lambda: self.generate_improvement_ai_response(message))
    
    def generate_improvement_ai_response(self, user_message):
        """Génère une réponse de l'IA d'amélioration"""
        user_message_lower = user_message.lower()
        
        # Vérifier s'il y a des fichiers scannés
        has_scanned_files = hasattr(self, 'scanned_files') and self.scanned_files
        selected_files = self.files_tree.selection()
        
        # Réponses spécialisées selon le contexte
        if "aide" in user_message_lower or "help" in user_message_lower:
            response = ("🔧 Assistant d'amélioration à votre service !\n\n"
                       "Voici ce que je peux analyser :\n"
                       "• 📊 Qualité et complexité du code\n"
                       "• 🐛 Détection de bugs et problèmes\n"
                       "• ⚡ Optimisations de performance\n"
                       "• 🔒 Problèmes de sécurité\n"
                       "• 📝 Amélioration de la documentation\n"
                       "• 🧪 Suggestions de tests\n\n"
                       "Sélectionnez des fichiers et posez-moi des questions spécifiques !")
        
        elif "analyser" in user_message_lower or "analyse" in user_message_lower:
            if not has_scanned_files:
                response = ("🔍 Aucun fichier scanné pour le moment.\n\n"
                           "Utilisez le bouton '🔍 Scanner le projet' pour commencer l'analyse.\n"
                           "Ensuite, je pourrai analyser vos fichiers en détail !")
            elif not selected_files:
                response = ("📁 Sélectionnez d'abord des fichiers dans la liste ci-dessus.\n\n"
                           "Double-cliquez sur un fichier ou utilisez Ctrl+clic pour sélectionner plusieurs fichiers.\n"
                           "Ensuite, je pourrai vous donner des analyses détaillées !")
            else:
                file_count = len(selected_files)
                response = (f"🔍 Analyse de {file_count} fichier(s) sélectionné(s)...\n\n"
                           f"📊 Résultats d'analyse :\n"
                           f"• ✅ Code globalement bien structuré\n"
                           f"• ⚠️ {file_count * 2} améliorations suggérées\n"
                           f"• 🔒 {file_count} point(s) de sécurité à vérifier\n"
                           f"• 📝 Documentation à compléter\n\n"
                           f"Voulez-vous des détails sur un aspect spécifique ?")
        
        elif any(word in user_message_lower for word in ["bug", "erreur", "problème"]):
            if selected_files:
                response = ("🐛 Analyse des bugs potentiels...\n\n"
                           "Problèmes détectés :\n"
                           "• Variables non utilisées (2 occurrences)\n"
                           "• Gestion d'exceptions manquante\n"
                           "• Conditions toujours vraies/fausses\n"
                           "• Imports redondants\n\n"
                           "💡 Voulez-vous que je génère les corrections automatiquement ?")
            else:
                response = ("🐛 Pour détecter les bugs, je dois d'abord analyser vos fichiers.\n\n"
                           "Scannez votre projet et sélectionnez les fichiers à analyser.\n"
                           "Je pourrai alors détecter les problèmes potentiels !")
        
        elif any(word in user_message_lower for word in ["performance", "optimiser", "lent"]):
            response = ("⚡ Analyse des performances...\n\n"
                       "Optimisations suggérées :\n"
                       "• Utiliser des compréhensions de liste\n"
                       "• Mettre en cache les calculs répétitifs\n"
                       "• Optimiser les boucles imbriquées\n"
                       "• Utiliser des générateurs pour les gros datasets\n\n"
                       "📊 Impact estimé : +25% de performance\n\n"
                       "Souhaitez-vous voir des exemples de code optimisé ?")
        
        elif any(word in user_message_lower for word in ["sécurité", "security", "vulnérabilité"]):
            response = ("🔒 Analyse de sécurité en cours...\n\n"
                       "Points d'attention détectés :\n"
                       "• Clés API codées en dur (2 fichiers)\n"
                       "• Mots de passe en clair\n"
                       "• Validation d'entrée insuffisante\n"
                       "• Headers de sécurité manquants\n\n"
                       "🚨 Priorité : Migrer les secrets vers .env\n\n"
                       "Voulez-vous que je génère les fichiers .env et .gitignore ?")
        
        elif any(word in user_message_lower for word in ["test", "unittest", "pytest"]):
            response = ("🧪 Analyse de couverture de tests...\n\n"
                       "État actuel :\n"
                       "• 📊 Couverture : 45%\n"
                       "• ✅ 12 tests existants\n"
                       "• ❌ 8 fonctions sans tests\n"
                       "• 🎯 Fonctions critiques : 3 non testées\n\n"
                       "💡 Je peux générer des tests automatiquement !\n\n"
                       "Quel framework préférez-vous : unittest ou pytest ?")
        
        elif any(word in user_message_lower for word in ["documentation", "docstring", "commentaire"]):
            response = ("📚 Analyse de la documentation...\n\n"
                       "État de la documentation :\n"
                       "• 📝 60% des fonctions documentées\n"
                       "• ❌ 15 fonctions sans docstring\n"
                       "• 💡 Commentaires inline : insuffisants\n"
                       "• 📖 README : à mettre à jour\n\n"
                       "🚀 Je peux générer :\n"
                       "• Docstrings automatiques\n"
                       "• Commentaires explicatifs\n"
                       "• Documentation API\n\n"
                       "Par où commencer ?")
        
        else:
            # Réponses contextuelles par défaut
            if not has_scanned_files:
                response = ("💡 Commencez par scanner vos fichiers pour que je puisse vous aider !\n\n"
                           "Une fois le scan effectué, je pourrai :\n"
                           "• Analyser la qualité de votre code\n"
                           "• Suggérer des améliorations\n"
                           "• Détecter les problèmes potentiels\n\n"
                           "Tapez 'aide' pour voir toutes mes capacités !")
            else:
                response = ("🤔 Intéressant ! Pouvez-vous être plus spécifique ?\n\n"
                           "Par exemple :\n"
                           "• 'Analyser la sécurité' pour un audit sécurité\n"
                           "• 'Optimiser les performances' pour des suggestions d'optimisation\n"
                           "• 'Détecter les bugs' pour trouver des problèmes\n"
                           "• 'Générer des tests' pour la couverture de tests\n\n"
                           "Je suis là pour améliorer votre code ! 🔧")
        
        self.add_improvement_chat_message("🤖 Assistant Amélioration", response)
    
    def show_file_improvement_details(self, filename, file_values):
        """Affiche les détails d'amélioration pour un fichier"""
        detail_window = tk.Toplevel(self.root)
        detail_window.title(f"LazyRepo - Amélioration de {filename}")
        detail_window.geometry("800x600")
        
        # En-tête
        header_frame = ttk.Frame(detail_window)
        header_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(header_frame, text=f"🔧 Analyse d'amélioration - {filename}", 
                 font=("Arial", 14, "bold")).pack(anchor="w")
        ttk.Label(header_frame, text=f"Type: {file_values[1]} | Taille: {file_values[2]} | Statut: {file_values[4]}", 
                 foreground="gray").pack(anchor="w")
        
        # Notebook pour organiser les analyses
        analysis_notebook = ttk.Notebook(detail_window)
        analysis_notebook.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        # Onglet 1: Problèmes détectés
        problems_frame = ttk.Frame(analysis_notebook)
        analysis_notebook.add(problems_frame, text="🐛 Problèmes")
        
        problems_text = tk.Text(problems_frame, wrap=tk.WORD, font=("Consolas", 9))
        problems_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        problems_content = """🐛 PROBLÈMES DÉTECTÉS

Ligne 23: Variable 'unused_var' déclarée mais jamais utilisée
    Suggestion: Supprimer la variable ou l'utiliser

Ligne 45: Exception non gérée dans la fonction process_data()
    Suggestion: Ajouter un try-catch block

Ligne 67: Condition 'if True:' toujours vraie
    Suggestion: Vérifier la logique conditionnelle

Ligne 89: Import 'os' redondant (déjà importé ligne 3)
    Suggestion: Supprimer l'import dupliqué"""
        
        problems_text.insert("1.0", problems_content)
        problems_text.config(state="disabled")
        
        # Onglet 2: Optimisations
        optimizations_frame = ttk.Frame(analysis_notebook)
        analysis_notebook.add(optimizations_frame, text="⚡ Optimisations")
        
        opt_text = tk.Text(optimizations_frame, wrap=tk.WORD, font=("Consolas", 9))
        opt_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        opt_content = """⚡ OPTIMISATIONS SUGGÉRÉES

Performance:
- Ligne 15: Utiliser list comprehension au lieu de loop
  Avant: result = []
         for item in data:
             result.append(process(item))
  Après:  result = [process(item) for item in data]

- Ligne 34: Mettre en cache le résultat de calculate_heavy()
  Impact: -50% de temps d'exécution

Mémoire:
- Ligne 56: Utiliser un générateur pour large_dataset
  Impact: -80% d'utilisation mémoire"""
        
        opt_text.insert("1.0", opt_content)
        opt_text.config(state="disabled")
        
        # Onglet 3: Sécurité
        security_frame = ttk.Frame(analysis_notebook)
        analysis_notebook.add(security_frame, text="🔒 Sécurité")
        
        sec_text = tk.Text(security_frame, wrap=tk.WORD, font=("Consolas", 9))
        sec_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        sec_content = """🔒 ANALYSE DE SÉCURITÉ

CRITIQUE:
- Ligne 12: Clé API exposée en dur
  API_KEY = "sk-1234567890abcdef"
  Solution: Utiliser une variable d'environnement

- Ligne 28: Mot de passe en clair
  PASSWORD = "admin123"
  Solution: Hacher le mot de passe

AVERTISSEMENT:
- Ligne 45: Input utilisateur non validé
  Solution: Ajouter une validation des entrées

- Ligne 62: Connexion SQL sans paramètres
  Solution: Utiliser des requêtes préparées"""
        
        sec_text.insert("1.0", sec_content)
        sec_text.config(state="disabled")
        
        # Boutons d'action
        buttons_frame = ttk.Frame(detail_window)
        buttons_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        ttk.Button(buttons_frame, text="🔧 Appliquer toutes les corrections", 
                  command=lambda: self.apply_all_improvements(filename)).pack(side="left", padx=(0, 10))
        ttk.Button(buttons_frame, text="💾 Exporter le rapport", 
                  command=lambda: self.export_improvement_report(filename)).pack(side="left", padx=(0, 10))
        ttk.Button(buttons_frame, text="❌ Fermer", 
                  command=detail_window.destroy).pack(side="right")
    
    def apply_all_improvements(self, filename):
        """Applique toutes les améliorations suggérées"""
        messagebox.showinfo("Améliorations", 
                           f"🔧 Application des améliorations pour {filename}...\n\n"
                           f"✅ 4 problèmes corrigés\n"
                           f"⚡ 3 optimisations appliquées\n"
                           f"🔒 2 problèmes de sécurité résolus\n\n"
                           f"Le fichier a été sauvegardé avec les améliorations.")
        
        # Ajouter à l'historique
        timestamp = datetime.datetime.now().strftime("%H:%M")
        modification_entry = f"[{timestamp}] ✅ Améliorations appliquées à {filename}"
        
        if self.modifications_listbox.size() == 1 and "Aucune modification" in self.modifications_listbox.get(0):
            self.modifications_listbox.delete(0)
            self.modifications_listbox.config(foreground="black")
        
        self.modifications_listbox.insert(0, modification_entry)
    
    def export_improvement_report(self, filename):
        """Exporte le rapport d'amélioration"""
        messagebox.showinfo("Export", 
                           f"📄 Rapport d'amélioration exporté !\n\n"
                           f"Fichier: improvement_report_{filename}.pdf\n"
                           f"Location: ./reports/\n\n"
                           f"Le rapport contient toutes les analyses détaillées.")
    
    def clear_modifications_history(self):
        """Vide l'historique des modifications"""
        response = messagebox.askyesno("Vider l'historique", 
                                      "Êtes-vous sûr de vouloir vider l'historique des modifications ?\n\n"
                                      "Cette action est irréversible.")
        if response:
            self.modifications_listbox.delete(0, tk.END)
            self.modifications_listbox.insert(0, "📝 Aucune modification effectuée pour le moment")
            self.modifications_listbox.config(foreground="gray")
    
    def view_modification_details(self, event=None):
        """Affiche les détails d'une modification"""
        selection = self.modifications_listbox.curselection()
        if not selection:
            return
        
        modification = self.modifications_listbox.get(selection[0])
        
        if "Aucune modification" in modification:
            return
        
        messagebox.showinfo("Détails de la modification", 
                           f"📋 Détails de la modification :\n\n"
                           f"{modification}\n\n"
                           f"Cette modification a été appliquée automatiquement.\n"
                           f"Consultez les fichiers concernés pour voir les changements.")
    
    def analyze_single_file(self, tree_item):
        """Analyse un fichier spécifique"""
        item = self.files_tree.item(tree_item)
        values = item['values']
        filename = values[0].split(' ', 1)[1] if ' ' in values[0] else values[0]
        
        messagebox.showinfo("Analyse en cours", 
                           f"🔍 Analyse approfondie de {filename}...\n\n"
                           f"Cette analyse peut prendre quelques secondes.")
        
        # Simuler l'analyse avec délai
        self.root.after(2000, lambda: self.show_file_improvement_details(filename, values))
    
    def quick_actions_for_file(self, tree_item):
        """Affiche les actions rapides pour un fichier"""
        item = self.files_tree.item(tree_item)
        values = item['values']
        filename = values[0].split(' ', 1)[1] if ' ' in values[0] else values[0]
        
        # Créer une fenêtre d'actions rapides
        actions_window = tk.Toplevel(self.root)
        actions_window.title(f"Actions rapides - {filename}")
        actions_window.geometry("400x300")
        
        ttk.Label(actions_window, text=f"⚡ Actions rapides pour {filename}", 
                 font=("Arial", 12, "bold")).pack(pady=10)
        
        # Boutons d'actions spécifiques au fichier
        actions = [
            ("📝 Ajouter des commentaires", "comments"),
            ("🔒 Sécuriser les secrets", "security"),
            ("🎨 Formater le code", "format"),
            ("🐛 Détecter les bugs", "bugs"),
            ("⚡ Optimiser", "optimize"),
            ("🧪 Générer des tests", "tests")
        ]
        
        for action_name, action_type in actions:
            ttk.Button(actions_window, text=action_name,
                      command=lambda at=action_type: self.execute_file_action(filename, at, actions_window)).pack(pady=5, padx=20, fill="x")
        
        ttk.Button(actions_window, text="❌ Fermer",
                  command=actions_window.destroy).pack(pady=10)
    
    def execute_file_action(self, filename, action_type, window):
        """Exécute une action sur un fichier spécifique"""
        window.destroy()
        
        action_names = {
            "comments": "Ajout de commentaires",
            "security": "Sécurisation",
            "format": "Formatage",
            "bugs": "Détection de bugs",
            "optimize": "Optimisation",
            "tests": "Génération de tests"
        }
        
        action_name = action_names.get(action_type, "Action")
        
        messagebox.showinfo("Action en cours", 
                           f"🔄 {action_name} pour {filename}...\n\n"
                           f"Traitement en cours...")
        
        # Simuler avec délai
        self.root.after(1500, lambda: self.complete_file_action(filename, action_name))
    
    def complete_file_action(self, filename, action_name):
        """Complète l'action sur le fichier"""
        messagebox.showinfo("Action terminée", 
                           f"✅ {action_name} terminé pour {filename} !\n\n"
                           f"Les modifications ont été appliquées.")
        
        # Ajouter à l'historique
        timestamp = datetime.datetime.now().strftime("%H:%M")
        modification_entry = f"[{timestamp}] {action_name} appliqué à {filename}"
        
        if self.modifications_listbox.size() == 1 and "Aucune modification" in self.modifications_listbox.get(0):
            self.modifications_listbox.delete(0)
            self.modifications_listbox.config(foreground="black")
        
        self.modifications_listbox.insert(0, modification_entry)
    
    def refresh_file_status(self, tree_item):
        """Actualise le statut d'un fichier"""
        item = self.files_tree.item(tree_item)
        values = list(item['values'])
        filename = values[0].split(' ', 1)[1] if ' ' in values[0] else values[0]
        
        # Simuler une mise à jour du statut
        new_statuses = ["✅ Analysé", "⚠️ Améliorable", "🔍 En cours", "🔒 Sécurité OK"]
        values[4] = random.choice(new_statuses)
        
        # Mettre à jour l'item
        self.files_tree.item(tree_item, values=values)
        
        messagebox.showinfo("Statut actualisé", 
                           f"🔄 Statut de {filename} mis à jour !\n\n"
                           f"Nouveau statut: {values[4]}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LazyRepoDemo(root)
    root.mainloop()
