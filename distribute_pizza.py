#!/usr/bin/env python3

import pizzatron

from util.guild import pizza_distribution


GUILD = 'Braves of Glory'


def _ord(n):
    return f'{n}{"st" if n == 1 else "nd" if n == 2 else "rd" if n == 3 else "th"}'


def main(guild_name):
    print('Generating summary...')
    link, guild = pizza_distribution.auto_summary(guild_name)
    placement = pizza_distribution.Season.pizza_to_placement(guild.pizza[-1])

    if placement >= 6:
        return

    season_name = guild.seasons[-1].name

    breadwinners = ''
    for pizza in range(5, 0, -1):
        tier = list(filter(lambda x: x.pizza[-1] == pizza, guild.players))
        if tier:
            if len(tier) == 1:
                breadwinners += f'{tier[0].name} receives {pizza} pizza.\n'
            elif len(tier) == 2:
                breadwinners += f'{tier[0].name} and {tier[1].name} receive {pizza} pizza.\n'
            else:
                breadwinners += ', '.join(player.name for player in tier[:-1])
                breadwinners += f', and {tier[-1].name} receive {pizza} pizza.\n'

    msg = ((f'@everyone\n'
            f'**{guild_name} wins {_ord(placement)} place in {season_name}!**\n'
            f'\n'
            f'{breadwinners}\n'
            f'*Updated distribution*: {link}'))

    print('Announcing...')
    pizzatron.announce(msg)
    print(msg)


if __name__ == '__main__':
    main(GUILD)
