# Configuración de Parámetros AMI para crm_multi_call en Odoo

Sigue estos pasos para configurar la integración con Issabel/Asterisk:

## 1. Acceso a Parámetros del Sistema

1. Ve a **Ajustes** > **Técnico** > **Parámetros** > **Parámetros del sistema**.
   - Si no ves "Técnico", activa el modo desarrollador en Odoo.

## 2. Agrega los siguientes parámetros

| Clave                        | Valor de ejemplo   | Descripción                                 |
|------------------------------|--------------------|---------------------------------------------|
| crm_multi_call.ami_host      | 172.32.0.4         | IP de tu Issabel/Asterisk                   |
| crm_multi_call.ami_port      | 5038               | Puerto AMI (por defecto 5038)               |
| crm_multi_call.ami_user      | odoo               | Usuario AMI                                 |
| crm_multi_call.ami_password  | odoo               | Contraseña AMI                              |
| crm_multi_call.extension     | 123                | Extensión SIP que origina la llamada        |
| crm_multi_call.context       | from-internal      | Contexto de marcado (usualmente from-internal) |

## 3. Notas importantes

- El usuario AMI debe tener permisos para "originate" en Issabel/Asterisk.
- La extensión debe ser válida y tener permisos de salida.
- Puedes modificar estos parámetros en cualquier momento desde el mismo menú.

---

¡Listo! Ahora tu módulo `crm_multi_call` podrá comunicarse con Issabel/Asterisk usando estos parámetros. 