from django.shortcuts import render
from django.http import JsonResponse
from .models import User
import logging
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

# Create your views here.


@csrf_exempt
def do_auth(request):
    '''
    You can test this view with the supplied rauth_test.sh shell script (requires curl)
    :param request:
    :return:
    '''
    result = {}     # Dictionary
    username = None
    if request.method == 'POST':
        try:
            usr = User.objects.get(username__iexact=request.POST['username'])
            if usr:
                logger.info(
                    "[username=%s] User Object: require_valid_password=%s pass_if_pw_match=%s" % (
                        usr.username,
                        usr.require_valid_password,
                        usr.pass_if_pw_match
                    )
                )
                username = usr.username
                pw_match = False
                reason = ""

                if usr.pass_if_pw_match:
                    if usr.require_valid_password:
                        if request.POST['password'] == usr.password:
                            pw_match = True
                            reason = "Required valid password and passwords matched."
                        else:
                            reason = "Required valid password and passwords DID NOT match."
                    else:
                        pw_match = True
                        reason = "Default pass is set to TRUE and requiring a valid password is set to FALSE"
                else:
                    # Force Fail
                    reason = "Password checks are FORCED to FAIL"

                if pw_match:
                    result = {'result': 'pass', }
                else:
                    result = {'result': 'fail', }
                result['reason'] = reason

            else:
                result = {
                    'result': 'fail',
                    'reason': 'User not found (01)',
                }
        except:
            result = {
                    'result': 'fail',
                    'reason': 'User not found (02)',
                }
            pass
    else:
        result = {
            'result': 'fail',
            'reason': 'Only POST method is accepted',
        }
    logger.info("[username=%s] result=%s" % (username, result))
    response = JsonResponse(result)
    return response
