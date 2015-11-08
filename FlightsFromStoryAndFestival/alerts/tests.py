from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from alerts.models import UserAlert
import json


class AlertTests(APITestCase):
    invalid_token ='123456invalidToken'
    valid_token   ='9a6b90ba'
    def test_alert_post_inValidUserToken(self):
        # url(r'^alerts/(?P<user_token>[A-Za-z0-9]+)/?$', alert_views_values, name='alerts'),
        data ={
                "id": 1,
                "alert_name": "test_alert_from_zhb",
                "username": "user_test01",
                "token": self.invalid_token,
                "alert_expression": "cpu_usage_rate  >  90",
                "rules": [
                    {
                        "rule_name": "rule1",
                        "stats_function_operator": "val",
                        "metric_name": "cpu_usage_rate",
                        "metric_key": "cpu_usage_rate",
                        "metric_threshold": "90",
                        "metric_evaluator": ">",
                        "metric_timeperiod": ""
                    }
                ],
                "actions": [
                    {
                        "alert_choice": "email",
                        "action_email": "zhb@gmail.com",
                        "action_api_url": "",
                        "action_payload": ""
                    }
                ],
                "status": "active",
                "last_triggered": 0.0,
                "frequency": 60.0
             }
        response = self.client.post(reverse('alerts', kwargs={'user_token': self.invalid_token}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('invalid token')!=-1)
        self.assertTrue(response.find('{"error":"invalid token"}')!=-1)


    def test_alert_post_validUserToken(self):
        count = UserAlert.objects.count()
        # url = 'http://localhost:8000/alerts/9a6b90ba'
        data ={
                "id": 1,
                "alert_name": "test_alert_from_zhb",
                "username": "user_test01",
                "token": self.valid_token,
                "alert_expression": "cpu_usage_rate  >  90",
                "rules": [
                    {
                        "rule_name": "rule1",
                        "stats_function_operator": "val",
                        "metric_name": "cpu_usage_rate",
                        "metric_key": "cpu_usage_rate",
                        "metric_threshold": "90",
                        "metric_evaluator": ">",
                        "metric_timeperiod": ""
                    }
                ],
                "actions": [
                    {
                        "alert_choice": "email",
                        "action_email": "zhb@gmail.com",
                        "action_api_url": "",
                        "action_payload": ""
                    }
                ],
                "status": "active",
                "last_triggered": 0.0,
                "frequency": 60.0
             }
        response = self.client.post(reverse('alerts',kwargs={'user_token':self.valid_token}), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserAlert.objects.count(), count+1)

        response =str(response)
        begin    = response.index('{')
        res_json_str =response[begin-1:].strip()
        res_json = json.loads(res_json_str)
        atrributes_list = ['id','alert_name','username','token','alert_expression','status','last_triggered','frequency']
        for key in atrributes_list:
            self.assertEqual(res_json[key],data[key])

        rule_attributes_list =['rule_name','stats_function_operator','metric_name','metric_key','metric_threshold','metric_evaluator','metric_timeperiod']

        i=0
        for rule in res_json['rules']:
            for key in rule_attributes_list:
                self.assertEqual(rule[key]  ,data['rules'][i][key])
            i+=1

        action_attributes_list=['alert_choice','action_email','action_api_url','action_payload']
        i=0
        for action in res_json['actions']:
            for key in action_attributes_list:
                self.assertEqual(action[key],data['actions'][i][key])
            i+=1

    def test_alert_get_validUserToken(self):
        # url = 'http://localhost:8000/alerts/9a6b90ba'
        response = self.client.get(reverse('alerts',kwargs={'user_token':self.valid_token}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_alert_get_invalidUserToken(self):
        # url = 'http://localhost:8000/alerts/invalidToken'
        response = self.client.get(reverse('alerts',kwargs={'user_token':self.invalid_token}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('invalid token')!=-1)
        self.assertTrue(response.find('{"error":"invalid token"}')!=-1)

    def test_alert_post_invalidData(self):
        count = UserAlert.objects.count()
        data ={
                    "id": 1,
                    # "alert_name": "test_alert_from_zhb",
                    # "username": "user_test01",
                    "token": self.valid_token,
                    # "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            # "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    # "actions": [
                    #     {
                    #         "alert_choice": "email",
                    #         "action_email": "zhb@gmail.com",
                    #         "action_api_url": "",
                    #         "action_payload": ""
                    #     }
                    # ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }
        response = self.client.post(reverse('alerts',kwargs={'user_token':self.valid_token}), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(UserAlert.objects.count(), count)
        response =str(response)
        begin    = response.index('{')
        res_json_str =response[begin-1:].strip()
        res_json = json.loads(res_json_str)
        print 'the response is 999999999999999999999999999999999999999999999999999 : ', res_json_str
        print 'the response is 999999999999999999999999999999999999999999999999999 : '
        print 'the response is 999999999999999999999999999999999999999999999999999 : '

        self.assertEqual(res_json['alert_name'][0],'This field is required.')
        self.assertEqual(res_json['username'][0],'This field is required.')
        self.assertEqual(res_json['alert_expression'][0],'This field is required.')
        self.assertEqual(res_json['rules'][0]['rule_name'][0],'This field is required.')
        self.assertEqual(res_json['actions'][0],'This field is required.')

        #
        # rule_attributes_list =['rule_name','stats_function_operator','metric_name','metric_key','metric_threshold','metric_evaluator','metric_timeperiod']
        #
        # i=0
        # for rule in res_json['rules']:
        #     for key in rule_attributes_list:
        #         self.assertEqual(rule[key]  ,data['rules'][i][key])
        #     i+=1
        #
        # action_attributes_list=['alert_choice','action_email','action_api_url','action_payload']
        # i=0
        # for action in res_json['actions']:
        #     for key in action_attributes_list:
        #         self.assertEqual(action[key],data['actions'][i][key])
        #     i+=1




class AlertDetialTest(APITestCase):
    invalid_token ='123456invalidToken'
    valid_token   ='9a6b90ba'
    def test_alert_detail_get_invalidUserToken(self):
        # url = 'http://localhost:8000/alerts/invalidToken/1'
        # url(r'^alerts/(?P<user_token>[A-Za-z0-9]+)/(?P<id>[0-9]+)/?$', alerts_views.alert_detail,name='alerts_detail'),
        response = self.client.get(reverse('alerts_detail',kwargs={'user_token':self.invalid_token,'id':1}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('invalid token')!=-1)
        self.assertTrue(response.find('{"error":"invalid token"}')!=-1)

    def test_alert_detail_put_invalidUserToken(self):
        data ={
                    "id": 1,
                    "alert_name": "test_alert_from_zhb",
                    "username": "user_test01",
                    "token": "9a6b90ba",
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }
        #Attention: url for Put method shoud shold with Id detail
        # url = 'http://localhost:8000/alerts/inValidToken/1'
        response = self.client.put(reverse('alerts_detail',kwargs={'user_token':self.invalid_token,'id':1}),data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('invalid token')!=-1)
        self.assertTrue(response.find('{"error":"invalid token"}')!=-1)

    def test_alert_detail_delete_invalidUserToken(self):
        # url = 'http://localhost:8000/alerts/inValidToken/1'
        # invalidToken ='123456invalidToken'
        response = self.client.delete(reverse('alerts_detail',kwargs={'user_token':self.invalid_token,'id':1}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('invalid token')!=-1)
        self.assertTrue(response.find('{"error":"invalid token"}')!=-1)


    def test_alert_detail_get_validUserToken_with_sameDataToken(self):
        # validToken='9a6b90ba'
        # url = 'http://localhost:8000/alerts/'+validToken
        data ={
                    "id": 1,
                    "alert_name": "test_alert_from_zhb",
                    "username": "user_test01",
                    "token": self.valid_token,
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }
        self.client.post(reverse('alerts',kwargs={'user_token':self.valid_token}), data, format='json')

        # url = 'http://localhost:8000/alerts/9a6b90ba/1'
        response = self.client.get(reverse('alerts_detail',kwargs={'user_token':self.valid_token,'id':1}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response =str(response)
        begin    = response.index('{')
        res_json_str =response[begin-1:].strip()
        res_json = json.loads(res_json_str)

        atrributes_list = ['id','alert_name','username','token','alert_expression','status','last_triggered','frequency']
        for key in atrributes_list:
            self.assertEqual(res_json[key],data[key])

        rule_attributes_list =['rule_name','stats_function_operator','metric_name','metric_key','metric_threshold','metric_evaluator','metric_timeperiod']

        i=0
        for rule in res_json['rules']:
            for key in rule_attributes_list:
                self.assertEqual(rule[key]  ,data['rules'][i][key])
            i+=1

        action_attributes_list=['alert_choice','action_email','action_api_url','action_payload']
        i=0
        for action in res_json['actions']:
            for key in action_attributes_list:
                self.assertEqual(action[key],data['actions'][i][key])
            i+=1

    def test_alert_detail_get_validUserToken_with_differentDataToken(self):
        valid_token1='9a6b90ba'
        valid_token2='8f8e1a68'

        data ={
                    "id": 1,
                    "alert_name": "test_alert_from_zhb",
                    "username": "user_test01",
                    "token": valid_token2,
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }
        # url = 'http://localhost:8000/alerts/'+valid_token1
        response_post=self.client.post(reverse('alerts',kwargs={'user_token':valid_token1}), data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        # url = 'http://localhost:8000/alerts/'+valid_token1+'/1/'
        response = self.client.get(reverse('alerts_detail',kwargs={'user_token':valid_token1,'id':1}))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('Not allowed to access')!=-1)
        self.assertTrue(response.find('{"error":"Not allowed to access"}')!=-1)






# AssertionError: The `.update()` method does not support writable nestedfields by default.
# Write an explicit `.update()` method for serializer `alerts.serializers.AlertSerializer`,
# or set `read_only=True` on nested serializer fields.

    def test_alert_detail_put_validUserToken_with_sameDataToken(self):
        data ={
                    "id": 1,
                    "alert_name": "test_alert_from_zhb",
                    "username": "user_test01",
                    "token": self.valid_token,
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }
        # url = 'http://localhost:8000/alerts/'+token
        response_post = self.client.post(reverse('alerts',kwargs={'user_token':self.valid_token}), data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        data_to_update ={
                    "id": 1,
                    "alert_name": "updated_test_alert_from_zhb",
                    "username": "updated_user_test01",
                    "token": self.valid_token,
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "updated_rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "updated_zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }

        # url = 'http://localhost:8000/alerts/9a6b90ba/1'
        response = self.client.put(reverse('alerts_detail',kwargs={'user_token':self.valid_token,'id':1}) ,data_to_update,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!Can not complete Cascade operation and update the nestedfields 'rules and actions' !!!!!!!!!!
        #!!!!!!!!!!!!!!!!
        response_get_updated  =self.client.get(reverse('alerts_detail',kwargs={'user_token':self.valid_token,'id':1}))

        self.assertEqual(response_get_updated.status_code, status.HTTP_200_OK)
        print ":::::::updated::::::::"
        print "the updated response is::::updated::::: ",response_get_updated
        print ":::::::updated::::::::"
        response_get_updated =str(response_get_updated)
        begin    = response_get_updated.index('{')
        res_json_str =response_get_updated[begin-1:].strip()
        res_json = json.loads(res_json_str)

        atrributes_list = ['id','alert_name','username','token','alert_expression','status','last_triggered','frequency']
        for key in atrributes_list:
            self.assertEqual(res_json[key],data_to_update[key])

        rule_attributes_list =['rule_name','stats_function_operator','metric_name','metric_key','metric_threshold','metric_evaluator','metric_timeperiod']

        i=0
        for rule in res_json['rules']:
            for key in rule_attributes_list:
                self.assertEqual(rule[key]  ,data_to_update['rules'][i][key])
            i+=1

        action_attributes_list=['alert_choice','action_email','action_api_url','action_payload']
        i=0
        for action in res_json['actions']:
            for key in action_attributes_list:
                self.assertEqual(action[key],data_to_update['actions'][i][key])
            i+=1



    def test_alert_detail_put_validUserToken_with_differentDataToken(self):
        token1='9a6b90ba'
        token2='8f8e1a68'
        url = 'http://localhost:8000/alerts/'+token1
        data ={
                    "id": 1,
                    "alert_name": "test_alert_from_zhb",
                    "username": "user_test01",
                    "token": token2,
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }

        response_post=self.client.post(url, data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        url = 'http://localhost:8000/alerts/'+token1+'/1/'
        response = self.client.get(url)
        # print "the response is : ",response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response =str(response)
        self.assertTrue(response.find('error')!=-1)
        self.assertTrue(response.find('Not allowed to access')!=-1)
        self.assertTrue(response.find('{"error":"Not allowed to access"}')!=-1)

    def test_alert_detail_delete_validTolen(self):
        data ={
                    "id": 1,
                    "alert_name": "test_alert_from_zhb",
                    "username": "user_test01",
                    "token": self.valid_token,
                    "alert_expression": "cpu_usage_rate  >  90",
                    "rules": [
                        {
                            "rule_name": "rule1",
                            "stats_function_operator": "val",
                            "metric_name": "cpu_usage_rate",
                            "metric_key": "cpu_usage_rate",
                            "metric_threshold": "90",
                            "metric_evaluator": ">",
                            "metric_timeperiod": ""
                        }
                    ],
                    "actions": [
                        {
                            "alert_choice": "email",
                            "action_email": "zhb@gmail.com",
                            "action_api_url": "",
                            "action_payload": ""
                        }
                    ],
                    "status": "active",
                    "last_triggered": 0.0,
                    "frequency": 60.0
                 }
        # url = 'http://localhost:8000/alerts/'+valid_token
        response_post = self.client.post(reverse('alerts',kwargs={'user_token':self.valid_token}), data, format='json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)

        # url = 'http://localhost:8000/alerts/'+valid_token+'/1'
        response = self.client.delete(reverse('alerts_detail',kwargs={'user_token':self.valid_token,'id':1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
