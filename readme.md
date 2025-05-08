# 📝 Blog Personal API

API REST para gestionar un blog personal con autenticación JWT, permisos según el rol del usuario, y estructura limpia basada en Django REST Framework.

## 🚀 Características

- CRUD de publicaciones (posts).
- CRUD de comentarios.
- Usuarios autenticados pueden publicar y comentar.
- JWT para login/registro y protección de endpoints.
- Permisos: solo los autores pueden editar sus posts y comentarios.
- Serializadores separados para operaciones de lectura/escritura.
- Soporte para múltiples categorías por post (opcional).
- Documentación automática con Swagger/OpenAPI (si activás `drf-spectacular` o `drf-yasg`).

---

## 🛠️ Tecnologías

- Python 3.11+
- Django 5+
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL
- (Opcional) drf-spectacular o drf-yasg para documentación Swagger

---


