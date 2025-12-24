# 💼 Freelance Portfolio - Arturo

> Starter kit para freelancers: Portfolio web, templates y estrategia de negocio

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 ¿Qué es esto?

Un **portfolio profesional** y **starter kit completo** para freelancers que incluye:

- 🎨 **Portfolio web** moderno y responsive (`docs/index.html`)
- 📝 **Templates de propuestas** para proyectos
- 💼 **Catálogo de servicios** con pricing
- 📧 **Scripts de outreach** para clientes
- 📊 **Plan de negocio** 30-60-90 días

---

## 🚀 Quick Start

### 1. Ver el portfolio

```bash
# Abrir portfolio en navegador
open docs/index.html

# O servir localmente
cd docs/
python3 -m http.server 8000
# Visita: http://localhost:8000
```

### 2. Personalizar contenido

Edita el portfolio en `docs/index.html` con tu información:
- Nombre y tagline
- Proyectos realizados
- Skills y tecnologías
- Links de contacto

### 3. Usar templates

Los templates están en `/docs`:

```bash
# Ver catálogo de servicios
cat docs/SERVICES_CATALOG.md

# Ver templates de propuestas
cat docs/PROPOSAL_TEMPLATES.md

# Plan de negocio
cat docs/FREELANCE_PLAN_30-60-90.md
```

---

## 📁 Estructura del Proyecto

```
freelance-portfolio/
 docs/
   ├── index.html                    # 🎨 Portfolio web principal
   ├── PORTFOLIO.md                  # 📝 Guía para crear portfolio
   ├── SERVICES_CATALOG.md           # 💰 Servicios y precios
   ├── PROPOSAL_TEMPLATES.md         # 📄 Templates de propuestas
   ├── OUTREACH_TEMPLATES.md         # 📧 Emails para clientes
   ├── UPWORK_PROFILE.md             # 💼 Perfil Upwork/Fiverr
   ├── FREELANCE_PLAN_30-60-90.md    # 📊 Plan de negocio
   └── README_FREELANCE.md           # 📚 Guía completa freelance
 .env.example                      # ⚙️ Variables de entorno
 .gitignore                        # 🚫 Archivos ignorados
 README.md                         # 📖 Este archivo
```

---

## 🎨 Portfolio Web

El portfolio en `docs/index.html` incluye:

- **Header**: Nombre, tagline, navegación
- **Hero section**: Presentación y CTA
- **Projects**: Showcase de proyectos con demos visuales
- **Skills**: Tecnologías y herramientas
- **Contact**: Links a GitHub, LinkedIn, Email

**Features:**
- ✅ Responsive design (mobile-first)
- ✅ Dark theme moderno
- ✅ Modales interactivos para demos
- ✅ Sin dependencias (HTML/CSS puro)
- ✅ Fácil de personalizar

---

## 💼 Servicios Ofrecidos

Basado en `docs/SERVICES_CATALOG.md`:

| Servicio | Duración | Precio |
|----------|----------|--------|
| **Data Pipeline** | 2-3 semanas | $2,000-3,000 |
| **Web Scraping** | 1-2 semanas | $1,500-2,500 |
| **Dashboard Interactivo** | 2-4 semanas | $2,500-4,000 |
| **Automatización** | 1-2 semanas | $1,000-2,000 |

Ver catálogo completo en [SERVICES_CATALOG.md](docs/SERVICES_CATALOG.md)

---

## 📈 Plan de Negocio

Sigue el plan **30-60-90 días** en `docs/FREELANCE_PLAN_30-60-90.md`:

### Mes 1 (Días 1-30): Setup
- ✅ Crear portfolio
- ✅ Configurar perfiles (Upwork, Fiverr)
- ✅ Primeras propuestas

### Mes 2 (Días 31-60): Primeros Clientes
- 🎯 3-5 propuestas/día
- 🎯 1-2 clientes pequeños
- 🎯 $500-1,000 ingresos

### Mes 3 (Días 61-90): Escalamiento
- 🎯 Cliente grande ($2,000+)
- 🎯 5-10 propuestas/día
- 🎯 $2,000-3,000 ingresos

---

## 🛠️ Tech Stack

**Portfolio:**
- HTML5 + CSS3 (vanilla, sin frameworks)
- Responsive design
- Dark theme

**Servicios ofrecidos:**
- Python 3.11+ (data pipelines, automation)
- JavaScript/Node.js (web scraping, APIs)
- React/Next.js (dashboards)
- PostgreSQL/MongoDB (databases)
- AWS/GCP (cloud deployment)

---

## 📚 Documentación

- **[PORTFOLIO.md](docs/PORTFOLIO.md)** - Cómo crear un portfolio efectivo
- **[SERVICES_CATALOG.md](docs/SERVICES_CATALOG.md)** - Servicios y pricing
- **[PROPOSAL_TEMPLATES.md](docs/PROPOSAL_TEMPLATES.md)** - Templates para propuestas
- **[OUTREACH_TEMPLATES.md](docs/OUTREACH_TEMPLATES.md)** - Emails de outreach
- **[UPWORK_PROFILE.md](docs/UPWORK_PROFILE.md)** - Optimizar perfil Upwork
- **[FREELANCE_PLAN_30-60-90.md](docs/FREELANCE_PLAN_30-60-90.md)** - Plan de negocio
- **[README_FREELANCE.md](docs/README_FREELANCE.md)** - Guía completa

---

## 🚀 Deploy Portfolio

### GitHub Pages

```bash
# 1. Push a GitHub
git add -A
git commit -m "feat: Add freelance portfolio"
git push origin main

# 2. Configurar GitHub Pages
# Settings → Pages → Source: main branch → /docs
```

Tu portfolio estará en: `https://tu-usuario.github.io/repo-name/`

### Netlify

```bash
# 1. Instalar Netlify CLI
npm install -g netlify-cli

# 2. Deploy
cd docs/
netlify deploy --prod
```

---

## ✅ Checklist de Personalización

- [ ] Actualizar nombre y tagline en `index.html`
- [ ] Agregar tus proyectos con screenshots/demos
- [ ] Actualizar skills y tecnologías
- [ ] Cambiar links de contacto (GitHub, LinkedIn, Email)
- [ ] Personalizar `SERVICES_CATALOG.md` con tus precios
- [ ] Adaptar `PROPOSAL_TEMPLATES.md` a tu estilo
- [ ] Configurar `.env` con tus credenciales
- [ ] Crear perfil en Upwork/Fiverr
- [ ] Deploy portfolio en GitHub Pages

---

## 🤝 Contribuir

Este es un proyecto personal, pero las sugerencias son bienvenidas:

1. Fork el repo
2. Crea una branch (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la branch (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para más detalles

---

## 👨‍💻 Autor

**Arturo** - [GitHub](https://github.com/arturo393)

---

## 🔗 Links

- **Portfolio Live:** [Agregar URL cuando deploys]
- **Upwork:** [Agregar perfil]
- **LinkedIn:** [Agregar perfil]

---

**¿Te gusta este starter kit?** Dale una ⭐ en GitHub y úsalo para tu negocio freelance!
