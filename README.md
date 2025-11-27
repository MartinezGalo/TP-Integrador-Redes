# Trabajo Práctico Integrador - Redes de Computadoras

**Universidad Nacional de La Matanza** **Departamento de Ingeniería e Investigaciones Tecnológicas** **Cátedra:** Redes de Computadoras (3643)  
**Año:** 2025 - 2° Cuatrimestre

---

## 📋 Descripción del Proyecto

Este repositorio contiene el diseño, implementación y validación de una arquitectura de red corporativa jerárquica y convergente. [cite_start]El objetivo principal fue interconectar diversos departamentos organizacionales (Ingeniería, Economía, RR.HH., Deportes, Decanato y Salud) mediante una infraestructura **Dual-Stack (IPv4 e IPv6)**, asegurando alta disponibilidad y escalabilidad[cite: 42, 43].

[cite_start]El proyecto va más allá de la configuración tradicional, integrando conceptos de **automatización y programabilidad** mediante el uso de un Network Controller, API REST y scripts de Python[cite: 322, 323].

## 👥 Integrantes - Grupo 8

* **Brizzolara, César** - 34728140
* **Testa, Tomas** - 38687789
* **Fernández, Mario** - 39912991
* **Yturre, Gabriel Agustin** - 44940038
* **Martínez, Galo** - 43094675
[cite_start][cite: 35-38]

## 🛠️ Tecnologías y Herramientas

* **Simulación:** Cisco Packet Tracer.
* **Hardware Simulado:** Routers ISR 4331, Switches Catalyst 3650 (L3) y 2960 (L2).
* **Protocolos:** OSPFv2, OSPFv3, IPv4, IPv6, DHCP, DNS, NTP.
* **Automatización:** Cisco Network Controller (SDN).
* **Testing & Scripting:** Postman (API Testing), Python (Librería `requests`).

## 🏗️ Topología de Red

La arquitectura de red se diseñó siguiendo un modelo jerárquico:

* [cite_start]**Borde (Edge):** Router `R1` gestiona la conexión hacia el ISP simulado y la salida a Internet[cite: 45].
* [cite_start]**Núcleo (Core):** Routers `R2` y `R3` interconectan las distintas zonas mediante enlaces seriales redundantes[cite: 46].
* [cite_start]**Distribución (Capa 3):** Switches `SW3`, `SW4`, `SW5` actúan como gateways para sus respectivas VLANs utilizando puertos enrutados[cite: 47].
* [cite_start]**Acceso (Capa 2):** Switches `SW1`, `SW2` conectados a `R3` utilizando la técnica **Router-on-a-Stick**[cite: 48].

### Segmentación VLAN

| VLAN | Departamento | Subred IPv4 | Subred IPv6 | Ubicación |
| :--- | :--- | :--- | :--- | :--- |
| 10 | DEPORTES | 192.168.10.0/24 | 2001:db8:0:10::/64 | SW1 (vía R3) |
| 20 | DECANATO | 192.168.20.0/24 | 2001:db8:0:20::/64 | SW1 (vía R3) |
| 30 | SALUD | 192.168.30.0/24 | 2001:db8:0:30::/64 | SW2 (vía R3) |
| 40 | ECONOMIA | 192.168.40.0/24 | 2001:db8:0:40::/64 | SW3 |
| 50 | DPTO. ING | 192.168.50.0/24 | 2001:db8:0:50::/64 | SW4 |
| 60 | SERVERS | 192.168.60.0/24 | 2001:db8:0:60::/64 | SW4 |
| 70 | RR.HH | 192.168.70.0/24 | 2001:db8:0:70::/64 | SW5 |
| 99 | NC (Gestión)| 192.168.99.0/24 | 2001:db8:0:99::/64 | SW3 |
[cite_start][cite: 69]

## ⚙️ Servicios e Infraestructura

* [cite_start]**Enrutamiento:** Dinámico mediante **OSPF** (Área 0) con redistribución de ruta por defecto desde el borde[cite: 71, 80].
* [cite_start]**DHCP:** Configurado en `R3` (Deportes, Decanato, Salud) y `SW5` (RR.HH)[cite: 51, 52].
* **Servidores (VLAN 60):**
    * **DNS:** 192.168.60.1
    * [cite_start]**NTP:** 192.168.60.2 [cite: 55, 56]
* [cite_start]**ISP Simulado:** Servicios HTTP y FTP públicos accesibles mediante NAT/Enrutamiento[cite: 62].

## 🤖 Automatización y API

Se implementó un **Network Controller** en la VLAN 99 para la gestión centralizada. Se realizaron pruebas de concepto (PoC) utilizando la API Northbound del controlador.

### Postman
Se validaron operaciones CRUD completas:
* **POST:** `addTicket`, `addCliCredential`, `insertDiscovery` (Descubrimiento de red).
* **GET:** `getNetworkDevices` (Inventario), `getHosts`.
* **PUT:** `updateNetworkDevice` (Sincronización).
* **DELETE:** `deleteNetworkDeviceById`.
[cite_start][cite: 240-257]

### Scripts de Python
Se incluyeron scripts para verificar la programabilidad de la red desde la consola:
* [cite_start]`01_get-ticket.py`: Autenticación y obtención de Service Ticket[cite: 262].
* [cite_start]`02_get-network-device.py`: Obtención del inventario de dispositivos[cite: 266].
* [cite_start]`03_get-host.py`: Listado de hosts conectados[cite: 269].
* [cite_start]`04_tabulate.py`: Formato de salida tabular[cite: 272].

## 🚀 Instrucciones de Ejecución

1.  **Topología:** Abrir el archivo `.pkt` con Cisco Packet Tracer (versión recomendada 8.2 o superior).
2.  **API Server:** Asegurarse de que el servicio del Network Controller esté activo dentro de la simulación.
3.  **Python:**
    * Navegar a la carpeta `Scripts`.
    * Instalar dependencias (si aplica) o usar el entorno de Packet Tracer.
    * Ejecutar: `python 01_get-ticket.py`.
4.  **Postman:** Importar la colección JSON adjunta en la carpeta `/Postman` para probar los endpoints.

---
*Trabajo Práctico aprobado - Ingeniería e Investigaciones Tecnológicas - UNLaM*