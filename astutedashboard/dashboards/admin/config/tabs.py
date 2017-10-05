#
# Copyright 2017 NephoScale
#


from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from openstack_dashboard import api

from astutedashboard.common import get_billing_types,	get_service_types, \
		get_plans, get_discount_types, get_discounts, get_rab_rates

from astutedashboard.dashboards.admin.config import tables


class BillingTypesTab(tabs.TableTab):
		name = _("Billing Types")
		slug = "billing_types_tab"
		table_classes = (tables.BillingTypesTable,)
		template_name = ("admin/config/_table.html")
		preload = False

		def get_billing_types_data(self):
			try:
					data = get_billing_types()
					return data

			except Exception:
					error_message = _('Unable to get billing types')
					exceptions.handle(self.request, error_message)
					return []


class ServiceTypesTab(tabs.TableTab):
		name = _("Service Types")
		slug = "service_types_tab"
		table_classes = (tables.ServiceTypesTable,)
		template_name = ("horizon/common/_detail_table.html")
		preload = False

		def get_service_types_data(self):
			try:
					data = get_service_types()
					return data

			except Exception:
					self._has_more = False
					error_message = _('Unable to get service types')
					exceptions.handle(self.request, error_message)

					return []



class DiscountTypesTab(tabs.TableTab):
		name = _("Discount Types")
		slug = "discount_types_tab"
		table_classes = (tables.DiscountTypesTable,)
		template_name = ("horizon/common/_detail_table.html")
		preload = False

		def get_discount_types_data(self):
			try:
					data = get_discount_types()
					return data

			except Exception:
					self._has_more = False
					error_message = _('Unable to get discount types')
					exceptions.handle(self.request, error_message)

					return []


class DiscountsTab(tabs.TableTab):
		name = _("Discounts")
		slug = "discounts_tab"
		table_classes = (tables.DiscountsTable,)
		template_name = ("horizon/common/_detail_table.html")
		preload = False

		def get_discounts_data(self):
			try:
					data = get_discounts()
					return data

			except Exception:
					self._has_more = False
					error_message = _('Unable to get discounts')
					exceptions.handle(self.request, error_message)

					return []


class PlansTab(tabs.TableTab):
		name = _("Plans")
		slug = "plans_tab"
		table_classes = (tables.PlansTable,)
		template_name = ("horizon/common/_detail_table.html")
		preload = False

		def get_plans_data(self):
			try:
					data = get_plans(verbose=True)
					return data

			except Exception:
					self._has_more = False
					error_message = _('Unable to get plans')
					exceptions.handle(self.request, error_message)

					return []


class RABRatesTab(tabs.TableTab):
		name = _("RAB Rates")
		slug = "rab_rates_tab"
		table_classes = (tables.RABRatesTable,)
		template_name = ("horizon/common/_detail_table.html")
		preload = False

		def get_rab_rates_data(self):
			try:
					data = get_rab_rates()
					return data

			except Exception:
					self._has_more = False
					error_message = _('Unable to get RAB rates')
					exceptions.handle(self.request, error_message)

					return []


class ConfigTabs(tabs.TabGroup):
    slug = "config_tabs"
    tabs = (
	    		BillingTypesTab,
	    		ServiceTypesTab,
	    		DiscountTypesTab,
	    		DiscountsTab,
	    		PlansTab,
	    		RABRatesTab,
    	)
    sticky = True
