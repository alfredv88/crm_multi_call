# Guía paso a paso: Subir, instalar y probar el módulo crm_multi_call en Odoo

## 1. Comprimir la carpeta en un ZIP

1. Asegúrate de que la carpeta se llame exactamente `crm_multi_call` y contenga todos los archivos y subcarpetas.
2. Haz clic derecho sobre la carpeta `crm_multi_call`.
3. Selecciona **Enviar a > Carpeta comprimida (zip)** (en Windows) o **Comprimir** (en Mac).
4. Se creará un archivo llamado `crm_multi_call.zip`.

---

## 2. Subir el módulo a Odoo

### A. Si tienes opción "Importar" en la web de Odoo
1. Ve a **Aplicaciones** (Apps) en Odoo.
2. Haz clic en el botón **Importar** (arriba a la derecha).
3. Selecciona el archivo `crm_multi_call.zip` y súbelo.
4. Espera a que Odoo procese el archivo.

### B. Si NO tienes opción "Importar"
1. Usa FileZilla, WinSCP o SCP para subir la carpeta `crm_multi_call` a la carpeta de addons de tu servidor Odoo (por ejemplo, `/opt/odoo/odoo/addons/`).
2. Reinicia el servicio de Odoo (por SSH):
   ```bash
   systemctl restart odoo
   # o
   service odoo restart
   ```

---

## 3. Instalar el módulo en Odoo

1. Ve a **Aplicaciones** (Apps).
2. Haz clic en el ícono de **Actualizar lista de aplicaciones** (flecha circular, arriba a la derecha).
   - Si no lo ves, activa el **modo desarrollador** en **Ajustes**.
3. Busca "CRM Multi Call" o "call".
4. Haz clic en **Instalar** junto al módulo.

---

## 4. Configurar los parámetros AMI

1. Ve a **Ajustes** > **Técnico** > **Parámetros del sistema**.
2. Agrega o verifica los siguientes parámetros (usa los valores reales de tu entorno):

   | Clave                        | Valor de ejemplo   |
   |------------------------------|--------------------|
   | crm_multi_call.ami_host      | 172.32.0.4         |
   | crm_multi_call.ami_port      | 5038               |
   | crm_multi_call.ami_user      | odoo               |
   | crm_multi_call.ami_password  | odoo               |
   | crm_multi_call.extension     | 123                |
   | crm_multi_call.context       | from-internal      |

---

## 5. Probar el módulo

1. Ve al menú **CRM**.
2. Crea un lead (cliente potencial) con un número de teléfono.
3. Haz clic en el botón **Multi Call** en el formulario del lead.
4. Haz clic en **Start Multi Call** en la ventana que aparece.
5. Observa el resultado:
   - El sistema intentará llamar al número usando Issabel/Asterisk.
   - El estado de la llamada se actualizará.
   - Podrás dejar una nota y se registrará la actividad en el lead.

---

## ¿Qué hacer si hay errores?

- Si Odoo se cae o muestra error, revisa los logs del servidor y copia aquí el mensaje.
- Si el botón no aparece, asegúrate de que el módulo esté instalado y la lista de aplicaciones actualizada.
- Si la llamada no se realiza, revisa los parámetros AMI y la configuración de Issabel/Asterisk.

---

**Si tienes dudas o te atoras en algún paso, pide ayuda indicando el paso exacto donde te quedaste.** 