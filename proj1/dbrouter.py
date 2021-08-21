
class AuthRouter():

    def db_for_read(self, model, **hints):
        if model._meta.app_label == "app":
            return None
        if model._meta.app_label == "book":
            return "db2"
        return "db"

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "app":
            return None
        if model._meta.app_label == "book":
            return "db2"
        return "db"

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == "app" and obj2._meta.app_label == "app":
            return None
        if obj1._meta.app_label == "book" and obj2._meta.app_label == "book":
            return "db2"
        return "db"

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == "app":
            return db == "db"
        if app_label == "book":
            return db == "db2"
        else:
            return db == "db"
