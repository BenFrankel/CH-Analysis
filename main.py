import gamedata
import reconstruct
import optimize


log_filename = 'temp/example_logs/log1'

# gamedata.download()
gamedata.load()


def optimize_test():
    optimize.load()

    archetype = input('Archetype: ')
    print('Card Classes:\n ', '\n  '.join(sorted(optimize.get_card_classes().keys())))
    print()
    card_class_input = input('Optimize for: ')

    card_class_combo = dict()
    total_weight = 0
    for card_class_input in card_class_input.split(','):
        if '=' in card_class_input:
            name, weight = card_class_input.split('=')
            name = name.replace(':', '').strip()
            weight = float(weight.strip())
        else:
            name = card_class_input.replace(':', '').strip()
            weight = 1
        if ':' in card_class_input:
            card_class = {name: weight}
        else:
            card_class = optimize.get_card_class(name)
        for card in card_class:
            card_class_combo[card] = card_class_combo.get(card, 0) + weight * card_class[card]
        total_weight += weight
    for card in card_class_combo:
        card_class_combo[card] /= total_weight

    score, num_traits, optimum = optimize.optimum(archetype, card_class_combo)[0]
    print('\nTotal value: {}\nNumber of traits: {}\nAverage value: {}'.format(score, num_traits, score / (36 - num_traits)))
    print(', '.join(str(x) for x in optimum))
    print()
    for item in optimum:
        print(', '.join([str(card) for card in item.cards]), sep='')


def battle_test():
    while True:
        print('Commands: (u)pdate, (r)efresh, (s)how, (d)ownload')

        event_list = []
        command = input().lower().replace(' ', '')

        if command in "ur":
            event_list, battle = reconstruct.load_battle()
            if not event_list:
                event_list, battle = reconstruct.load_battle(log_filename)
        if command in "sr":
            for enemy in battle.enemy.groups:
                print()
                print(enemy)
                print()
            print('Enemy =', battle.enemy.name, 'index', battle.enemy.index)
            print(battle.scenario_name, 'aka', battle.scenario_display_name)
            print(battle.room_name)
            print()
            print(battle.map)
            for i, event in enumerate(event_list):
                print(i, event)
        if command == 'd':
            gamedata.download()
            gamedata.load()

        print()


battle_test()
