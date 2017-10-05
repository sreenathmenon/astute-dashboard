#
# Copyright 2017 NephoScale
#

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import forms

from openstack_dashboard import api

from astutedashboard.common import \
		create_billing_type, \
		modify_billing_type, \
		create_service_type, \
		modify_service_type, \
		create_discount, \
		modify_discount, \
		create_plan, \
		modify_plan, \
		get_billing_types, \
		get_discount_types, \
		get_service_types

#
# helper routines
#

# generate service types list
def gen_billing_types():
	data = []
	for item in get_billing_types():
			data.append((item['id'], _(item['name'])))
	return data

# generate dicount types list
def gen_discount_types():
	data = []
	for item in get_discount_types():
			data.append((item['id'], _(item['name'])))
	return data

# generate service types list
def gen_service_types():
	data = []
	for item in get_service_types():
			data.append((item['id'], _(item['name'])))
	return data

# generate flavors list
def gen_flavors():
	data = []
	#for item in get_discount_types():
	#		data.append((item['id'], _(item['name'])))
	return data


#
# Billing Type forms
#

class CreateBillingTypeForm(forms.SelfHandlingForm):

		name = forms.CharField(max_length=255, label=_("Name"))
		code = forms.CharField(max_length=32, label=_("Code"))

		def handle(self, request, data):
				try:
						create_billing_type(data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to create billing type.'))


class ModifyBillingTypeForm(forms.SelfHandlingForm):

		id = forms.CharField(label=_("ID"), widget=forms.HiddenInput())
		name = forms.CharField(max_length=255, label=_("Name"))
		code = forms.CharField(max_length=32, label=_("Code"))

		def handle(self, request, data):
				type_id = data.pop('id', None)
				if not type_id:
						exceptions.handle(request, _('Invalid request.'))
						return False
				try:
						modify_billing_type(id=type_id, data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to modify billing type.'))

#
# Service Type forms
#

class CreateServiceTypeForm(forms.SelfHandlingForm):

		name = forms.CharField(max_length=255, label=_("Name"))

		def handle(self, request, data):
				try:
						create_service_type(data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to create service type.'))


class ModifyServiceTypeForm(forms.SelfHandlingForm):

		id = forms.CharField(label=_("ID"), widget=forms.HiddenInput())
		name = forms.CharField(max_length=255, label=_("Name"))

		def handle(self, request, data):
				type_id = data.pop('id', None)
				if not type_id:
						exceptions.handle(request, _('Invalid request.'))
						return False
				try:
						modify_service_type(id=type_id, data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to service billing type.'))

#
# Discount forms
#

class CreateDiscountForm(forms.SelfHandlingForm):

		name = forms.CharField(max_length=255, label=_("Name"))
		code = forms.CharField(max_length=32, label=_("Code"))
		discount_type_id = forms.ChoiceField(label=_('Discount Type'), choices=[])
		expiration_date = forms.DateField(label=_('Expiration Date'))
		amt = forms.FloatField(label=_('Amount'))
		notes = forms.CharField(max_length=255, label=_("Notes"), required=False)

		def __init__(self, request, *args, **kwargs):
				super(CreateDiscountForm, self).__init__(request, *args, **kwargs)
				# set discount types
				self.fields['discount_type_id'].choices = gen_discount_types()

		def handle(self, request, data):
				data['expiration_date'] = str(data['expiration_date'])
				try:
						create_discount(data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to create discount type.'))


class ModifyDiscountForm(forms.SelfHandlingForm):

		id = forms.CharField(label=_("ID"), widget=forms.HiddenInput())
		name = forms.CharField(max_length=255, label=_("Name"))
		code = forms.CharField(max_length=32, label=_("Code"))
		discount_type_id = forms.ChoiceField(label = _('Discount Type'), choices=[])
		expiration_date = forms.DateField(label=_('Expiration Date'))
		amt = forms.FloatField(label=_('Amount'))
		notes = forms.CharField(max_length=255, label=_("Notes"), required=False)

		def handle(self, request, data):
				data['expiration_date'] = str(data['expiration_date'])
				type_id = data.pop('id', None)
				if not type_id:
						exceptions.handle(request, _('Invalid request.'))
						return False
				try:
						modify_discount(id=type_id, data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to modify discount type.'))

#
# Billing Plan forms
#

class CreatePlanForm(forms.SelfHandlingForm):

		name = forms.CharField(max_length=255, label=_("Name"))
		code = forms.CharField(max_length=32, label=_("Code"))
		rate = forms.FloatField(label=_('Rate'))
		setup_fee = forms.FloatField(label=_('Setup Fee'), required=False)
		service_type = forms.ChoiceField(label = _('Service Type'), choices=[])
		billing_type = forms.ChoiceField(label = _('Billing Type'), choices=[])
		ref_id = forms.ChoiceField(label = _('Flavor'), choices=[])
		attrs_cpu = forms.IntegerField(label=_('CPU'), required=False)
		attrs_ram = forms.IntegerField(label=_('RAM'), required=False)
		attrs_storage = forms.IntegerField(label=_('Storage'), required=False)

		def handle(self, request, data):
				try:
						create_plan(data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to create billing plan.'))


class ModifyPlanForm(forms.SelfHandlingForm):

		id = forms.CharField(label=_("ID"), widget=forms.HiddenInput())
		name = forms.CharField(max_length=255, label=_("Name"))
		code = forms.CharField(max_length=32, label=_("Code"))

		def handle(self, request, data):
				type_id = data.pop('id', None)
				if not type_id:
						exceptions.handle(request, _('Invalid request.'))
						return False
				try:
						modify_plan(id=type_id, data=data)
						return True

				except Exception:
						exceptions.handle(request, _('Unable to modify billing plan.'))

