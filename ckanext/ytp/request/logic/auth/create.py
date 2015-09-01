from ckanext.ytp.request.helper import get_user_member

import ckan.new_authz as authz

def member_request_create(context, data_dict):
    """ Create request access check 
    Sysadmin should not be "allowed" to create as he has full access already """
    user = context['user']

    if not authz.auth_is_loggedin_user():
        return {'success': False, 'msg': _('User is not logged in')}
    if authz.is_sysadmin(user):
    	return {'success': False, 'msg': _('Sysadmin has already full access to organizations')}

    organization_id = None if not data_dict else data_dict.get('organization_id', None)

    if organization_id:
        member = get_user_member(organization_id)
        if member:
            return {'success': False, 'msg': _('The user has already a pending request or an active membership')}

    return {'success': True}

