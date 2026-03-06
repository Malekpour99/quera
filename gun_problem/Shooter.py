# https://quera.org/problemset/182272?tab=description
# ---------------------------------------------------
from dataclasses import dataclass


@dataclass
class Bullet:
    type: str
    size: float
    damage: float


# Bullet Types
BULLET_TYPE_A = "A"
BULLET_TYPE_B = "B"
BULLET_TYPE_C = "C"
BULLET_TYPE_D = "D"

BULLETS: dict[float, Bullet] = {
    # Key is the bullet size
    0.5: Bullet(
        type=BULLET_TYPE_A,
        size=0.5,
        damage=1,
    ),
    1: Bullet(
        type=BULLET_TYPE_B,
        size=1,
        damage=1.5,
    ),
    3: Bullet(
        type=BULLET_TYPE_C,
        size=3,
        damage=3,
    ),
    4: Bullet(
        type=BULLET_TYPE_D,
        size=4,
        damage=2,
    ),
}


@dataclass
class Gun:
    name: str
    range: int
    power: int
    bullet_size: float


# Guns
SUBMACHINE_GUN = "Submachine Gun"
ASSAULT_RIFLE_GUN = "Assault Rifle"
PISTOL_GUN = "Pistol"
SHOTGUN_GUN = "Shotgun"
SNIPER_RIFLE_GUN = "Sniper Rifle"


GUNS: dict[str, Gun] = {
    SUBMACHINE_GUN: Gun(
        name=SUBMACHINE_GUN,
        range=100,
        power=10,
        bullet_size=0.5,
    ),
    ASSAULT_RIFLE_GUN: Gun(
        name=ASSAULT_RIFLE_GUN,
        range=200,
        power=20,
        bullet_size=1,
    ),
    PISTOL_GUN: Gun(
        name=PISTOL_GUN,
        range=80,
        power=8,
        bullet_size=0.5,
    ),
    SHOTGUN_GUN: Gun(
        name=SHOTGUN_GUN,
        range=50,
        power=40,
        bullet_size=4,
    ),
    SNIPER_RIFLE_GUN: Gun(
        name=SNIPER_RIFLE_GUN,
        range=1000,
        power=30,
        bullet_size=3,
    ),
}


class Shooter:
    def __init__(self) -> None:
        self.__gun: Gun | None = None
        self.__bullet: Bullet | None = None
        self.__bullet_count: int = 0

    def set_gun_by_name(self, name: str) -> None:
        gun = GUNS.get(name)
        if not gun:
            raise Exception(f"This Gun does not exist: '{name}'")
        self.__gun = gun

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        # Check for acquired gun
        if not self.__gun:
            raise Exception("Please select a gun before adding bullets")

        # Check for bullet count
        if count < 0:
            raise Exception("Count must be non-negative")

        # Check for requested bullet
        bullet = BULLETS.get(size)
        if not bullet:
            raise Exception(f"Couldn't found bullet with '{size}' caliber.")

        # Check for gun and bullet match
        if self.__gun.bullet_size != bullet.size:
            raise Exception(
                f"Requested '{size}' bullet can not be used with your selected gun"
            )

        # Add bullets
        self.__bullet = bullet
        self.__bullet_count += count

    def shoot_to_target(
        self, target_x: int, target_y: int, target_distance: int, aim_x: int, aim_y: int
    ) -> float:
        # Make sure gun and bullet are selected
        if not self.__gun or not self.__bullet:
            raise Exception("Please select a gun and bullet before shooting")

        # Make sure gun has ammo
        if not self.__bullet_count:
            raise Exception("No ammo! add more bullets")

        hit_damage: float = 0
        if (
            self.__gun.range >= target_distance and
            (target_x <= aim_x <= target_x + 10) and
            (target_y <= aim_y <= target_y + 10)
        ):
            hit_damage = self.__gun.power * self.__bullet.damage

        self.__bullet_count -= 1
        return hit_damage
