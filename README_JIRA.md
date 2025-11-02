# 🎯 Quick Start con Jira

Tu proyecto ya está configurado con Jira. Aquí está todo lo que necesitas saber:

## 📋 Tu Board de Jira
🔗 https://averas-1744767979220.atlassian.net/jira/software/projects/DN/boards/133

## ⚡ Crear Issues Iniciales

**Opción 1: Usar el script (RECOMENDADO)**
```bash
# Primero actualiza tu email en .env
nano .env  # Cambia JIRA_EMAIL=tu_email@ejemplo.com

# Luego ejecuta el script
pip install -r requirements.txt
python scripts/jira_integration.py
```

**Opción 2: Manual en Jira**
Ve al board y crea estos issues:
- DN-001: Setup Beehiiv account (2 SP)
- DN-002: Research Aave protocol (5 SP)
- DN-003: Write Newsletter #1 (8 SP)
- DN-004: Test automation scripts (3 SP)

## 🔄 Workflow Diario

### 1. Morning (Lunes)
```bash
# Ve a Jira board
# Mueve issues a "In Progress"
# Asigna issues a ti mismo
```

### 2. Trabajar en el código
```bash
# Crea branch por issue
git checkout -b feature/DN-001-setup-beehiiv

# Haz commits con referencia al issue
git commit -m "DN-001 #comment Configuración inicial de Beehiiv"
```

### 3. Completar tarea
```bash
git commit -m "DN-001 #close Setup completado exitosamente"
git push
```

## 🎨 Labels en Jira

Crea estos labels en tu board:
- `newsletter` - Para issues de contenido
- `automation` - Para scripts y bots
- `monetization` - Para afiliados y sponsors
- `learning` - Para investigación DeFi
- `bug` - Para errores
- `enhancement` - Para mejoras

## 📊 Epics Recomendados

1. **Content Production** - Newsletters y contenido
2. **Automation** - Scripts y GitHub Actions
3. **Monetization** - Afiliados, sponsors, productos
4. **DeFi Learning** - Investigación protocolos
5. **Growth** - Marketing y crecimiento

## 💡 Smart Commits Cheat Sheet

```bash
# Comentar
git commit -m "DN-001 #comment Trabajo en progreso"

# Cerrar
git commit -m "DN-001 #close Tarea completada"

# Logear tiempo
git commit -m "DN-001 #time 2h #comment Investigación completada"

# Transicionar
git commit -m "DN-001 #done Testing finalizado"
```

## 🚀 Próximos Pasos

1. ✅ Actualiza JIRA_EMAIL en `.env`
2. ✅ Ejecuta `python scripts/jira_integration.py`
3. ✅ Ve a tu board y verifica los issues
4. ✅ Comienza a trabajar en DN-001

---

**¿Problemas?** Revisa `docs/JIRA-INTEGRATION.md` para más detalles.
