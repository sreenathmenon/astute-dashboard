#
# Copyright 2017 NephoScale
#


from django.utils.translation import ugettext_lazy as _
import horizon

from astutedashboard.dashboards.admin.config import panel as config_panel


class AstutePanels(horizon.PanelGroup):
    slug = "astute"
    name = _("Billing")
    panels = (config_panel.Config,)
