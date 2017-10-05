#
# Copyright 2017 NephoScale
#


from django.utils.translation import ugettext_lazy as _

import horizon


class Config(horizon.Panel):
    name = _("Configuration")
    slug = "billing_config"
