#
# Copyright 2017 NephoScale
#

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms
from horizon import tabs

from astutedashboard.dashboards.admin.config \
    import forms as config_forms
from astutedashboard.dashboards.admin.config \
    import tabs as config_tabs

from astutedashboard.common import \
		get_billing_type, \
		get_service_type, \
		get_discount, \
		get_plan

class IndexView(tabs.TabbedTableView):
		tab_group_class = config_tabs.ConfigTabs
		template_name = "admin/config/index.html"


#
# Billing Type views
#

class CreateBillingTypeView(forms.ModalFormView):
		form_class = config_forms.CreateBillingTypeForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "create_billing_type_modal"
		modal_header = _("Create Billing Type")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:create_billing_type"

		def get_initial(self):
				return {}

		def get_context_data(self, **kwargs):
				context = super(CreateBillingTypeView, self).get_context_data(**kwargs)
				context['submit_url'] = reverse(self.submit_url)
				return context


class ModifyBillingTypeView(forms.ModalFormView):
		form_class = config_forms.ModifyBillingTypeForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "modify_billing_type_modal"
		modal_header = _("Modify Billing Type")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:modify_billing_type"

		def get_initial(self):
				return get_billing_type(id=self.kwargs['id'])

		def get_context_data(self, **kwargs):
				context = super(ModifyBillingTypeView, self).get_context_data(**kwargs)
				type_id = self.kwargs['id']
				context['submit_url'] = reverse(self.submit_url, args=[type_id])
				return context

#
# Service Type views
#

class CreateServiceTypeView(forms.ModalFormView):
		form_class = config_forms.CreateServiceTypeForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "create_service_type_modal"
		modal_header = _("Create Service Type")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:create_service_type"

		def get_initial(self):
				return {}

		def get_context_data(self, **kwargs):
				context = super(CreateServiceTypeView, self).get_context_data(**kwargs)
				context['submit_url'] = reverse(self.submit_url)
				return context


class ModifyServiceTypeView(forms.ModalFormView):
		form_class = config_forms.ModifyServiceTypeForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "modify_service_type_modal"
		modal_header = _("Modify Service Type")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:modify_service_type"

		def get_initial(self):
				return get_service_type(id=self.kwargs['id'])

		def get_context_data(self, **kwargs):
				context = super(ModifyServiceTypeView, self).get_context_data(**kwargs)
				type_id = self.kwargs['id']
				context['submit_url'] = reverse(self.submit_url, args=[type_id])
				return context

#
# Discount views
#
class CreateDiscountView(forms.ModalFormView):
		form_class = config_forms.CreateDiscountForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "create_discount_modal"
		modal_header = _("Create Discount")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:create_discount"

		def get_initial(self):
				return {}

		def get_context_data(self, **kwargs):
				context = super(CreateDiscountView, self).get_context_data(**kwargs)
				context['submit_url'] = reverse(self.submit_url)
				return context


class ModifyDiscountView(forms.ModalFormView):
		form_class = config_forms.ModifyDiscountForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "modify_discount_modal"
		modal_header = _("Modify Discount")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:modify_discount"

		def get_initial(self):
				return get_discount(id=self.kwargs['id'])

		def get_context_data(self, **kwargs):
				context = super(ModifyDiscountView, self).get_context_data(**kwargs)
				type_id = self.kwargs['id']
				context['submit_url'] = reverse(self.submit_url, args=[type_id])
				return context


#
# Plan views
#
class CreatePlanView(forms.ModalFormView):
		form_class = config_forms.CreatePlanForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "create_plan_modal"
		modal_header = _("Create Billing Plan")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:create_plan"

		def get_initial(self):
				return {}

		def get_context_data(self, **kwargs):
				context = super(CreatePlanView, self).get_context_data(**kwargs)
				context['submit_url'] = reverse(self.submit_url)
				return context


class ModifyPlanView(forms.ModalFormView):
		form_class = config_forms.ModifyPlanForm
		template_name = 'admin/config/billing_form.html'
		success_url = reverse_lazy("horizon:admin:billing_config:index")
		modal_id = "modify_plan_modal"
		modal_header = _("Modify Billing Plan")
		submit_label = _("Submit")
		submit_url = "horizon:admin:billing_config:modify_plan"

		def get_initial(self):
				return get_plan(id=self.kwargs['id'])

		def get_context_data(self, **kwargs):
				context = super(ModifyPlanView, self).get_context_data(**kwargs)
				type_id = self.kwargs['id']
				context['submit_url'] = reverse(self.submit_url, args=[type_id])
				return context
