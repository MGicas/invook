from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.inventory import Supply

class SupplyService:
    def create_supply(self, code, name, description, stock):
        code = UtilText.apply_trim(code)
        name = UtilText.apply_trim(name)
        description = UtilText.apply_trim(description)
        stock = UtilNumber.ensure_positive(stock)
        
        supply = Supply.objects.create(
            _code = code,
            _name = name,
            _description = description,
            _stock = stock
        )
        return supply