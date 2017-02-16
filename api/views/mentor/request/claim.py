"""
    Claim a help request. Can only be done by mentors.
"""

from django import forms
from django.core.exceptions import ValidationError
from hackfsu_com.views.generic import ApiView
from hackfsu_com.util import acl
from api.models import HelpRequest


class RequestForm(forms.Form):
    help_request_id = forms.IntegerField()


class ClaimView(ApiView):
    request_form_class = RequestForm
    access_manager = acl.AccessManager(acl_accept=[acl.group_mentor])

    def work(self, request, req, res):
        help_request = HelpRequest.objects.filter(id=req['help_request_id'])
        if help_request.exists():
            help_request = help_request[0]
        else:
            raise ValidationError('Invalid help request id')

        if hasattr(help_request, 'assigned_mentor'):
            # Already claimed
            raise ValidationError('Cannot claim help request because it is already claimed')

        # Assign to mentor
        help_request.assigned_mentor = request.user.mentor_info
        help_request.save()
