from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.inventory import Hardware

class HardwareService:
    def create_hardware(self, serial, name, description, type, state, available, comment):
        serial = UtilText.apply_trim(serial)
        name = UtilText.apply_trim(name)
        description = UtilText.apply_trim(description)
        comment = UtilText.apply_trim(comment)
        
        hardware = Hardware.objects.create(
            _serial = serial,
            _name = name,
            _description = description,
            _comment = comment,
            _type = type,
            _state = state,
            _available = available
        )
        return hardware