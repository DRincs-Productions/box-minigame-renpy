﻿init python:
    from pythonpackages.boxing_battle.fighting_state import FightingState
    from pythonpackages.extra_animated_value.extra_animated_value import ExtraAnimatedValue
    from pythonpackages.extra_animated_value.value_image import ValueImage

screen boxing_battle(player, opponent, recover_time = 10):
    python:
        bar_player_health = ExtraAnimatedValue(
            value=player.health, 
            range=player.max_health, 
            range_delay=3.0,
            warper="ease_quart",
        )
        bar_player_stamina = ExtraAnimatedValue(
            value=player.stamina, 
            range=player.max_stamina, 
            range_delay=3.0,
            warper="ease_quart",
        )
        bar_opponent_health = ExtraAnimatedValue(
            value=opponent.health, 
            range=opponent.max_health, 
            range_delay=3.0,
            warper="ease_quart",
        )
        bar_opponent_stamina = ExtraAnimatedValue(
            value=opponent.stamina, 
            range=opponent.max_stamina, 
            range_delay=3.0,
            warper="ease_quart",
        )

    vbox:
        spacing 10
        align (0.02, 0.02)
        use health_bar(bar_player_health)
        use stamina_bar(bar_player_stamina)

    vbox:
        spacing 10
        align (0.98, 0.02)
        use health_bar(bar_opponent_health)
        use stamina_bar(bar_opponent_stamina)

    # ...
    use boxing_battle_opponent(opponent)
    use boxing_battle_player(player)
    use joystick(player)
    timer recover_time repeat True action [
            Function(opponent.recover_stamina),
        ]

screen boxing_battle_player(player):
    $ renpy.show(player.idle_image)

screen boxing_battle_opponent(opponent):
    $ renpy.show(opponent.image)
    timer opponent.random_thinking_time repeat True action [
            Function(renpy.hide, opponent.image),
            Function(opponent.update_move),
            Function(renpy.show, opponent.image),
        ]
    if opponent.current_state == FightingState.ATTACK:
        timer opponent.random_time_between_hits repeat opponent.current_state == FightingState.ATTACK action [
                Function(renpy.hide, opponent.image),
                Function(opponent.add_hit),
                Function(renpy.show, opponent.image),
            ]

screen health_bar(my_bar):
    fixed:
        area (0,0, 400, 50)
        bar:
            value my_bar
            left_bar "images/bar/health_bar_400x50_left.png"
            right_bar "images/bar/health_bar_400x50_right.png"
            area (0,0, 400, 50)

        add my_bar.text(
            "{0.current_value:.0f} hp",
            size = 22,
            color = "#FFF",
            outlines = [(abs(2), "#000")],
            bold = True,
            xcenter = 0.5,
            ycenter = 0.57)

screen stamina_bar(my_bar):
    fixed:
        area (0,0, 400, 50)
        bar:
            value my_bar
            left_bar "images/bar/health_bar_400x50_left.png"
            right_bar "images/bar/health_bar_400x50_right.png"
            area (0,0, 400, 50)

        add my_bar.text(
            "{0.current_value:.0f}/{0.range:.0f}",
            size = 22,
            color = "#DDE",
            outlines = [(abs(1), "#222")],
            bold = True,
            xcenter = 0.5,
            ycenter = 0.5)

screen joystick(player):
    use joystick_button(player.up_button, (0.15, 0.40))
    use joystick_button(player.down_button, (0.15, 0.70))
    use joystick_button(player.left_button, (0.06, 0.55))
    use joystick_button(player.right_button, (0.24, 0.55))

    use joystick_button(player.x_button, (0.85, 0.40))
    use joystick_button(player.a_button, (0.85, 0.70))
    use joystick_button(player.y_button, (0.76, 0.55))
    use joystick_button(player.b_button, (0.94, 0.55))

    vbox:
        spacing 10
        align (0.02, 0.98)
        if player.up_button:
            use move_info(player.up_button)
        if player.down_button:
            use move_info(player.down_button)
        if player.left_button:
            use move_info(player.left_button)
        if player.right_button:
            use move_info(player.right_button)
    vbox:
        spacing 10
        align (0.98, 0.98)
        if player.x_button:
            use move_info(player.x_button)
        if player.a_button:
            use move_info(player.a_button)
        if player.y_button:
            use move_info(player.y_button)
        if player.b_button:
            use move_info(player.b_button)

screen joystick_button(move, my_align):
    if move and move.icon:
        imagebutton:
            idle move.icon
            align my_align
            at joystick_button
        # key move.key TODO: antion

screen move_info(move):
    hbox:
        spacing 10
        add move.icon:
            xysize (25, 25)
        text move.name:
            size 22
            color "#FFF"
            outlines [(abs(2), "#000")]
            bold True
            xcenter 0.5
            ycenter 0.5
        text _("Key: [move.key]"):
            size 22
            color "#FFF"
            outlines [(abs(2), "#000")]
            bold True
            xcenter 0.5
            ycenter 0.5
