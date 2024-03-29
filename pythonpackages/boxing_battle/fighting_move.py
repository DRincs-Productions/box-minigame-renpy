from typing import Optional, Union


class FightingMove:
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        animation_image: Union[str, list[str]],
        animation_sound: Optional[str] = None,
        can_be_pressed: bool = True,
    ):
        self.name = name
        self.icon = icon
        self.key = key
        if isinstance(animation_image, str):
            animation_image = [animation_image]
        self.animation_image = animation_image
        self.animation_sound = animation_sound
        self.can_be_pressed = can_be_pressed
        self.selected = False
        self.stamina_cost = 0

    @property
    def name(self) -> str:
        """The name of the move."""
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def icon(self) -> str:
        """The icon of the move."""
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def key(self) -> str:
        """The key of the move."""
        return self._key

    @key.setter
    def key(self, value: str):
        self._key = value

    @property
    def animation_image(self) -> str:
        """The image of the move."""
        if isinstance(self._animation_image, list):
            if len(self._animation_image) == 0:
                return ""
            return self._animation_image[0]
        return self._animation_image

    @property
    def animation_images(self) -> list[str]:
        """The images of the move."""
        if isinstance(self._animation_image, list):
            return self._animation_image
        return [self._animation_image]

    @animation_image.setter
    def animation_image(self, value: list[str]):
        self._animation_image = value

    @property
    def animation_sound(self) -> Optional[str]:
        """The sound of the move."""
        return self._animation_sound

    @animation_sound.setter
    def animation_sound(self, value: Optional[str]):
        self._animation_sound = value

    @property
    def can_be_pressed(self) -> bool:
        """If the move can be pressed."""
        return self._can_be_pressed

    @can_be_pressed.setter
    def can_be_pressed(self, value: bool):
        self._can_be_pressed = value

    @property
    def selected(self) -> bool:
        """If the move is selected."""
        return self._selected

    @selected.setter
    def selected(self, value: bool):
        self._selected = value

    @property
    def stamina_cost(self) -> int:
        """The required stamina of the move."""
        return self._stamina_cost

    @stamina_cost.setter
    def stamina_cost(self, value: int):
        self._stamina_cost = value


class AttackMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        health_damage: int,
        key: str,
        animation_image: Union[str, list[str]],
        stamina_cost: int,
        animation_sound: Optional[str] = None,
        stun_time: float = 0,
    ):
        super().__init__(
            name=name,
            icon=icon,
            key=key,
            animation_image=animation_image,
            animation_sound=animation_sound,
            can_be_pressed=False,
        )

        self.health_damage = health_damage
        self.stun_time = stun_time
        self.stamina_cost = stamina_cost

    @property
    def health_damage(self) -> int:
        """The health damage of the move."""
        return self._health_damage

    @health_damage.setter
    def health_damage(self, value: int):
        self._health_damage = value

    @property
    def stun_time(self) -> float:
        """The stun time of the move."""
        if self._stun_time is None:
            return 0.0
        return self._stun_time

    @stun_time.setter
    def stun_time(self, value: Optional[float]):
        self._stun_time = value


class DefenseMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        animation_image: str,
        animation_sound: Optional[str] = None,
        health_resistance: Optional[int] = None,
        stamina_cost: int = 0,
    ):
        super().__init__(
            name=name,
            icon=icon,
            key=key,
            animation_image=animation_image,
            animation_sound=animation_sound,
            can_be_pressed=True,
        )

        self.health_resistance = health_resistance
        self.stamina_cost = stamina_cost

    @property
    def health_resistance(self) -> int:
        """
        The health resistance of the move.
        Default is 999999.
        """
        if self._health_resistance is None:
            return 999999
        return self._health_resistance

    @health_resistance.setter
    def health_resistance(self, value: Optional[int]):
        self._health_resistance = value


class DodgeMove(FightingMove):
    def __init__(
        self,
        name: str,
        icon: str,
        key: str,
        effect_time: float,
        animation_image: str,
        animation_sound: Optional[str] = None,
    ):
        super().__init__(
            name=name,
            icon=icon,
            key=key,
            animation_image=animation_image,
            animation_sound=animation_sound,
            can_be_pressed=False,
        )
        effect_time = effect_time

    @property
    def effect_time(self) -> float:
        """The effect time of the move."""
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value: float):
        self._effect_time = value
