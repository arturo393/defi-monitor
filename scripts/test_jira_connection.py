#!/usr/bin/env python3
"""
Script para verificar la conexión con Jira y diagnosticar problemas.
"""

import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

console = Console()

# Cargar variables de entorno
load_dotenv()

JIRA_URL = os.getenv('JIRA_URL')
JIRA_EMAIL = os.getenv('JIRA_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')
PROJECT_KEY = os.getenv('JIRA_PROJECT_KEY', 'DN')

def test_connection():
    """Prueba la conexión básica con Jira."""
    console.print("\n[bold cyan]🔍 Verificando conexión con Jira...[/bold cyan]\n")
    
    if not all([JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
        console.print("[red]❌ Faltan variables de entorno[/red]")
        return False
    
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {"Accept": "application/json"}
    
    # Test 1: Autenticación
    console.print("1. Probando autenticación...")
    try:
        response = requests.get(
            f"{JIRA_URL}/rest/api/3/myself",
            headers=headers,
            auth=auth
        )
        response.raise_for_status()
        user_data = response.json()
        console.print(f"   [green]✅ Autenticado como: {user_data.get('displayName')}[/green]")
        console.print(f"   [dim]Email: {user_data.get('emailAddress')}[/dim]")
    except requests.exceptions.RequestException as e:
        console.print(f"   [red]❌ Error de autenticación: {e}[/red]")
        return False
    
    # Test 2: Acceso al proyecto
    console.print("\n2. Verificando acceso al proyecto...")
    try:
        response = requests.get(
            f"{JIRA_URL}/rest/api/3/project/{PROJECT_KEY}",
            headers=headers,
            auth=auth
        )
        response.raise_for_status()
        project_data = response.json()
        console.print(f"   [green]✅ Proyecto encontrado: {project_data.get('name')}[/green]")
        console.print(f"   [dim]Key: {project_data.get('key')}[/dim]")
    except requests.exceptions.RequestException as e:
        console.print(f"   [red]❌ No se puede acceder al proyecto: {e}[/red]")
        if hasattr(e.response, 'text'):
            console.print(f"   [dim]Detalle: {e.response.text}[/dim]")
        return False
    
    # Test 3: Permisos de creación
    console.print("\n3. Verificando permisos...")
    try:
        response = requests.get(
            f"{JIRA_URL}/rest/api/3/mypermissions?projectKey={PROJECT_KEY}",
            headers=headers,
            auth=auth
        )
        response.raise_for_status()
        perms = response.json()
        
        can_create = perms.get('permissions', {}).get('CREATE_ISSUES', {}).get('havePermission', False)
        
        if can_create:
            console.print(f"   [green]✅ Tienes permiso para crear issues[/green]")
        else:
            console.print(f"   [yellow]⚠️  NO tienes permiso para crear issues[/yellow]")
            console.print(f"   [dim]Solicita permisos al administrador del proyecto[/dim]")
            return False
            
    except requests.exceptions.RequestException as e:
        console.print(f"   [yellow]⚠️  No se pueden verificar permisos: {e}[/yellow]")
    
    # Test 4: Listar issue types disponibles
    console.print("\n4. Tipos de issues disponibles...")
    try:
        response = requests.get(
            f"{JIRA_URL}/rest/api/3/issue/createmeta?projectKeys={PROJECT_KEY}",
            headers=headers,
            auth=auth
        )
        response.raise_for_status()
        meta = response.json()
        
        if meta.get('projects'):
            issue_types = meta['projects'][0].get('issuetypes', [])
            table = Table(title="Issue Types")
            table.add_column("Tipo", style="cyan")
            table.add_column("ID", style="dim")
            
            for it in issue_types:
                table.add_row(it.get('name'), str(it.get('id')))
            
            console.print(table)
        else:
            console.print(f"   [yellow]⚠️  No se encontraron tipos de issue[/yellow]")
            
    except requests.exceptions.RequestException as e:
        console.print(f"   [yellow]⚠️  No se pueden listar tipos de issue: {e}[/yellow]")
    
    # Test 5: Listar issues existentes
    console.print("\n5. Issues existentes en el proyecto...")
    try:
        response = requests.get(
            f"{JIRA_URL}/rest/api/3/search?jql=project={PROJECT_KEY}&maxResults=10",
            headers=headers,
            auth=auth
        )
        response.raise_for_status()
        search_results = response.json()
        
        total = search_results.get('total', 0)
        issues = search_results.get('issues', [])
        
        if total > 0:
            console.print(f"   [green]✅ Encontrados {total} issues[/green]")
            table = Table(title="Últimos Issues")
            table.add_column("Key", style="cyan")
            table.add_column("Summary", style="white")
            table.add_column("Status", style="yellow")
            
            for issue in issues[:5]:
                table.add_row(
                    issue.get('key'),
                    issue['fields'].get('summary', 'N/A'),
                    issue['fields'].get('status', {}).get('name', 'N/A')
                )
            
            console.print(table)
        else:
            console.print(f"   [dim]No hay issues en el proyecto todavía[/dim]")
            
    except requests.exceptions.RequestException as e:
        console.print(f"   [yellow]⚠️  No se pueden listar issues: {e}[/yellow]")
    
    console.print("\n[bold green]✅ Diagnóstico completado[/bold green]\n")
    return True

def main():
    """Función principal."""
    console.print("\n[bold]🔧 Diagnóstico de Conexión Jira[/bold]")
    
    if test_connection():
        console.print("[green]Todo parece estar en orden. Puedes crear issues.[/green]")
    else:
        console.print("\n[yellow]⚠️  Hay problemas de configuración:[/yellow]")
        console.print("\n[bold]Posibles soluciones:[/bold]")
        console.print("1. Verifica que el API token sea correcto")
        console.print("2. Asegúrate de usar el email correcto de Atlassian")
        console.print("3. Solicita permisos de 'Create Issues' al admin del proyecto")
        console.print("4. Verifica que el proyecto 'DN' exista y esté accesible")
        console.print("\n[dim]Para más ayuda, consulta: docs/JIRA-INTEGRATION.md[/dim]")

if __name__ == "__main__":
    main()
