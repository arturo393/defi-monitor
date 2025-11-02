# 📰 DeFi Newsletter - Proyecto Automatizado

> Newsletter automatizada sobre DeFi - Aprende estrategias mientras monetizas tu conocimiento

## 🎯 Objetivo

Crear una newsletter 100% automatizada que:
- 📚 Te ayude a aprender sobre protocolos DeFi
- 💰 Genere ingresos pasivos mediante afiliados
- 🤖 Se publique automáticamente cada semana
- 📈 Crezca tu audiencia orgánicamente

## 🛠️ Tech Stack

- **Python 3.x** - Scripts de automatización
- **DeFi Llama API** - Datos en tiempo real
- **Beehiiv** - Plataforma de newsletter
- **GitHub Actions** - Automatización CI/CD
- **Jira** - Project management

## 📁 Estructura del Proyecto

```
defi-newsletter/
├── .github/workflows/      # GitHub Actions
├── scripts/               # Scripts Python
├── content/              # Newsletters y drafts
├── data/                 # JSON con protocolos, afiliados, métricas
├── docs/                 # Documentación del proyecto
└── learning/             # Notas de investigación DeFi
```

## 🚀 Quick Start

### Setup Inicial (Primera vez)

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar setup interactivo
python scripts/setup_initial.py
```

El script de setup te guiará para:
- ✅ Crear archivo `.env`
- ✅ Configurar Jira (email + API token)
- ✅ Configurar Beehiiv (opcional)
- ✅ Crear issues iniciales en Jira

### Configuración Manual

Si prefieres configurar manualmente:

```bash
# 1. Copiar archivo de entorno
cp .env.example .env

# 2. Editar .env con tus credenciales
nano .env

# 3. Crear issues en Jira
python scripts/jira_integration.py

# 4. Probar scripts
python scripts/collect_defi_data.py
```

### 📋 Accesos Rápidos

- **Jira Board:** https://averas-1744767979220.atlassian.net/jira/software/projects/DN/boards/133
- **Obtener API Token:** https://id.atlassian.com/manage-profile/security/api-tokens

## 📊 Roadmap

Ver [docs/ROADMAP.md](docs/ROADMAP.md) para el plan completo de 6 meses.

## 💰 Monetización

- Enlaces de afiliados (Binance, Aave, etc.)
- Sponsors ($500-2000/edición)
- Productos digitales (ebooks, cursos)

## 📝 License

MIT License - Haz lo que quieras con este código

## 🤝 Contributing

Este es un proyecto personal de aprendizaje, pero las PRs son bienvenidas.

---

**Creado con ❤️ por [Arturo](https://github.com/arturo393)**
