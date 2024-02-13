import asyncio
import logging

from ipr_service.schemas import IprRequest
from ipr_service.service import IprService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - PID:%(process)d - threadName:%(thread)d - %(message)s",
)
logging.getLogger("pika").setLevel(logging.WARNING)


async def main():
    logging.info("program started")
    service = IprService()
    await service.async_start(service.settings.ipr_queue, IprRequest)


if __name__ == "__main__":
    asyncio.run(main())
