# Guía de instalación y prueba del módulo crm_multi_call en Odoo

## 1. Acceso al servidor
- Tienes acceso SSH (root) y acceso web a Odoo.

## 2. Copiar el módulo al servidor
1. En tu PC, asegúrate de tener la carpeta `crm_multi_call` lista y corregida.
2. Conéctate por SFTP o SCP (por ejemplo, con FileZilla, WinSCP, o desde terminal):
   - Host: `91.99.174.237`
   - Usuario: `root`
   - Contraseña: `Project@pbx25`
   - Navega a la carpeta de addons de Odoo (usualmente `/odoo/custom_addons/` o `/opt/odoo/addons/`).
   - Sube la carpeta `crm_multi_call` ahí.
   - Por terminal (Linux/Mac):
     ```bash
     scp -r crm_multi_call root@91.99.174.237:/ruta/a/tu/carpeta/addons/
     ```

## 3. Reiniciar el servicio de Odoo
1. Conéctate por SSH:
   ```bash
   ssh root@91.99.174.237
   ```
2. Reinicia Odoo (el comando puede variar):
   ```bash
   systemctl restart odoo
   # o
   service odoo restart
   # o
   systemctl restart odoo-server
   ```

## 4. Instalar el módulo desde la web
1. Accede a Odoo en tu navegador:
   - URL: (la que te hayan dado, o prueba con la IP y el puerto, por ejemplo: `http://91.99.174.237:8069`)
2. Inicia sesión con:
   - Usuario: `develop@`
   - Contraseña: `Odoopbx25`
3. Ve a **Aplicaciones**.
4. Haz clic en **Actualizar lista de aplicaciones** (ícono de flecha circular o desde el menú de desarrollador).
5. Busca "CRM Multi Call".
6. Haz clic en **Instalar**.

## 5. Probar el módulo
1. Ve a **CRM**.
2. Crea un lead con un teléfono.
3. Haz clic en **Multi Call** y luego en **Start Multi Call**.

---

**Si tienes problemas en algún paso, revisa los mensajes de error y pide ayuda indicando el paso exacto donde te quedaste.** 