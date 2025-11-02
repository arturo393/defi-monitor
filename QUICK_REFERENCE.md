# 🚀 Quick Reference - DeFi Newsletter

## ⚡ Comandos Más Usados

### Setup y Configuración

```bash
# Setup inicial completo (primera vez)
python3 scripts/setup_initial.py

# Solo actualizar JIRA API token
python3 scripts/update_jira_token.py

# Verificar conexión con Jira
python3 scripts/test_jira_connection.py

# Crear issues en Jira
python3 scripts/jira_integration.py
```

### Desarrollo

```bash
# Recopilar datos DeFi
python3 scripts/collect_defi_data.py

# Generar newsletter
python3 scripts/generate_newsletter.py

# Enviar a Beehiiv
python3 scripts/send_to_beehiiv.py
```

### Git Workflow

```bash
# Crear branch para un issue
git checkout -b feature/DN-001-setup-beehiiv

# Commit con smart commits
git commit -m "DN-001 #comment Trabajo en progreso"
git commit -m "DN-001 #time 2h #comment Investigación completada"
git commit -m "DN-001 #close Tarea completada"

# Push
git push origin feature/DN-001-setup-beehiiv
```

## 📋 Enlaces Rápidos

| Recurso | URL |
|---------|-----|
| Jira Board | https://averas-1744767979220.atlassian.net/jira/software/projects/DN/boards/133 |
| API Tokens | https://id.atlassian.com/manage-profile/security/api-tokens |
| DeFi Llama | https://defillama.com |
| Beehiiv | https://beehiiv.com |

## 🎯 Issues de Jira

| Key | Tarea | Story Points | Labels |
|-----|-------|--------------|--------|
| DN-001 | Setup Beehiiv account | 2 | automation, setup |
| DN-002 | Research Aave protocol | 5 | learning, research |
| DN-003 | Write Newsletter #1 | 8 | newsletter, content |
| DN-004 | Test automation scripts | 3 | automation, testing |
| DN-005 | Create affiliate links | 2 | monetization, data |
| DN-006 | Setup GitHub Actions | 5 | automation, devops |
| DN-007 | Design newsletter template | 3 | newsletter, design |
| DN-008 | Research DeFi protocols | 3 | learning, planning |

## 📚 Estructura de Archivos

```
defi-newsletter/
├── scripts/           # 🤖 Scripts de automatización
│   ├── setup_initial.py          # Setup guiado
│   ├── update_jira_token.py      # Actualizar token Jira
│   ├── test_jira_connection.py   # Test conexión Jira
│   ├── jira_integration.py       # Crear issues
│   ├── collect_defi_data.py      # Datos DeFi
│   ├── generate_newsletter.py    # Generar newsletter
│   └── send_to_beehiiv.py        # Enviar a Beehiiv
│
├── content/           # ✍️ Contenido de newsletters
│   ├── drafts/                   # Borradores
│   └── newsletters/              # Publicadas
│       └── template.md           # Plantilla
│
├── data/             # 📊 Datos y configuración
│   └── (JSON con protocolos, afiliados, etc.)
│
├── docs/             # 📖 Documentación
│   ├── JIRA-INTEGRATION.md      # Guía Jira
│   ├── ROADMAP.md               # Plan 6 meses
│   ├── MONETIZATION.md          # Monetización
│   └── CONTENT-IDEAS.md         # Ideas
│
├── learning/         # 📚 Investigación DeFi
│   ├── aave-notes.md            # Notas Aave
│   └── defi-glossary.md         # Glosario
│
├── .env              # 🔑 Credenciales (NO commitear)
├── requirements.txt  # 📦 Dependencias Python
├── README.md         # 📘 Documentación principal
└── SETUP_STATUS.md   # ✅ Estado del setup
```

## 🔧 Troubleshooting Rápido

### Problema: "Module not found"
```bash
pip3 install -r requirements.txt
```

### Problema: "JIRA API Token inválido"
```bash
python3 scripts/update_jira_token.py
```

### Problema: ".env no encontrado"
```bash
cp .env.example .env
nano .env
```

### Problema: "No permission to create issues"
- Verifica el API token en .env
- Asegúrate de tener permisos en el proyecto DN
- Ejecuta: `python3 scripts/test_jira_connection.py`

## 🎨 Smart Commits Cheat Sheet

| Comando | Uso | Ejemplo |
|---------|-----|---------|
| `#comment` | Añadir comentario | `DN-001 #comment Progreso del 50%` |
| `#time` | Registrar tiempo | `DN-001 #time 2h 30m` |
| `#close` | Cerrar issue | `DN-001 #close Completado` |
| `#done` | Marcar como done | `DN-001 #done Listo para review` |

## 📅 Workflow Semanal

### Lunes
- [ ] Recopilar datos DeFi
- [ ] Generar newsletter
- [ ] Publicar a las 9am

### Martes-Viernes
- [ ] Investigar protocolos
- [ ] Escribir contenido
- [ ] Mejorar automatización

### Fin de Semana
- [ ] Revisar métricas
- [ ] Planear siguiente semana
- [ ] Aprender nuevos protocolos

## 🎯 Objetivos por Mes

| Mes | Objetivo | Métricas |
|-----|----------|----------|
| 1 | Setup + Primera newsletter | 50 subs |
| 2 | 4 newsletters publicadas | 200 subs |
| 3 | Automatización completa | 500 subs |
| 4 | Primeros afiliados | $500/mes |
| 5 | Optimización y crecimiento | 2,000 subs |
| 6 | Sponsors y productos | $3,000/mes |

## 💡 Tips

- 🔥 Publica consistentemente (mismo día/hora)
- 📊 Analiza qué contenido funciona mejor
- 🤝 Colabora con otros creadores DeFi
- 💰 No spamees afiliados, enfócate en valor
- 📚 Documenta todo lo que aprendas
- 🚀 Automatiza lo repetitivo

## 📞 Ayuda

- 📖 Docs completas: `docs/`
- 🐛 Issues: GitHub Issues
- 💬 Preguntas: README.md tiene todo

---

**Última actualización:** 2 nov 2025  
**Versión:** 1.0  
**Autor:** [@arturo393](https://github.com/arturo393)
