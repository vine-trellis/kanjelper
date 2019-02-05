from __future__ import print_function # Python 2/3 compatibility
import boto3
import os
import tz

# if os.name == 'nt':
#     def _naive_is_dst(self, dt):
#         timestamp = tz.tz._datetime_to_timestamp(dt)
#         # workaround the bug of negative offset UTC prob
#         if timestamp+time.timezone < 0:
#             current_time = timestamp + time.timezone + 31536000
#         else:
#             current_time = timestamp + time.timezone
#         return time.localtime(current_time).tm_isdst

# tz.tzlocal._naive_is_dst = _naive_is_dst

dynamodb = boto3.resource('dynamodb', region_name='dan-region', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Kanji2')

table.delete()
