import logging

from common.handlers.base import MessageHandler
from common.models.oil_data import OilData
from gateway_service.manager import GatewayManager
from gateway_service.models import TaskStatus
from gateway_service.schemas import TaskSchema

from ipr_service.schemas import IprRequest
from ipr_service.settings import ServiceSettings


class IprService(MessageHandler):
    def __init__(self):
        super().__init__()
        self.settings = ServiceSettings()
        self.gateway_service_manager = GatewayManager(self.settings.gateway_service_url)

    def _calculate_ipr(self) -> OilData:
        """Функция является заглушкой расчетов. Вернуть дефолтные данные ipr."""
        return OilData(
            q_liq=[
                190.0446738744384,
                187.46046182072422,
                184.87624976701005,
                182.12243886015682,
                177.57083329326997,
                171.26580712037182,
                163.59504945642,
                154.8214808983079,
                145.1331376002457,
                134.6700119019678,
                123.53966094072084,
                111.82684391052348,
                99.60000000000002,
                87.15,
                74.70000000000002,
                62.25,
                49.80000000000001,
                37.35000000000002,
                24.900000000000006,
                12.450000000000017,
                0,
            ],
            p_wf=[
                1,
                13.45,
                25.9,
                38.349999999999994,
                50.8,
                63.25,
                75.69999999999999,
                88.14999999999999,
                100.6,
                113.05,
                125.5,
                137.95,
                150.39999999999998,
                162.85,
                175.29999999999998,
                187.75,
                200.2,
                212.64999999999998,
                225.1,
                237.54999999999998,
                250,
            ],
        )

    async def _process_message(self, request: IprRequest):
        """Обработать сообщение в очереди RabbitMQ."""
        logging.info(f"request received, task {request.id}")
        oil_data = self._calculate_ipr()
        updated_task = TaskSchema(id=request.id, status=TaskStatus.ipr_calculated, ipr=oil_data)
        await self.gateway_service_manager.update_task(task_schema=updated_task)
        logging.info(f"task {request.id} processed")
