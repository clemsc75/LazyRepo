<div align="center">

<!-- Vous pouvez ajouter un logo ici -->
<!-- <img src="URL_DE_VOTRE_LOGO" alt="LazyRepo Logo" width="150"/> -->

# LazyRepo

**Automatisez la documentation de vos projets GitHub avec la puissance de l'IA. Ne rédigez plus jamais un README à la main.**

</div>

<p align="center">
  <!-- Badges : à adapter avec vos propres liens -->
  <a href="#"><img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python Version"></a>
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/status-en%20d%C3%A9veloppement-orange.svg" alt="Project Status"></a>
</p>

---

## 📖 Table des Matières

1.  [**🎯 Objectif**](#-objectif)
2.  [**✨ Fonctionnalités Principales**](#-fonctionnalités-principales)
3.  [**🛠️ Technologies Utilisées**](#️-technologies-utilisées)
5.  [**📄 Licence**](#-licence)

---

## 🎯 Objectif

**LazyRepo** est un outil en ligne de commande qui exploite l'IA pour éliminer la charge mentale et la répétitivité liées à la documentation de projet. En analysant intelligemment votre base de code, il génère automatiquement des `README.md` clairs, des commentaires pertinents et des fichiers de configuration essentiels.

Notre mission est de permettre aux :

-   **Développeurs** de maintenir des dépôts professionnels sans effort.
-   **Équipes** de standardiser leurs processus de documentation.
-   **Contributeurs Open Source** de présenter leurs projets de manière impactante.

---

## ✨ Fonctionnalités Principales

LazyRepo s'appuie sur une équipe d'agents autonomes gérés par **Crew AI** pour offrir une suite complète de fonctionnalités.

### Phase 1 : Documentation et Amélioration du Code

| Fonctionnalité                | Description                                                                                                                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Génération de `README.md`**   | Analyse le code source pour créer un `README.md` structuré, incluant la description du projet, les fonctionnalités, des exemples d'utilisation et les dépendances.                                  |
| **Amélioration du Code**        | Ajoute des commentaires explicatifs, suggère des noms de variables plus clairs et aide à respecter les standards de code (PEP 8 pour Python) pour une lisibilité maximale.                           |
| **Création de Contenu Social**  | Génère des publications prêtes à l'emploi pour les réseaux sociaux (LinkedIn, etc.) afin de promouvoir votre projet, incluant un titre, une description, un lien et des hashtags pertinents.        |
| **Boucle de Feedback**        | Un agent interactif vous demande votre avis sur les documents générés pour affiner les résultats et améliorer continuellement les performances de l'IA.                                                |

### Phase 2 : Sécurité et Finalisation

| Fonctionnalité                     | Description                                                                                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Analyse de Sécurité**            | Un agent spécialisé scanne le code à la recherche d'informations sensibles (clés d'API, mots de passe).                                                                                             |
| **Gestion des Secrets**            | Isole automatiquement les informations sensibles dans un fichier `.env` (ajouté au `.gitignore`) et met à jour le code pour charger ces variables d'environnement de manière sécurisée.            |
| **Génération de Fichiers Clés**    | Crée automatiquement les fichiers essentiels à tout projet Python : `requirements.txt` pour les dépendances et un `.gitignore` complet et adapté.                                                  |

---

## 🛠️ Technologies Utilisées

-   **Langage principal** : Python
-   **Framework IA** : Crew AI
-   **Interface Utilisateur (Phase de test)** : Tkinter, Colorama

---

## 📄 Licence

Ce projet est distribué sous la Licence MIT. Voir le fichier `LICENSE` pour plus de détails.
