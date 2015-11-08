from rest_framework import serializers
from alerts.models import UserAlert
from alerts.models import AlertRule
from alerts.models import AlertAction

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertAction
        fields = ('alert_choice', 'action_email', 'action_api_url',
                  'action_payload')

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertAction
        fields = ('alert_choice', 'action_email', 'action_api_url',
                  'action_payload')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertAction
        fields = ('alert_choice', 'action_email', 'action_api_url',
                  'action_payload')


#Nested List Writable
class AlertRuleListSerializer(serializers.ListSerializer):
    def create(self,validated_data):
        rules =[AlertRule(**item) for item in validated_data]
        return AlertRule.objects.bulk_create(rules)

    def update(self, instance, validated_data):
        rule_mapping={rule.id:rule for rule in instance}
        data_mapping ={item['id']:item for item in validated_data}

        # Perform creations and updates.
        ret =[]
        for rule_id,data in data_mapping.items():
            rule = rule_mapping.get(rule_id,None)
            if rule is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(rule,data))

        # Perform deletions.
        for rule_id, rule in rule_mapping.items():
            if rule_id not in data_mapping:
                rule.delete()

        return ret

    def many_init(AlertRuleSerializer, *args, **kwargs):
        # Instantiate the child serializer.
        kwargs['child'] = AlertRuleSerializer()
        # Instantiate the parent list serializer.
        return AlertRuleListSerializer(*args, **kwargs)


class AlertRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertRule
        fields = ('rule_name', 'stats_function_operator', 'metric_name',
                  'metric_key', 'metric_threshold', 'metric_evaluator',
                  'metric_timeperiod')
        list_serializer_class =AlertRuleListSerializer


class AlertActionListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        actions=[AlertAction(**item) for item in validated_data]
        return AlertAction.objects.bulk_create(actions)

    def update(self, instance, validated_data):
        action_mapping ={action.id:action for action in instance}
        data_mapping   ={item['id']:item for item in validated_data}
        # Perform creations and updates.

        ret =[]
        for action_id,data in action_mapping.items():
            action = action_mapping.get(action_id,None)
            if action is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(action,data))

        # Perform deletions.
        for action_id, action in action_mapping.items():
            if action_id not in data_mapping:
                action.delete()
        return ret

    def many_init(AlertRuleSerializer, *args, **kwargs):
        # Instantiate the child serializer.
        kwargs['child'] = AlertActionSerializer()
        # Instantiate the parent list serializer.
        return AlertActionListSerializer(*args, **kwargs)

class AlertActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertAction
        fields = ('alert_choice', 'action_email', 'action_api_url',
                  'action_payload')
        list_serializer_class=AlertActionListSerializer



class AlertSerializer(serializers.ModelSerializer):
    # rules   = AlertRuleSerializer(many=True, read_only=False)
    # actions = AlertActionSerializer(many=True, read_only=False)
    rules   = AlertRuleSerializer(many=True,read_only=False)
    actions = AlertActionSerializer(many=True,read_only=False)
    # rules   = AlertRuleListSerializer(read_only=False)
    # actions = AlertActionListSerializer(read_only=False)
    class Meta:
        model = UserAlert
        fields = ('id', 'alert_name', 'created', 'username', 'token',
                  'alert_expression', 'alert_severity', 'rules', 'actions','status','last_triggered','frequency')

    #For Post
    def create(self, validated_data):
        rules_data   = validated_data.pop('rules')
        actions_data = validated_data.pop('actions')
        alert = UserAlert.objects. create(**validated_data)
        for rule_data in rules_data:
            AlertRule.objects.create(alert=alert, **rule_data)
        for action_data in actions_data:
            AlertAction.objects.create(alert=alert, **action_data)
        return alert

    #For Put
    def update(self, instance , validated_data):
        rules_list_data  =validated_data.get('rules')#list
        actions_list_data=validated_data.get('actions')#list

        rules   =instance.rules     #not iterable objects list,but related manager
        actions =instance.actions   #not iterable objects list,but related manager


        instance.id         = validated_data.get('id'        ,instance.id)
        instance.alert_name = validated_data.get('alert_name',instance.alert_name)
        instance.username   = validated_data.get('username'  ,instance.username)
        instance.token      = validated_data.get('token'     ,instance.token)

        instance.save()
        print '$'
        print '$'
        print '$'
        print type(instance)
        print type(rules)
        print type(actions)
        print validated_data
        print '$'
        print '$'
        print '$'

        for rule_data in rules_list_data:
            rules.rule_name = rule_data['rule_name']

        rules.save()
        actions.save()
        # for rule in rules:
        #     rule.save()
        #
        # for action in actions:
        #     action.save()
        return instance