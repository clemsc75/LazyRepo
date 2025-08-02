<div align="center">

<!-- Vous pouvez ajouter un logo ici -->
<!-- <img src="URL_DE_VOTRE_LOGO" alt="LazyRepo Logo" width="150"/> -->

# LazyRepo

**Automatisez la documentation et l'amélioration de vos projets avec la puissance de l'IA et Crew AI. Une solution multi-agents pour des dépôts professionnels.**

</div>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python Version"></a>
  <a href="#"><img src="https://img.shields.io/badge/docker-ready-2496ED.svg" alt="Docker Ready"></a>
  <a href="#"><img src="https://img.shields.io/badge/crew%20ai-powered-FF6B6B.svg" alt="Crew AI Powered"></a>
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/status-en%20d%C3%A9veloppement-orange.svg" alt="Project Status"></a>
</p>

---

## 📖 Table des Matières

1. [**🎯 Vue d'ensemble**](#-vue-densemble)
2. [**🏗️ Architecture**](#️-architecture) 
3. [**✨ Fonctionnalités**](#-fonctionnalités)
4. [**🚀 Installation et Utilisation**](#-installation-et-utilisation)
5. [**⚙️ Configuration**](#️-configuration)
6. [**🐳 Utilisation avec Docker**](#-utilisation-avec-docker)
7. [**🛠️ Technologies**](#️-technologies)
8. [**📄 Licence**](#-licence)

---

## 🎯 Vue d'ensemble

**LazyRepo** est une solution d'automatisation intelligente qui exploite **Crew AI** pour transformer la documentation et l'amélioration de projets logiciels. Grâce à une équipe d'agents IA spécialisés, LazyRepo analyse vos dépôts et génère automatiquement une documentation professionnelle, améliore la qualité du code et assure la sécurité.

### 🎯 Objectifs
- **Éliminer la charge mentale** liée à la documentation technique
- **Standardiser les processus** de développement dans les équipes
- **Améliorer la qualité** et la sécurité des projets
- **Faciliter la contribution** open source

---

## 🏗️ Architecture

LazyRepo utilise une architecture modulaire basée sur **Crew AI** avec des agents spécialisés organisés en équipes (crews) thématiques.

### Structure du Projet *(Structure évolutive)*

```
LazyRepo/
├── main.py                          # Point d'entrée principal
├── config/                          # Configuration globale
│   ├── agents_config.yaml           # Configuration des agents Crew AI
│   └── languages_config.yaml       # Paramètres par langage
├── src/
│   ├── crews/                       # Équipes d'agents spécialisées
│   │   ├── documentation_crew.py    # Équipe documentation
│   │   ├── code_improvement_crew.py # Équipe amélioration code
│   │   ├── security_crew.py         # Équipe sécurité
│   │   └── social_content_crew.py   # Équipe contenu social
│   ├── agents/                      # Agents individuels
│   │   ├── readme_agent.py          # Spécialiste README
│   │   ├── security_agent.py        # Expert sécurité
│   │   └── language_specialists/    # Agents par langage
│   ├── tasks/                       # Définition des tâches
│   ├── tools/                       # Outils d'analyse
│   └── utils/                       # Utilitaires
├── templates/                       # Modèles de génération
├── output/                          # Fichiers générés
└── requirements.txt
```

### Agents Spécialisés
- **Agents par langage** : Python, JavaScript, Java, C#, Go...
- **Agents thématiques** : Documentation, Sécurité, Amélioration
- **Agent de feedback** : Interaction et amélioration continue

---

## ✨ Fonctionnalités

LazyRepo organise ses fonctionnalités autour d'équipes d'agents (crews) spécialisées, chacune dédiée à un aspect spécifique de l'amélioration de projet.

### 📚 Documentation Crew
| Fonctionnalité | Description |
|----------------|-------------|
| **README.md automatique** | Génération de documentation complète avec analyse du code source |
| **Documentation API** | Création de docs techniques pour les API et modules |
| **Guides d'installation** | Instructions détaillées par environnement et plateforme |

### 🔧 Code Improvement Crew
| Fonctionnalité | Description |
|----------------|-------------|
| **Amélioration du code** | Ajout de commentaires et suggestions d'optimisation |
| **Standards de qualité** | Application des conventions (PEP 8, ESLint, etc.) |
| **Refactoring intelligent** | Suggestions d'amélioration structurelle |

### 🔒 Security Crew
| Fonctionnalité | Description |
|----------------|-------------|
| **Scan de sécurité** | Détection de vulnérabilités et informations sensibles |
| **Gestion des secrets** | Migration vers `.env` et variables d'environnement |
| **Configuration sécurisée** | Génération de `.gitignore` et fichiers de sécurité |

### 📱 Social Content Crew
| Fonctionnalité | Description |
|----------------|-------------|
| **Posts LinkedIn** | Contenu professionnel pour présenter le projet |
| **Descriptions GitHub** | Optimisation des descriptions de dépôt |
| **Documentation marketing** | Contenu promotionnel et cas d'usage |

---

## 🚀 Installation et Utilisation

### Installation Locale

```bash
# Cloner le repository
git clone https://github.com/clemsc75/LazyRepo.git
cd LazyRepo

# Créer un environnement virtuel
python -m venv venv_LazyRepo
source venv_LazyRepo/bin/activate  # Linux/Mac
# ou
venv_LazyRepo\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'analyse
python main.py /chemin/vers/votre/projet
```

---

## ⚙️ Configuration

LazyRepo utilise des fichiers **YAML** pour une configuration flexible et lisible.

### Configuration des Agents (`config/agents_config.yaml`)

```yaml
agents:
  readme_agent:
    role: "Documentation Specialist"
    goal: "Créer des README complets et informatifs"
    backstory: "Expert en documentation technique avec 10 ans d'expérience"
    tools:
      - file_analyzer
      - git_analyzer
    max_iter: 5
    verbose: true

  security_agent:
    role: "Security Expert"
    goal: "Identifier et résoudre les vulnérabilités"
    backstory: "Spécialiste en cybersécurité et bonnes pratiques"
    tools:
      - security_scanner
      - dependency_analyzer
```

### Configuration par Langage (`config/languages_config.yaml`)

```yaml
languages:
  python:
    conventions: "PEP 8"
    common_frameworks: ["Django", "Flask", "FastAPI"]
    security_patterns: ["secrets", "env_vars"]
    readme_template: "python_readme.md"
    
  javascript:
    conventions: "ESLint Standard"
    common_frameworks: ["React", "Vue", "Express"]
    security_patterns: ["api_keys", "tokens"]
    readme_template: "javascript_readme.md"
```

### Variables d'Environnement

#### Développement (`.env.dev`)
```bash
# IA Locale - LM Studio pour développement
AI_PROVIDER=lmstudio
LMSTUDIO_URL=http://localhost:1234
LMSTUDIO_MODEL=llama2

# Configuration
DEFAULT_LANGUAGE=python
OUTPUT_FORMAT=markdown
VERBOSE_MODE=true
DEBUG=true
```

#### Production (`.env.prod`)
```bash
# IA Locale - Ollama pour production
AI_PROVIDER=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Configuration
DEFAULT_LANGUAGE=python
OUTPUT_FORMAT=markdown
VERBOSE_MODE=false
DEBUG=false
```

---

## 🐳 Utilisation avec Docker

LazyRepo est conçu pour fonctionner parfaitement dans un environnement conteneurisé, offrant portabilité et facilité de déploiement avec plusieurs interfaces utilisateur.

### 🚀 Interfaces Disponibles

LazyRepo propose **trois modes d'utilisation** via Docker pour s'adapter à tous les besoins :

#### 💻 Interface en Ligne de Commande (CLI)
```bash
# Construire l'image
docker build -t lazyrepo .

# Analyser un projet en mode CLI
docker run -v /chemin/vers/votre/projet:/app/input \
           -v ./output:/app/output \
           --env-file .env \
           lazyrepo --mode cli /app/input
```

#### 🖥️ Interface Graphique (GUI)
```bash
# Lancer l'interface graphique (nécessite X11 forwarding sur Linux/Mac)
docker run -v /chemin/vers/votre/projet:/app/input \
           -v ./output:/app/output \
           -v /tmp/.X11-unix:/tmp/.X11-unix \
           -e DISPLAY=$DISPLAY \
           --env-file .env \
           lazyrepo --mode gui

# Sur Windows avec Docker Desktop
docker run -v /chemin/vers/votre/projet:/app/input \
           -v ./output:/app/output \
           --env-file .env \
           lazyrepo --mode gui
```

#### 🌐 Interface Web
```bash
# Lancer le service web
docker run -p 8080:8080 \
           -v /chemin/vers/votre/projet:/app/input \
           -v ./output:/app/output \
           --env-file .env \
           lazyrepo --mode web

# Accès via http://localhost:8080
# Interface web complète avec upload de projets et visualisation des résultats
```

### 🤖 Configuration IA Locale

#### Développement avec LM Studio
```bash
# Variables d'environnement pour LM Studio
docker run --env-file .env.dev \
           -e AI_PROVIDER=lmstudio \
           -e LMSTUDIO_URL=http://host.docker.internal:1234 \
           lazyrepo
```

#### Production avec Ollama
```bash
# Variables d'environnement pour Ollama
docker run --env-file .env.prod \
           -e AI_PROVIDER=ollama \
           -e OLLAMA_URL=http://host.docker.internal:11434 \
           lazyrepo
```

### 📁 Volumes Docker Recommandés

| Volume | Description | Utilisation |
|--------|-------------|-------------|
| `/app/input` | Projet à analyser | Montage du code source |
| `/app/output` | Résultats générés | Sauvegarde des fichiers créés |
| `/app/config` | Configuration personnalisée | Fichiers YAML custom |

### 🚀 Docker Compose pour Usage Simplifié

```yaml
version: '3.8'
services:
  lazyrepo-web:
    build: .
    ports:
      - "8080:8080"
    volumes:
      - ./projects:/app/input
      - ./output:/app/output
      - ./config:/app/config
    environment:
      - AI_PROVIDER=ollama
      - OLLAMA_URL=http://ollama:11434
    command: --mode web
    
  lazyrepo-cli:
    build: .
    volumes:
      - ./projects:/app/input
      - ./output:/app/output
    environment:
      - AI_PROVIDER=ollama
      - OLLAMA_URL=http://ollama:11434
    command: --mode cli /app/input
    profiles: ["cli"]
    
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
```

### ☁️ Déploiement Cloud

LazyRepo Docker est compatible avec :
- **Docker Swarm** pour le scaling horizontal
- **Kubernetes** pour l'orchestration avancée  
- **CI/CD pipelines** pour l'intégration continue

---

## 🛠️ Technologies

### Framework Principal
- **Python 3.9+** - Langage de développement
- **Crew AI** - Orchestration des agents IA multi-agents
- **LM Studio** - Modèles IA locaux pour le développement
- **Ollama** - Modèles IA locaux pour la production

### Architecture et Déploiement
- **Docker** - Conteneurisation et portabilité
- **YAML** - Configuration flexible et lisible
- **Jinja2** - Moteur de templates pour la génération

### Outils d'Analyse
- **AST** - Analyse syntaxique du code
- **GitPython** - Analyse des dépôts Git
- **Security scanners** - Détection de vulnérabilités

### Interfaces Utilisateur
- **CLI** - Interface en ligne de commande (Docker + terminal)
- **GUI** - Interface graphique intuitive (Docker + bureau)
- **REST API** - Service web accessible via navigateur (Docker + web)
- **Tkinter** - Interface native pour le développement local

---

## 📄 Licence

Ce projet est distribué sous la Licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

<div align="center">

**🚀 Transformez vos projets avec LazyRepo - L'IA au service de votre code**

[Documentation](docs/) • [Issues](https://github.com/clemsc75/LazyRepo/issues) • [Contributions](CONTRIBUTING.md)

</div>
