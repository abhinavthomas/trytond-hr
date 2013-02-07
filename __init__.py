# -*- coding: utf-8 -*-
"""
    __init__

    :copyright: © 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from .company import *
from .payroll import *
from .attendance import *


def register():
    Pool.register(
        Department,
        EmployeeDetail,
        Responsibility,
        Language,
        Academic,
        Skill,
        Team,
        TransferProposal,
        TransferRemark,
        PayrollPeriod,
        PayrollHoliday,
        Attendance,
        AttendanceSummary,
        PaymentDetail,
        module='hr', type_='model')
