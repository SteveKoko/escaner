# Escaner de red (CLI)

Herramienta CLI en Python que usa `python-nmap` para detectar hosts activos y
realizar un escaneo basico de puertos en una red o equipo.

## Requisitos

- Python 3.13+
- uv (gestor de dependencias)
- Nmap instalado en el sistema

## Instalar uv

macOS y Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows: usa el instalador oficial de uv (ver docs)
https://docs.astral.sh/uv/getting-started/installation/

## Instalar Nmap (multiplataforma)

macOS:

```bash
brew install nmap
```

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install nmap
```

Windows:

- Descarga el instalador desde https://nmap.org/download.html
- Instala Nmap y Npcap (necesario para escaneos)

## Instalacion de dependencias (uv)

Con uv, las dependencias se leen desde `pyproject.toml`.

```bash
uv sync
```

## Uso

```bash
uv run main.py
```

Opciones del menu:

- `01` Detecta hosts activos en la red (ping scan con `-sn`)
- `02` Escaneo basico de puertos (SYN scan con `-sS`)
- `00` Salir

## Ejemplos

Escaneo de hosts activos:

```
Introduce la red objetivo: 192.168.1.0/24
```

Escaneo de puertos:

```
Introduce el equipo o la red a escanear: 192.168.1.10
```

## Notas

- El escaneo de puertos puede requerir permisos elevados segun el sistema.
- Usa esta herramienta solo en redes y equipos con autorizacion.

## Compilar ejecutable (PyInstaller con uv)

Instala dependencias de desarrollo y compila:

```bash
uv sync --group dev
uv run pyinstaller --onefile --name escaner main.py
```

Salida:

- macOS/Linux: `dist/escaner`
- Windows: `dist/escaner.exe`
