from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.usecase.hardware.ICreateHardwareUseCase import ICreateHardwareUseCase
from co.edu.uco.invook.applicationcore.usecase.hardware.IGetAllHardwareUseCase import IGetAllHardwareUseCase
from co.edu.uco.invook.applicationcore.usecase.hardware.IGetHardwareBySerialUseCase import IGetHardwareBySerialUseCase
from co.edu.uco.invook.applicationcore.usecase.hardware.IDeleteHardwareUseCase import IDeleteHardwareUseCase


class HardwareFacade:
    def __init__(
        self,
        create_hardware_uc: ICreateHardwareUseCase,
        get_all_hardware_uc: IGetAllHardwareUseCase,
        get_hardware_by_serial_uc: IGetHardwareBySerialUseCase,
        delete_hardware_uc: IDeleteHardwareUseCase
    ):
        self._create_hardware_uc = create_hardware_uc
        self._get_all_hardware_uc = get_all_hardware_uc
        self._get_hardware_by_serial_uc = get_hardware_by_serial_uc
        self._delete_hardware_uc = delete_hardware_uc

    def create_hardware(self, hardware: Hardware) -> None:
        self._create_hardware_uc.execute(hardware)

    def get_all_hardware(self) -> List[Hardware]:
        return self._get_all_hardware_uc.execute()

    def get_hardware_by_serial(self, serial: str) -> Optional[Hardware]:
        return self._get_hardware_by_serial_uc.execute(serial)

    def delete_hardware(self, serial: str) -> None:
        self._delete_hardware_uc.execute(serial)
