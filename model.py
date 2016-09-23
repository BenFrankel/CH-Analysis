# This file models the static CH structures (cards, items, characters).


class CardType:
    def __init__(self, ID, name, short_name, types, attack_type, damage_type, damage, min_range,
                 max_range, move_points, duration, trigger, keep, trigger_effect, trigger_effect2,
                 text, flavor_text, play_text, trigger_text, trigger_attempt_text,
                 trigger_succeed_text, trigger_fail_text, trigger_text2, trigger_attempt_text2,
                 trigger_succeed_text2, trigger_fail_text2, component1, params1, component2,
                 params2, component3, params3, component4, params4, component5, params5, params,
                 plus_minus, quality, quality_warrior, quality_priest, quality_wizard,
                 quality_dwarf, quality_elf, quality_human, rarity, function_tags, attach_image,
                 status, audio_key, audio_key2, from_set, level, slot_types, art):
        self.ID = ID
        self.name = name
        self.short_name = short_name
        self.types = types
        self.attack_type = attack_type
        self.damage_type = damage_type
        self.min_range = min_range
        self.max_range = max_range
        self.move_points = move_points
        self.duration = duration
        self.trigger = trigger
        self.keep = keep
        self.trigger_effect = trigger_effect
        self.trigger_effect2 = trigger_effect2
        self.text = text
        self.flavor_text = flavor_text
        self.play_text = play_text
        self.trigger_text = trigger_text
        self.trigger_attempt_text = trigger_attempt_text
        self.trigger_succeed_text = trigger_succeed_text
        self.trigger_fail_text = trigger_fail_text
        self.trigger_text2 = trigger_text2
        self.trigger_attempt_text2 = trigger_attempt_text2
        self.trigger_succeed_text2 = trigger_succeed_text2
        self.trigger_fail_text2 = trigger_fail_text2
        self.component1 = component1
        self.params1 = params1
        self.component2 = component2
        self.params2 = params2
        self.component3 = component3
        self.params3 = params3
        self.component4 = component4
        self.params4 = params4
        self.component5 = component5
        self.params5 = params5
        self.params = params
        self.plus_minus = plus_minus
        self.quality = quality
        self.quality_warrior = quality_warrior
        self.quality_priest = quality_priest
        self.quality_wizard = quality_wizard
        self.quality_dwarf = quality_dwarf
        self.quality_elf = quality_elf
        self.quality_human = quality_human
        self.rarity = rarity
        self.function_tags = function_tags
        self.attach_image = attach_image
        self.status = status
        self.audio_key = audio_key
        self.audio_key2 = audio_key2
        self.from_set = from_set
        self.level = level
        self.slot_types = slot_types
        self.art = art


class ItemType:
    def __init__(self, ID, name, short_name, rarity, level, intro_level, total_value, token_cost, cards, slot_type,
                 slot_type_default, image_name, tags, from_set, manual_rarity, manual_value):
        self.ID = ID
        self.name = name
        self.short_name = short_name
        self.rarity = rarity
        self.level = level
        self.intro_level = intro_level
        self.total_value = total_value
        self.token_cost = token_cost
        self.cards = cards
        self.slot_type = slot_type
        self.slot_type_default = slot_type_default
        self.image_name = image_name
        self.tags = tags
        self.from_set = from_set
        self.manual_rarity = manual_rarity
        self.manual_value = manual_value

    def __contains__(self, card_type):
        return card_type in self.cards


class CharacterArchetype:
    def __init__(self, name, character_type, role, race, description, default_move, default_figure, start_items,
                 slot_types, levels):
        self.name = name
        self.character_type = character_type
        self.role = role
        self.race = race
        self.description = description
        self.default_move = default_move
        self.default_figure = default_figure
        self.start_items = start_items
        self.slot_types = slot_types
        self.levels = levels