# 🎯 Guía Completa de Integración con Jira

## 📋 Configuración Inicial

### 1. Obtener API Token de Jira

1. Ve a: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click en **"Create API token"**
3. Dale un nombre descriptivo (ej: "DeFi Newsletter Automation")
4. Copia el token (¡solo se muestra una vez!)
5. Pégalo en tu archivo `.env`

### 2. Configurar Variables de Entorno

Edita el archivo `.env`:

```bash
# Actualiza estos valores
JIRA_EMAIL=tu_email@ejemplo.com  # Tu email de Atlassian
JIRA_API_TOKEN=tu_token_aqui      # El token que acabas de crear
```

Las siguientes ya están configuradas:
- `JIRA_URL=https://averas-1744767979220.atlassian.net`
- `JIRA_PROJECT_KEY=DN`

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## 🚀 Uso del Script de Integración

### Crear Issues Iniciales

```bash
python scripts/jira_integration.py
```

Este script creará automáticamente:
- DN-001: Setup Beehiiv account (2 SP)
- DN-002: Research Aave protocol (5 SP)
- DN-003: Write Newsletter #1 (8 SP)
- DN-004: Test automation scripts (3 SP)
- DN-005: Create affiliate links database (2 SP)
- DN-006: Setup GitHub Actions workflow (5 SP)
- DN-007: Design newsletter template (3 SP)
- DN-008: Research DeFi protocols pipeline (3 SP)

## 📊 Workflow con Jira

### Trabajar en un Issue

1. **Crear branch:**
```bash
git checkout -b feature/DN-001-setup-beehiiv
```

2. **Hacer commits con smart commits:**
```bash
# Comentar progreso
git commit -m "DN-001 #comment Configuración inicial completada"

# Logear tiempo trabajado
git commit -m "DN-001 #time 1h 30m #comment Investigación de Beehiiv API"

# Cerrar issue
git commit -m "DN-001 #close Setup de Beehiiv completado exitosamente"
```

### Smart Commits Disponibles

| Comando | Ejemplo | Efecto |
|---------|---------|--------|
| `#comment` | `DN-001 #comment Working on this` | Añade comentario |
| `#close` | `DN-001 #close Task completed` | Cierra el issue |
| `#time` | `DN-001 #time 2h 30m` | Registra tiempo |
| `#done` | `DN-001 #done Ready for review` | Mueve a Done |

### Consultar Status

Directamente en Jira:
🔗 https://averas-1744767979220.atlassian.net/jira/software/projects/DN/boards/133

## 🏷️ Labels del Proyecto

Usa estos labels para categorizar issues:

- `newsletter` - Creación de contenido
- `automation` - Scripts y automatización
- `monetization` - Afiliados y monetización
- `learning` - Investigación DeFi
- `bug` - Errores
- `enhancement` - Mejoras
- `setup` - Configuración inicial
- `testing` - Pruebas
- `devops` - CI/CD y deployment
- `design` - Diseño y templates
- `data` - Manejo de datos
- `research` - Investigación
- `planning` - Planificación

## 📈 Epics Sugeridos

Organiza tus issues en estos epics:

1. **EPIC-001: Content Production**
   - Creación de newsletters
   - Investigación de protocolos
   - Templates y diseño

2. **EPIC-002: Automation Infrastructure**
   - Scripts Python
   - GitHub Actions
   - Integraciones API

3. **EPIC-003: Monetization Strategy**
   - Enlaces de afiliados
   - Búsqueda de sponsors
   - Productos digitales

4. **EPIC-004: DeFi Learning Journey**
   - Investigación de protocolos
   - Documentación técnica
   - Glosario y notas

5. **EPIC-005: Audience Growth**
   - SEO y distribución
   - Social media
   - Partnerships

## 🔧 Troubleshooting

### Error: "Authentication failed"
- Verifica que `JIRA_EMAIL` sea correcto
- Asegúrate que el API token sea válido
- Comprueba que no haya espacios extra en `.env`

### Error: "Project not found"
- Verifica que `JIRA_PROJECT_KEY=DN` sea correcto
- Asegúrate de tener acceso al proyecto

### Los issues no se crean
- Revisa los permisos de tu cuenta en Jira
- Comprueba que el proyecto permita crear issues vía API

## 🎨 Personalización

### Añadir Más Issues Iniciales

Edita `scripts/jira_integration.py` y añade más items al array `issues`:

```python
{
    "summary": "Tu nueva tarea",
    "description": "Descripción detallada de la tarea",
    "story_points": 3,
    "labels": ["newsletter", "content"]
}
```

### Cambiar Story Points

Jira requiere configurar el campo de story points. Si quieres habilitarlo:

1. Ve a Project Settings → Custom Fields
2. Encuentra el ID del campo "Story Points"
3. Actualiza en el script: `customfield_XXXXX`

## 📚 Recursos Adicionales

- [Jira REST API Docs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Smart Commits Reference](https://support.atlassian.com/bitbucket-cloud/docs/use-smart-commits/)
- [Python Jira Library](https://jira.readthedocs.io/)

---

**¿Necesitas ayuda?** Abre un issue en el repo o consulta la documentación oficial de Jira.
