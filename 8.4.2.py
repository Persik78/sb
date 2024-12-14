total_soldiers = int(input('Кол-во солдат: '))
total_rules = int(input('Кол-во правил: '))
count_push_ups = 0
for soldier in range(total_soldiers-3, 0, -4):
    print(soldier)
    rules_soldier = int(input('Солдат, сколько правил в уставе? '))
    if rules_soldier != total_rules:
        push_up = soldier * 10
        print('Хуйня, отжимайся', push_up, 'раз')
        count_push_ups += push_up
    else:
        print('Молодец солдат, так держать!')
        break
if count_push_ups != 0:
    print('Общее кол-во отжиманий:', count_push_ups)