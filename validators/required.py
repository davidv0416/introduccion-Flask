from flask import flash

def Required(field, nombre):
    if field == "":
        flash('El campo '+ nombre +' es requerido')
        return False
    return True