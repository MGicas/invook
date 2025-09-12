from django.db.models import Model
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText
from co.edu.uco.invook.crosscutting.util.UtilNumber import UtilNumber

class UtilPatch:

    @staticmethod
    def patch_model(instance: Model, data: dict) -> Model:
        editable_fields = [f.name for f in instance._meta.get_fields() 
                        if getattr(f, "editable", False) and not f.auto_created]

        for key, value in data.items():
            if key not in editable_fields:
                continue 
            
            if isinstance(value, str):
                value = UtilText.apply_trim(value)
                
            elif isinstance(value, int) or isinstance(value, float):
                value = UtilNumber.ensure_positive(value)

            setattr(instance, key, value)

        instance.save()
        return instance
