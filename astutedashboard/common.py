#
# Copyright 2017 NephoScale
#

from openstack_dashboard.local.local_settings import ASTUTE_BASE_URL

import requests as request


#
# Billing Types helper routines
#

# @returns billing types list
def get_billing_types():
		response = request.get(ASTUTE_BASE_URL + 'billing/type')
		return response.json()

# @returns billing type data
def get_billing_type(id):
		response = request.get(ASTUTE_BASE_URL + 'billing/type/' + str(id))
		return response.json()

# create billing type
def create_billing_type(data):
		response = request.post(ASTUTE_BASE_URL + 'billing/type', json=data)
		return response.json()

# modify billing type
def modify_billing_type(id, data):
		response = request.put(ASTUTE_BASE_URL + 'billing/type/' + str(id), json=data)
		return response.json()

# delete billing type
def delete_billing_type(id):
		response = request.delete(ASTUTE_BASE_URL + 'billing/type/' + str(id))
		return response.json()

#
# Service Tyles helper routines
#

# @returns service types list
def get_service_types():
		response = request.get(ASTUTE_BASE_URL + 'service_type')
		# TODO (div): adjust response format for consistency
		return response.json()['service_types']['rows']

# @returns service type data
def get_service_type(id):
		response = request.get(ASTUTE_BASE_URL + 'service_type/' + str(id))
		# TODO (div): adjust response format for consistency
		return response.json()['service_types']['rows'][0]

# create service type
def create_service_type(data):
		response = request.post(ASTUTE_BASE_URL + 'service_type', json=data)
		return response.json()

# modify service type
def modify_service_type(id, data):
		response = request.put(ASTUTE_BASE_URL + 'service_type/' + str(id), json=data)
		return response.json()

# modify service type
def delete_service_type(id):
		response = request.delete(ASTUTE_BASE_URL + 'service_type/' + str(id))
		return response.json()

#
# Discount helper routines
#

# @returns discount types list
def get_discount_types():
		response = request.get(ASTUTE_BASE_URL + 'discount/type')
		return response.json()

# @returns discount type data
def get_discount_type(id):
		response = request.get(ASTUTE_BASE_URL + 'discount/type/' + str(id))
		return response.json()

#
# Discounts helper routines
#

# @returns discounts list
def get_discounts():
		response = request.get(ASTUTE_BASE_URL + 'discount')
		data = response.json()
		# adjust data
		for item in data:
				item['create_time'] = item['create_time'].split(' ')[0]
				item['expiration_date'] = item['expiration_date'].split(' ')[0]
		return data

# @returns discount data
def get_discount(id):
		response = request.get(ASTUTE_BASE_URL + 'discount/' + str(id))
		data = response.json()
		# adjust data
		data['create_time'] = data['create_time'].split(' ')[0]
		data['expiration_date'] = data['expiration_date'].split(' ')[0]
		return data

# create discount
def create_discount(data):
		response = request.post(ASTUTE_BASE_URL + 'discount', json=data)
		return response.json()

# modify discount
def modify_discount(id, data):
		response = request.put(ASTUTE_BASE_URL + 'discount/' + str(id), json=data)
		return response.json()

# delete discount
def delete_discount(id):
		response = request.delete(ASTUTE_BASE_URL + 'discount/' + str(id))
		return response.json()

#
# Plans helper routines
#

# @returns plans list
def get_plans(verbose = False):
		response = request.get(ASTUTE_BASE_URL + 'plan')
		plans = response.json()
		if verbose:
				_service_types = get_service_types()
				service_types = {}
				for service_type in _service_types:
						service_types[service_type['id']] = service_type
				for plan in plans:
						plan['service_type'] = service_types[plan['service_type']]['name']
		return plans

# @returns plan data
def get_plan(id, verbose = False):
		response = request.get(ASTUTE_BASE_URL + 'plan' + str(id))
		plan = response.json()
		if verbose:
				_service_types = get_service_types()
				service_types = {}
				for service_type in _service_types:
						service_types[service_type['id']] = service_type
				plan['service_type'] = service_types[plan['service_type']]['name']
		return plans

# create plan
def create_plan(data):
		response = request.post(ASTUTE_BASE_URL + 'plan', json=data)
		return response.json()

# modify plan
def modify_plan(id, data):
		response = request.put(ASTUTE_BASE_URL + 'plan/' + str(id), json=data)
		return response.json()

# delete plan
def delete_plan(id):
		response = request.delete(ASTUTE_BASE_URL + 'plan/' + str(id))
		return response.json()

#
# RAB Rates helper routines
#

def get_rab_rates():
		response = request.get(ASTUTE_BASE_URL + 'rabrate')
		return response.json()
