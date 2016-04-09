from django.db import models


class BlitzUsers(models.Model):
    account_id = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname


class StatsUserVehicle(models.Model):
    account_id = models.CharField(max_length=255)
    last_battle_time = models.CharField(max_length=255)
    trees_cut = models.CharField(max_length=255)
    in_garage_updated = models.CharField(max_length=255)
    max_frags = models.CharField(max_length=255)
    frags = models.CharField(max_length=255)
    mark_of_mastery = models.CharField(max_length=255)
    battle_life_time = models.CharField(max_length=255)
    in_garage = models.CharField(max_length=255)
    tank_id = models.CharField(max_length=255)
    all_spotted = models.CharField(max_length=255)
    all_hits = models.CharField(max_length=255)
    all_frags = models.CharField(max_length=255)
    all_max_xp = models.CharField(max_length=255)
    all_wins = models.CharField(max_length=255)
    all_losses = models.CharField(max_length=255)
    all_capture_points = models.CharField(max_length=255)
    all_battles = models.CharField(max_length=255)
    all_damage_dealt = models.CharField(max_length=255)
    all_damage_received = models.CharField(max_length=255)
    all_max_frags = models.CharField(max_length=255)
    all_shots = models.CharField(max_length=255)
    all_frags8p = models.CharField(max_length=255)
    all_xp = models.CharField(max_length=255)
    all_win_and_survived = models.CharField(max_length=255)
    all_survived_battles = models.CharField(max_length=255)
    all_dropped_capture_points = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname
