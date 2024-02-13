from common.rabbit.models import BaseRequest


class IprRequest(BaseRequest):
    p_res: float
    wct: float
    pi: float
    pb: float
