# -*- coding: utf-8 -*-

__author__ = "gao"

from datetime import datetime

from AmazingQuant.event_engine.event_engine_base import Event
from AmazingQuant.constant import EventType, Status
from AmazingQuant.environment import Environment


class EventRiskManagement(Event):
    def __init__(self):
        super().__init__(event_type=EventType.EVENT_RISK_MANAGEMENT.value)

    @classmethod
    def black_namelist_check(cls, event):
        if Environment.current_order_data.status == Status.NOT_REPORTED.value and \
                Environment.current_order_data.instrument + "." + Environment.current_order_data.exchange not in \
                Environment.black_namelist:
            Environment.is_pass_risk = False
            print("Order Stock_code in Black_namelist")

        print("黑名单")
        pass

    @classmethod
    def change_order_status(cls, event):
        if Environment.is_pass_risk:
            Environment.current_order_data.status = Status.NOT_TRADED.value
        else:
            Environment.current_order_data.status = Status.WITHDRAW.value

    @classmethod
    def send_order(cls, event):
        if Environment.current_order_data.status == Status.NOT_TRADED.value:
            Environment.is_send_order = True