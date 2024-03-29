# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# Use CharaData to grab icon and conventional name from kirara
from django.db import models


class AnimEventSideOn(models.Model):
    card_id = models.IntegerField()
    side_on_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'anim_event_side_on'


class AnivCountData(models.Model):
    id = models.IntegerField(primary_key=True)
    aniv = models.IntegerField()
    count = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    day_flag = models.IntegerField()
    value1 = models.TextField()
    value2 = models.TextField()
    value3 = models.TextField()

    class Meta:
        managed = False
        db_table = 'aniv_count_data'


class AnnounceAnimData(models.Model):
    id = models.IntegerField(primary_key=True)
    asset_name = models.TextField()
    prefab_name = models.TextField()
    bgm_name = models.TextField()
    se_name = models.TextField()
    reset_node_list = models.TextField()

    class Meta:
        managed = False
        db_table = 'announce_anim_data'


class AnnounceAnimDetailData(models.Model):
    id = models.IntegerField(primary_key=True)
    key_index = models.IntegerField()
    key_name = models.TextField()
    skip_key_name = models.TextField()
    is_skip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'announce_anim_detail_data'
        unique_together = (('id', 'key_index'),)


class AnnounceData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    no = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    priority = models.IntegerField()
    parts_id = models.IntegerField()
    set_num = models.IntegerField()
    set_id_01 = models.IntegerField()
    set_id_02 = models.IntegerField()
    set_id_03 = models.IntegerField()
    set_id_04 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'announce_data'


class AtaponBetRate(models.Model):
    bet_type_id = models.IntegerField()
    bet_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_bet_rate'


class AtaponDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    live_detail_id = models.IntegerField()
    max_event_point = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    bet_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_detail'


class AtaponItemNumRate(models.Model):
    cost_stamina = models.IntegerField()
    event_item_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_item_num_rate'


class AtaponPointRankDisp(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_point_rank_disp'


class AtaponPointRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_point_rank_reward'


class AtaponPointReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    need_point = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_point_reward'


class AtaponScoreRankDisp(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_score_rank_disp'


class AtaponScoreRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_score_rank_reward'


class AtaponStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    type = models.IntegerField()
    open_event_point = models.IntegerField()
    next_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'atapon_story_detail'


class AvailableTimeType(models.Model):
    available_time_type = models.IntegerField()
    available_time_min = models.IntegerField()
    available_time_max = models.IntegerField()
    explain = models.TextField()

    class Meta:
        managed = False
        db_table = 'available_time_type'


class Banner(models.Model):
    banner_id = models.IntegerField()
    type = models.IntegerField()
    img_id = models.IntegerField()
    transition = models.IntegerField()
    page_index = models.IntegerField()
    order_num = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'banner'


class BirthdayBg(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    discription = models.TextField()
    sort = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'birthday_bg'


class BirthdayFrame(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    discription = models.TextField()
    sort = models.IntegerField()
    day_position = models.IntegerField()
    day_position_x = models.IntegerField()
    day_position_y = models.IntegerField()
    name_position = models.IntegerField()
    name_position_x = models.IntegerField()
    name_position_y = models.IntegerField()
    logo_position = models.IntegerField()
    logo_position_x = models.IntegerField()
    logo_position_y = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'birthday_frame'


class BusBlockData(models.Model):
    id = models.IntegerField(primary_key=True)
    area_id = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'bus_block_data'


class BusCharaBonus(models.Model):
    id = models.IntegerField(primary_key=True)
    bus_id = models.IntegerField()
    chara_list = models.TextField()
    bonus_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bus_chara_bonus'


class BusData(models.Model):
    id = models.IntegerField(primary_key=True)
    block_id = models.IntegerField()
    bus_name = models.TextField()
    bus_sp_type = models.IntegerField()
    event_id = models.IntegerField()
    sort = models.IntegerField()
    day_type = models.IntegerField()
    limit_type = models.IntegerField()
    limit_num = models.IntegerField()
    anime_type = models.IntegerField()
    anime_bg = models.IntegerField()
    open_category = models.IntegerField()
    open_value_1 = models.IntegerField()
    open_value_2 = models.IntegerField()
    cost_time = models.IntegerField()
    bus_type = models.IntegerField()
    rank_vo_condition = models.IntegerField()
    rank_da_condition = models.IntegerField()
    rank_vi_condition = models.IntegerField()
    get_money_min = models.IntegerField()
    get_money_max = models.IntegerField()
    get_exp_min = models.IntegerField()
    get_exp_max = models.IntegerField()
    get_fan_min = models.IntegerField()
    get_fan_max = models.IntegerField()
    get_event_pt_min = models.IntegerField()
    get_event_pt_max = models.IntegerField()
    drop_id = models.IntegerField()
    drop_level = models.IntegerField()
    bus_start_date = models.TextField()
    bus_end_date = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'bus_data'


class BusData2(models.Model):
    id = models.IntegerField(primary_key=True)
    block_id = models.IntegerField()
    bus_name = models.TextField()
    bus_sp_type = models.IntegerField()
    event_id = models.IntegerField()
    sort = models.IntegerField()
    day_type = models.IntegerField()
    limit_type = models.IntegerField()
    limit_num = models.IntegerField()
    anime_type = models.IntegerField()
    anime_bg = models.IntegerField()
    open_category = models.IntegerField()
    open_value_1 = models.IntegerField()
    open_value_2 = models.IntegerField()
    cost_time = models.IntegerField()
    bus_type = models.IntegerField()
    rank_vo_condition = models.IntegerField()
    rank_da_condition = models.IntegerField()
    rank_vi_condition = models.IntegerField()
    get_money_min = models.IntegerField()
    get_money_max = models.IntegerField()
    get_exp_min = models.IntegerField()
    get_exp_max = models.IntegerField()
    get_fan_min = models.IntegerField()
    get_fan_max = models.IntegerField()
    get_event_pt_min = models.IntegerField()
    get_event_pt_max = models.IntegerField()
    drop_id = models.IntegerField()
    drop_level = models.IntegerField()
    bus_start_date = models.TextField()
    bus_end_date = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'bus_data_2'


class BusDropRewardDisp(models.Model):
    id = models.IntegerField(primary_key=True)
    reward_icon_1 = models.TextField(blank=True, null=True)
    reward_text_1 = models.TextField(blank=True, null=True)
    reward_type_1 = models.IntegerField()
    reward_icon_2 = models.TextField(blank=True, null=True)
    reward_text_2 = models.TextField(blank=True, null=True)
    reward_type_2 = models.IntegerField()
    reward_icon_3 = models.TextField(blank=True, null=True)
    reward_text_3 = models.TextField(blank=True, null=True)
    reward_type_3 = models.IntegerField()
    reward_icon_4 = models.TextField(blank=True, null=True)
    reward_text_4 = models.TextField(blank=True, null=True)
    reward_type_4 = models.IntegerField()
    reward_icon_5 = models.TextField(blank=True, null=True)
    reward_text_5 = models.TextField(blank=True, null=True)
    reward_type_5 = models.IntegerField()
    reward_icon_6 = models.TextField(blank=True, null=True)
    reward_text_6 = models.TextField(blank=True, null=True)
    reward_type_6 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bus_drop_reward_disp'


class BusSet(models.Model):
    set_id = models.IntegerField()
    set_bus_id = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'bus_set'


class BusTutorial(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'bus_tutorial'


class CampaignBonus(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    value_1 = models.IntegerField()
    value_2 = models.IntegerField()
    value_3 = models.IntegerField()
    icon_img = models.IntegerField()
    day = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'campaign_bonus'


class CappuccinoData(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.IntegerField()
    title = models.TextField()
    title_top = models.TextField()
    chara_list = models.TextField()
    disp_order = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    file_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'cappuccino_data'


class CaravanData(models.Model):
    event_id = models.IntegerField()
    date = models.TextField()
    date_order = models.IntegerField()
    bonus_type = models.IntegerField()
    disp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'caravan_data'


class CaravanDetail(models.Model):
    event_id = models.IntegerField()
    difficulty = models.IntegerField()
    rare_drop_rate_1 = models.IntegerField()
    rare_drop_rate_bonus_1 = models.IntegerField()
    rare_drop_odds_1 = models.TextField()
    rare_drop_level_1 = models.IntegerField()
    rare_drop_rate_2 = models.IntegerField()
    rare_drop_rate_bonus_2 = models.IntegerField()
    rare_drop_odds_2 = models.TextField()
    rare_drop_level_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'caravan_detail'
        unique_together = (('event_id', 'difficulty'),)


class CaravanMainIdol(models.Model):
    event_id = models.IntegerField()
    main_idol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'caravan_main_idol'


class CardComments(models.Model):
    id = models.IntegerField(primary_key=True)
    use_type = models.IntegerField()
    index = models.IntegerField()
    voice_flag = models.IntegerField()
    discription = models.TextField()
    insert_word_type = models.IntegerField()
    story_cue_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_comments'
        unique_together = (('id', 'use_type', 'index'),)


class CardData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    chara_id = models.IntegerField()
    rarity = models.IntegerField()
    attribute = models.IntegerField()
    title_flag = models.IntegerField()
    evolution_id = models.IntegerField()
    series_id = models.IntegerField()
    pose = models.IntegerField()
    place = models.IntegerField()
    evolution_type = models.IntegerField()
    album_id = models.IntegerField()
    open_story_id = models.IntegerField()
    open_dress_id = models.IntegerField()
    skill_id = models.IntegerField()
    leader_skill_id = models.IntegerField()
    grow_type = models.IntegerField()
    hp_min = models.IntegerField()
    vocal_min = models.IntegerField()
    dance_min = models.IntegerField()
    visual_min = models.IntegerField()
    hp_max = models.IntegerField()
    vocal_max = models.IntegerField()
    dance_max = models.IntegerField()
    visual_max = models.IntegerField()
    bonus_hp = models.IntegerField()
    bonus_vocal = models.IntegerField()
    bonus_dance = models.IntegerField()
    bonus_visual = models.IntegerField()
    solo_live = models.IntegerField()
    star_lesson_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_data'


class CardEvolveItem(models.Model):
    evolve_type = models.IntegerField()
    evolve_item_1 = models.IntegerField()
    item_num_1 = models.IntegerField()
    evolve_item_2 = models.IntegerField()
    item_num_2 = models.IntegerField()
    evolve_item_3 = models.IntegerField()
    item_num_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_evolve_item'


class CardGalleryMotion(models.Model):
    id = models.IntegerField(primary_key=True)
    motion_1 = models.TextField()
    motion_2 = models.TextField()
    motion_3 = models.TextField()
    motion_4 = models.TextField()
    motion_5 = models.TextField()
    motion_6 = models.TextField()
    motion_7 = models.TextField()
    motion_8 = models.TextField()
    motion_9 = models.TextField()
    motion_10 = models.TextField()

    class Meta:
        managed = False
        db_table = 'card_gallery_motion'


class CardGrow(models.Model):
    id = models.IntegerField(primary_key=True)
    rarity = models.IntegerField()
    grow_type = models.IntegerField()
    level = models.IntegerField()
    grow = models.IntegerField()
    total_grow = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_grow'


class CardImagePosition(models.Model):
    id = models.IntegerField(primary_key=True)
    home_position_x = models.IntegerField()
    home_position_y = models.IntegerField()
    petit_position_x = models.IntegerField()
    petit_position_y = models.IntegerField()
    commu_position_x = models.IntegerField()
    commu_position_y = models.IntegerField()
    love_position_x = models.IntegerField()
    love_position_y = models.IntegerField()
    home_veritical_id = models.IntegerField()
    el_position_x = models.IntegerField()
    el_position_y = models.IntegerField()
    sns_position_x = models.IntegerField()
    sns_position_y = models.IntegerField()
    home_h_position_y = models.IntegerField()
    home_v_position_y = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_image_position'


class CardLevel(models.Model):
    level = models.IntegerField()
    rare_1_exp = models.IntegerField()
    rare_3_exp = models.IntegerField()
    rare_5_exp = models.IntegerField()
    rare_7_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_level'


class CardLevelTable(models.Model):
    level = models.IntegerField()
    next_exp = models.IntegerField()
    exp_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_level_table'


class CardLocation(models.Model):
    index = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'card_location'


class CardRarity(models.Model):
    rarity = models.IntegerField()
    base_max_level = models.IntegerField()
    add_max_level = models.IntegerField()
    max_love = models.IntegerField()
    base_give_money = models.IntegerField()
    base_give_exp = models.IntegerField()
    add_param = models.IntegerField()
    max_star_rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_rarity'


class CardStorageData(models.Model):
    id = models.IntegerField(primary_key=True)
    use_jewel = models.IntegerField()
    max_card_num = models.IntegerField()
    name = models.TextField()
    start_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'card_storage_data'


class CharaData(models.Model):
    chara_id = models.IntegerField()
    name = models.TextField()
    name_kana = models.TextField()
    age = models.IntegerField()
    home_town = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    body_size_1 = models.IntegerField()
    body_size_2 = models.IntegerField()
    body_size_3 = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    constellation = models.IntegerField()
    blood_type = models.IntegerField()
    hand = models.IntegerField()
    favorite = models.TextField()
    voice = models.TextField()
    model_height_id = models.IntegerField()
    model_weight_id = models.IntegerField()
    model_bust_id = models.IntegerField()
    model_skin_id = models.IntegerField()
    spine_size = models.IntegerField()
    personality = models.IntegerField()
    type = models.IntegerField()
    base_card_id = models.IntegerField()
    bus_vo_value = models.IntegerField()
    bus_da_value = models.IntegerField()
    bus_vi_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chara_data'


class CharaFacePosition(models.Model):
    chara_id = models.IntegerField()
    pose = models.IntegerField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chara_face_position'
        unique_together = (('chara_id', 'pose'),)


class CookieSwapBgmList(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    group_id = models.IntegerField()
    bgm = models.TextField()
    sound_length = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cookie_swap_bgm_list'


class CookieSwapMission(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    mission_id = models.IntegerField()
    discription = models.TextField()
    discription_detail = models.TextField()
    disp_order = models.IntegerField()
    step_group_id = models.IntegerField()
    step_order = models.IntegerField()
    condition_type = models.IntegerField()
    condition_value_1 = models.IntegerField()
    condition_value_2 = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    message_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'cookie_swap_mission'


class CookieSwapSchedule(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    type = models.IntegerField()
    bg_id = models.IntegerField()
    bgm_group_id = models.IntegerField()
    motion_id = models.IntegerField()
    disp = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'cookie_swap_schedule'


class CookieSwapStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    type = models.IntegerField()
    next_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cookie_swap_story_detail'


class CyalumeColor(models.Model):
    raw = models.TextField()

    class Meta:
        managed = False
        db_table = 'cyalume_color'


class DailyMission(models.Model):
    id = models.IntegerField(primary_key=True)
    daily_mission_id = models.IntegerField()
    group_id = models.IntegerField()
    discription = models.TextField()
    discription_detail = models.TextField()
    disp_order = models.IntegerField()
    condition_type = models.IntegerField()
    condition_value_day = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    message_id = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'daily_mission'


class DressAccPalette(models.Model):
    id = models.IntegerField(primary_key=True)
    dress_id = models.IntegerField()
    model_type = models.IntegerField()
    layer_id = models.IntegerField()
    color_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'dress_acc_palette'


class DressClosetData(models.Model):
    id = models.IntegerField(primary_key=True)
    unlock_dress_id = models.IntegerField()
    default_name = models.TextField()
    next_closet_id = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'dress_closet_data'


class DressColorData(models.Model):
    chara_id = models.IntegerField()
    dress_id = models.IntegerField()
    model_type = models.IntegerField()
    color_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dress_color_data'
        unique_together = (('chara_id', 'model_type', 'dress_id'),)


class DressData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    open_type = models.IntegerField()
    dress_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dress_data'


class DressPalette(models.Model):
    id = models.IntegerField(primary_key=True)
    dress_id = models.IntegerField()
    model_type = models.IntegerField()
    layer_id = models.IntegerField()
    color_code = models.TextField()
    lock_flag = models.IntegerField()
    disp_order = models.IntegerField()
    acc_index = models.TextField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'dress_palette'


class DressRandomPalette(models.Model):
    id = models.IntegerField(primary_key=True)
    dress_id = models.IntegerField()
    model_type = models.IntegerField()
    layer_id = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'dress_random_palette'


class DressTarget(models.Model):
    id = models.IntegerField(primary_key=True)
    target_chara_type = models.IntegerField()
    target_chara_1 = models.IntegerField()
    target_chara_2 = models.IntegerField()
    target_chara_3 = models.IntegerField()
    target_chara_4 = models.IntegerField()
    target_chara_5 = models.IntegerField()
    target_chara_6 = models.IntegerField()
    target_chara_7 = models.IntegerField()
    target_chara_8 = models.IntegerField()
    target_chara_9 = models.IntegerField()
    target_chara_10 = models.IntegerField()
    target_chara_11 = models.IntegerField()
    target_chara_12 = models.IntegerField()
    target_chara_13 = models.IntegerField()
    target_chara_14 = models.IntegerField()
    target_chara_15 = models.IntegerField()
    target_chara_16 = models.IntegerField()
    target_chara_17 = models.IntegerField()
    target_chara_18 = models.IntegerField()
    target_chara_19 = models.IntegerField()
    target_chara_20 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dress_target'


class ElDepartment(models.Model):
    department_id = models.IntegerField()
    department_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'el_department'


class ElLiveData(models.Model):
    live_data_id = models.IntegerField()
    department = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'el_live_data'


class Emblem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    discription = models.TextField()
    info_disp = models.IntegerField()
    disp_order = models.IntegerField()
    category = models.IntegerField()
    small_text = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'emblem'


class EventAccessReward(models.Model):
    event_id = models.IntegerField()
    event_type = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_access_reward'


class EventAvailable(models.Model):
    event_id = models.IntegerField()
    reward_id = models.IntegerField()
    recommend_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_available'
        unique_together = (('event_id', 'recommend_order'),)


class EventBetaData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    name = models.TextField()
    notice_start = models.TextField()
    event_start = models.TextField()
    second_half_start = models.TextField()
    event_end = models.TextField()
    calc_start = models.TextField()
    result_start = models.TextField()
    result_end = models.TextField()
    limit_flag = models.IntegerField()
    bg_type = models.IntegerField()
    bg_id = models.IntegerField()
    play_level_min = models.IntegerField()
    play_level_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_beta_data'


class EventData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    name = models.TextField()
    notice_start = models.TextField()
    event_start = models.TextField()
    second_half_start = models.TextField()
    event_end = models.TextField()
    calc_start = models.TextField()
    result_start = models.TextField()
    result_end = models.TextField()
    limit_flag = models.IntegerField()
    bg_type = models.IntegerField()
    bg_id = models.IntegerField()
    login_bonus_type = models.IntegerField()
    login_bonus_count = models.IntegerField()
    master_plus_support = models.IntegerField()
    item_re = models.IntegerField()
    point_re = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_data'


class EventLoginDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    count = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_login_detail'


class ExchangeData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    event_id = models.IntegerField()
    group_id = models.IntegerField()
    limit_num = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    discount_count = models.IntegerField()
    discount_cost_value = models.IntegerField()
    get_type = models.IntegerField()
    get_id = models.IntegerField()
    get_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'exchange_data'


class ExchangeShopItem(models.Model):
    id = models.IntegerField(primary_key=True)
    view_type = models.IntegerField()
    tab_id = models.IntegerField()
    disp_order = models.IntegerField()
    limit_type = models.IntegerField()
    limit_num = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    discount_count = models.IntegerField()
    discount_cost_value = models.IntegerField()
    get_type = models.IntegerField()
    get_id = models.IntegerField()
    get_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'exchange_shop_item'


class ExchangeShopItemBonus(models.Model):
    exchange_shop_item_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    item_sum = models.IntegerField()
    item_type_1 = models.IntegerField()
    item_id_1 = models.IntegerField()
    item_value_1 = models.IntegerField()
    item_type_2 = models.IntegerField()
    item_id_2 = models.IntegerField()
    item_value_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'exchange_shop_item_bonus'


class ExchangeShopTerm(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'exchange_shop_term'


class GachaAvailable(models.Model):
    gacha_id = models.IntegerField()
    step_num = models.IntegerField()
    reward_id = models.IntegerField()
    recommend_order = models.IntegerField()
    limited_flag = models.IntegerField()
    relative_odds = models.IntegerField()
    relative_sr_odds = models.IntegerField()
    up_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_available'
        unique_together = (('gacha_id', 'reward_id'),)


class GachaData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    dicription = models.TextField()
    type = models.IntegerField()
    type_detail = models.IntegerField()
    source = models.TextField()
    source_guarantee = models.TextField()
    draw_num = models.IntegerField()
    draw_guarantee_num = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    message_id = models.IntegerField()
    step_id = models.IntegerField()
    max_step = models.IntegerField()
    loop_num = models.IntegerField()
    reset_time = models.TextField(blank=True, null=True)
    draw_limit_single = models.IntegerField()
    first_cost_num_single = models.IntegerField()
    cost_num_single = models.IntegerField()
    reward_type_single_1 = models.IntegerField()
    reward_single_1 = models.IntegerField()
    reward_num_single_1 = models.IntegerField()
    reward_type_single_2 = models.IntegerField()
    reward_single_2 = models.IntegerField()
    reward_num_single_2 = models.IntegerField()
    reward_type_single_3 = models.IntegerField()
    reward_single_3 = models.IntegerField()
    reward_num_single_3 = models.IntegerField()
    reward_type_single_4 = models.IntegerField()
    reward_single_4 = models.IntegerField()
    reward_num_single_4 = models.IntegerField()
    draw_limit_multi = models.IntegerField()
    first_cost_num_multi = models.IntegerField()
    cost_num_multi = models.IntegerField()
    reward_type_multi_1 = models.IntegerField()
    reward_multi_1 = models.IntegerField()
    reward_num_multi_1 = models.IntegerField()
    reward_type_multi_2 = models.IntegerField()
    reward_multi_2 = models.IntegerField()
    reward_num_multi_2 = models.IntegerField()
    reward_type_multi_3 = models.IntegerField()
    reward_multi_3 = models.IntegerField()
    reward_num_multi_3 = models.IntegerField()
    reward_type_multi_4 = models.IntegerField()
    reward_multi_4 = models.IntegerField()
    reward_num_multi_4 = models.IntegerField()
    base_id = models.IntegerField()
    extend_id = models.IntegerField()
    gacha_l_g_id = models.IntegerField()
    gacha_bg_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_data'


class GachaLEList(models.Model):
    id = models.IntegerField(primary_key=True)
    g_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    sub_reward_type_1 = models.IntegerField()
    sub_reward_id_1 = models.IntegerField()
    sub_reward_value_1 = models.IntegerField()
    sub_reward_type_2 = models.IntegerField()
    sub_reward_id_2 = models.IntegerField()
    sub_reward_value_2 = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_l_e_list'


class GachaLGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.IntegerField()
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_l_group'


class GachaRate(models.Model):
    id = models.IntegerField(primary_key=True)
    step = models.IntegerField()
    nomal_ratio = models.IntegerField()
    rare_ratio = models.IntegerField()
    sr_ratio = models.IntegerField()
    ssr_ratio = models.IntegerField()
    nomal_ratio2 = models.IntegerField()
    rare_ratio2 = models.IntegerField()
    sr_ratio2 = models.IntegerField()
    ssr_ratio2 = models.IntegerField()
    name = models.TextField()
    name2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'gacha_rate'
        unique_together = (('id', 'step'),)


class GachaSpEffect(models.Model):
    gacha_id = models.IntegerField()
    card_id = models.IntegerField()
    gacha_effect_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_sp_effect'
        unique_together = (('gacha_id', 'card_id'),)


class GachaStep(models.Model):
    step_id = models.IntegerField()
    step_num = models.IntegerField()
    draw_num = models.IntegerField()
    draw_guarantee_num = models.IntegerField()
    cost_num_multi = models.IntegerField()
    source = models.TextField()
    source_guarantee = models.TextField(blank=True, null=True)
    reward_type_1 = models.IntegerField()
    reward_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()
    reward_type_4 = models.IntegerField()
    reward_4 = models.IntegerField()
    reward_num_4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacha_step'
        unique_together = (('step_id', 'step_num'),)


class GalleryMarker(models.Model):
    id = models.IntegerField(primary_key=True)
    marker_type = models.IntegerField()
    value = models.IntegerField()
    target_name = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'gallery_marker'


class GalleryMusicCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    condition_type = models.IntegerField()
    condition_id = models.IntegerField()
    condition_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gallery_music_condition'


class GalleryMusicList(models.Model):
    id = models.IntegerField(primary_key=True)
    disp_order = models.IntegerField()
    live_id = models.IntegerField()
    motion_id = models.IntegerField()
    fade_msec = models.IntegerField()
    cutt_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gallery_music_list'


class GalleryPoseCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    condition_type = models.IntegerField()
    condition_id = models.IntegerField()
    condition_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gallery_pose_condition'


class GalleryPoseList(models.Model):
    id = models.IntegerField(primary_key=True)
    disp_order = models.IntegerField()
    disp_name = models.TextField()
    motion_id = models.IntegerField()
    fade_msec = models.IntegerField()
    cutt_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gallery_pose_list'


class GalleryStageCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    source_id = models.IntegerField()
    condition_type = models.IntegerField()
    condition_id = models.IntegerField()
    condition_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gallery_stage_condition'


class GalleryStageList(models.Model):
    id = models.IntegerField(primary_key=True)
    disp_order = models.IntegerField()
    disp_name = models.TextField()
    bg_id = models.IntegerField()
    bg_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gallery_stage_list'


class GiftMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    discription = models.TextField()
    type_1 = models.IntegerField()
    type_2 = models.IntegerField()
    type_3 = models.IntegerField()
    type_4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gift_message'


class IdelCampaignData(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    campaign_start = models.TextField()
    second_half_start = models.TextField()
    campaign_end = models.TextField()
    calc_start = models.TextField()
    result_start = models.TextField()
    result_end = models.TextField()
    open_type_1 = models.IntegerField()
    open_id_1 = models.IntegerField()
    open_value_1 = models.IntegerField()
    open_type_2 = models.IntegerField()
    open_id_2 = models.IntegerField()
    open_value_2 = models.IntegerField()
    open_type_3 = models.IntegerField()
    open_id_3 = models.IntegerField()
    open_value_3 = models.IntegerField()
    bg_id = models.IntegerField()
    ui_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'idel_campaign_data'


class IdelVoteIdol(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    card_id = models.IntegerField()
    use_type = models.IntegerField()
    index = models.IntegerField()
    description = models.TextField()
    insert_word_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'idel_vote_idol'


class IndexLeaderSkillData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    skill_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'index_leader_skill_data'


class IndexSkillData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    skill_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'index_skill_data'


class IndividualTutorial(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.IntegerField()
    discription = models.TextField()

    class Meta:
        managed = False
        db_table = 'individual_tutorial'


class ItemCategory(models.Model):
    category_type = models.IntegerField()
    category_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_category'


class ItemData(models.Model):
    item_id = models.IntegerField()
    item_category = models.IntegerField()
    name = models.TextField()
    comment = models.TextField()
    comment2 = models.TextField()
    effect_type_1 = models.IntegerField()
    effect_value_1 = models.IntegerField()
    effect_type_2 = models.IntegerField()
    effect_value_2 = models.IntegerField()
    limit_num = models.IntegerField()
    icon_path = models.TextField(blank=True, null=True)
    start_date = models.TextField()
    end_date = models.TextField()
    sort = models.IntegerField()
    sold_price = models.IntegerField()
    sold_type = models.IntegerField()
    sold_sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_data'


class ItemGivePresent(models.Model):
    item_id = models.IntegerField()
    type = models.IntegerField()
    type_effect = models.IntegerField()
    add_love = models.IntegerField()
    type_bonus = models.IntegerField()
    birthday_bonus = models.IntegerField()
    disp_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_give_present'


class JewelShop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    discription = models.TextField()
    view_type = models.IntegerField()
    view_value = models.IntegerField()
    buy_period_start_type = models.IntegerField()
    buy_period_day = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    close_date = models.TextField()
    payment_only_flag = models.IntegerField()
    jewel_num = models.IntegerField()
    max_buy_num = models.IntegerField()
    buy_item_type_1 = models.IntegerField()
    buy_item_id_1 = models.IntegerField()
    buy_item_value_1 = models.IntegerField()
    buy_item_present_set_flag_1 = models.IntegerField()
    buy_item_type_2 = models.IntegerField()
    buy_item_id_2 = models.IntegerField()
    buy_item_value_2 = models.IntegerField()
    buy_item_present_set_flag_2 = models.IntegerField()
    buy_item_type_3 = models.IntegerField()
    buy_item_id_3 = models.IntegerField()
    buy_item_value_3 = models.IntegerField()
    buy_item_present_set_flag_3 = models.IntegerField()
    open_type_1 = models.IntegerField()
    open_id_1 = models.IntegerField()
    open_value_1 = models.IntegerField()
    open_type_2 = models.IntegerField()
    open_id_2 = models.IntegerField()
    open_value_2 = models.IntegerField()
    open_type_3 = models.IntegerField()
    open_id_3 = models.IntegerField()
    open_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jewel_shop'


class JewelShopConditions(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'jewel_shop_conditions'


class LatteArtData(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    chara_list = models.TextField()
    disp_order = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'latte_art_data'


class LeaderBoostRate(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    life_max = models.IntegerField()
    life_min = models.IntegerField()
    boost_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leader_boost_rate'


class LeaderBoostRateRe(models.Model):
    id = models.IntegerField(primary_key=True)
    term_id = models.IntegerField()
    life_max = models.IntegerField()
    life_min = models.IntegerField()
    boost_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leader_boost_rate_re'


class LeaderSkillBoostRate(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    leader_skill_id = models.IntegerField()
    rarity = models.IntegerField()
    boost_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leader_skill_boost_rate'


class LeaderSkillBoostRateRe(models.Model):
    id = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    leader_skill_id = models.IntegerField()
    rarity = models.IntegerField()
    boost_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leader_skill_boost_rate_re'


class LeaderSkillData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    explain = models.TextField()
    type = models.IntegerField()
    need_cute = models.IntegerField()
    need_cool = models.IntegerField()
    need_passion = models.IntegerField()
    target_attribute = models.IntegerField()
    target_param = models.IntegerField()
    up_type = models.IntegerField()
    up_value = models.IntegerField()
    special_id = models.IntegerField()
    need_chara = models.TextField()

    class Meta:
        managed = False
        db_table = 'leader_skill_data'


class LimitedMission(models.Model):
    id = models.IntegerField(primary_key=True)
    limited_mission_id = models.IntegerField()
    discription = models.TextField()
    discription_detail = models.TextField()
    disp_order = models.IntegerField()
    step_group_id = models.IntegerField()
    step_order = models.IntegerField()
    condition_type = models.IntegerField()
    condition_value_1 = models.IntegerField()
    condition_value_2 = models.TextField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    message_id = models.IntegerField()
    event_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'limited_mission'


class Live3DcharaSpring(models.Model):
    music_id = models.IntegerField()
    chara_id = models.IntegerField()
    dress_id = models.IntegerField()
    head_ratio = models.IntegerField()
    body_ratio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_3dchara_spring'
        unique_together = (('music_id', 'chara_id', 'dress_id'),)


class LiveAchievementReward(models.Model):
    id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    achievement_type = models.IntegerField()
    achievement_rank = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_3 = models.IntegerField()
    reward_num_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_achievement_reward'


class LiveBgReplace(models.Model):
    id = models.IntegerField(primary_key=True)
    season_id = models.IntegerField()
    set_type = models.IntegerField()
    before_bg_id = models.IntegerField()
    after_bg_id = models.IntegerField()
    include_live_id = models.IntegerField()
    exclude_live_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_bg_replace'


class LiveDailyBonusDrop(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.TextField()
    end_date = models.TextField()
    day = models.IntegerField()
    drop_reward_id = models.IntegerField()
    add_reward_odds = models.TextField()
    num = models.IntegerField()
    img = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'live_daily_bonus_drop'


class LiveDailyBonusParam(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.TextField()
    end_date = models.TextField()
    day = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_daily_bonus_param'


class LiveData(models.Model):
    id = models.IntegerField(primary_key=True)
    music_data_id = models.IntegerField()
    sort = models.IntegerField()
    difficulty_1 = models.IntegerField(unique=True)
    difficulty_2 = models.IntegerField(unique=True)
    difficulty_3 = models.IntegerField(unique=True)
    difficulty_4 = models.IntegerField(unique=True)
    circle_type = models.IntegerField()
    live_bg = models.IntegerField()
    cyalume = models.IntegerField()
    chara_all_flag = models.IntegerField()
    chara_id = models.TextField()
    type = models.IntegerField()
    sp_type = models.IntegerField()
    jacket_id = models.IntegerField()
    prp_flag = models.IntegerField()
    release_type = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    event_type = models.IntegerField()
    difficulty_5 = models.IntegerField()
    member_number = models.IntegerField()
    difficulty_101 = models.IntegerField()
    v_mv = models.IntegerField()
    difficulty_11 = models.IntegerField()
    difficulty_12 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_data'


class LiveDataElcp(models.Model):
    id = models.IntegerField(primary_key=True)
    music_data_id = models.IntegerField()
    jacket_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_data_elcp'


class LiveDataPosition(models.Model):
    live_data_id = models.IntegerField()
    position_num = models.IntegerField()
    chara_position_1 = models.IntegerField()
    dress_position_1 = models.IntegerField()
    chara_position_2 = models.IntegerField()
    dress_position_2 = models.IntegerField()
    chara_position_3 = models.IntegerField()
    dress_position_3 = models.IntegerField()
    chara_position_4 = models.IntegerField()
    dress_position_4 = models.IntegerField()
    chara_position_5 = models.IntegerField()
    dress_position_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_data_position'


class LiveDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    live_data_id = models.IntegerField()
    difficulty_type = models.IntegerField()
    stamina = models.IntegerField()
    speed = models.IntegerField()
    level_vocal = models.IntegerField()
    level_dance = models.IntegerField()
    level_visual = models.IntegerField()
    rank_s_condition = models.IntegerField()
    get_money = models.IntegerField()
    get_exp = models.IntegerField()
    need_param = models.IntegerField()
    get_love = models.IntegerField()
    open_category = models.IntegerField()
    open_value = models.IntegerField()
    next_category_1 = models.IntegerField()
    next_value_1 = models.IntegerField()
    next_category_2 = models.IntegerField()
    next_value_2 = models.IntegerField()
    next_category_3 = models.IntegerField()
    next_value_3 = models.IntegerField()
    rare_drop_rate = models.IntegerField()
    rare_drop_odds = models.TextField()
    rare_drop_level = models.IntegerField()
    drop_s_type = models.IntegerField()
    drop_s_level = models.IntegerField()
    drop_a_type = models.IntegerField()
    drop_b_type = models.IntegerField()
    drop_c_type = models.IntegerField()
    achievement_reward_type = models.IntegerField()
    combo_s_condition = models.IntegerField()
    combo_a_condition = models.IntegerField()
    combo_b_condition = models.IntegerField()
    combo_c_condition = models.IntegerField()
    clear_s_condition = models.IntegerField()
    clear_a_condition = models.IntegerField()
    clear_b_condition = models.IntegerField()
    clear_c_condition = models.IntegerField()
    rare_drop_rate_guerrilla = models.IntegerField()
    rare_drop_odds_guerrilla = models.TextField()
    rare_drop_level_guerrilla = models.IntegerField()
    drop_s_type_guerrilla = models.IntegerField()
    drop_s_level_guerrilla = models.IntegerField()
    drop_a_type_guerrilla = models.IntegerField()
    drop_b_type_guerrilla = models.IntegerField()
    drop_c_type_guerrilla = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_detail'


class LiveNotesNumber(models.Model):
    live_id = models.IntegerField()
    difficulty = models.IntegerField()
    notes_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'live_notes_number'
        unique_together = (('live_id', 'difficulty'),)


class LiveSeasonData(models.Model):
    id = models.IntegerField(primary_key=True)
    season_name = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'live_season_data'


class LiveTutorial(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'live_tutorial'


class LoadingData(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    resource_id = models.IntegerField()
    rate = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'loading_data'


class LoginBonusData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    type = models.IntegerField()
    count_num = models.IntegerField()
    rap = models.IntegerField()
    img = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'login_bonus_data'


class LoginBonusDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    rap = models.IntegerField()
    count = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'login_bonus_detail'


class LotteryResource(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    banner_id = models.IntegerField()
    bg_id = models.IntegerField()
    campaign_anim_id = models.IntegerField()
    result_anim_id = models.IntegerField()
    campaign_anim_bgm = models.TextField()
    result_anim_bgm = models.TextField()

    class Meta:
        managed = False
        db_table = 'lottery_resource'


class MasterPlusGroup1(models.Model):
    id = models.IntegerField(primary_key=True)
    live_data_id = models.IntegerField()
    live_detail_id = models.IntegerField()
    term_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_plus_group_1'


class MasterPlusGroup2(models.Model):
    id = models.IntegerField(primary_key=True)
    live_data_id = models.IntegerField()
    live_detail_id = models.IntegerField()
    term_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_plus_group_2'


class MasterPlusGroup3(models.Model):
    id = models.IntegerField(primary_key=True)
    live_data_id = models.IntegerField()
    live_detail_id = models.IntegerField()
    term_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_plus_group_3'


class MasterPlusTerm(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.TextField()
    end_date = models.TextField()
    master_plus_group = models.IntegerField()
    notice_start_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'master_plus_term'


class MedleyData(models.Model):
    event_id = models.IntegerField()
    event_live_id = models.IntegerField()
    medley_type = models.IntegerField()
    cute_probability = models.IntegerField()
    cool_probability = models.IntegerField()
    passion_probability = models.IntegerField()
    all_probability = models.IntegerField()
    stamina_debut = models.IntegerField()
    stamina_regular = models.IntegerField()
    stamina_pro = models.IntegerField()
    stamina_master = models.IntegerField()
    vocal_rate = models.IntegerField()
    dance_rate = models.IntegerField()
    visual_rate = models.IntegerField()
    all_attribute_permil_1 = models.IntegerField()
    all_attribute_permil_2 = models.IntegerField()
    encore_get_point_master_plus = models.IntegerField()
    encore_get_point_master = models.IntegerField()
    encore_get_point_pro = models.IntegerField()
    encore_get_point_regular = models.IntegerField()
    encore_get_point_debut = models.IntegerField()
    story_flag = models.IntegerField()
    event_anime_type = models.IntegerField()
    event_anime_audience = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_data'


class MedleyDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    type = models.IntegerField()
    difficulty_type = models.IntegerField()
    rare_drop_rate = models.IntegerField()
    rare_drop_odds = models.TextField()
    rare_drop_level = models.IntegerField()
    drop_s_type = models.IntegerField()
    drop_s_level = models.IntegerField()
    drop_a_type = models.IntegerField()
    drop_b_type = models.IntegerField()
    drop_c_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_detail'
        unique_together = (('type', 'difficulty_type'),)


class MedleyGetPointEncoreRate(models.Model):
    event_id = models.IntegerField()
    difficulty = models.IntegerField()
    rank_s_rate = models.IntegerField()
    rank_a_rate = models.IntegerField()
    rank_b_rate = models.IntegerField()
    rank_c_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_get_point_encore_rate'
        unique_together = (('event_id', 'difficulty'),)


class MedleyGetPointRate(models.Model):
    event_id = models.IntegerField()
    difficulty = models.IntegerField()
    rank_s_rate = models.IntegerField()
    rank_a_rate = models.IntegerField()
    rank_b_rate = models.IntegerField()
    rank_c_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_get_point_rate'
        unique_together = (('event_id', 'difficulty'),)


class MedleyGrooveChange(models.Model):
    event_id = models.IntegerField()
    change_num = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_groove_change'
        unique_together = (('event_id', 'change_num'),)


class MedleyLiveExclude(models.Model):
    event_id = models.IntegerField()
    live_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_live_exclude'
        unique_together = (('event_id', 'live_id'),)


class MedleyPointRankDisp(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_point_rank_disp'


class MedleyPointRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_point_rank_reward'


class MedleyPointReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    need_point = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_point_reward'


class MedleyScoreRankDisp(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_score_rank_disp'


class MedleyScoreRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_score_rank_reward'


class MedleyScoreRate(models.Model):
    event_id = models.IntegerField()
    score_rate = models.IntegerField()
    vabration_max_rate = models.IntegerField()
    combo_s_rate = models.IntegerField()
    combo_a_rate = models.IntegerField()
    combo_b_rate = models.IntegerField()
    combo_c_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_score_rate'


class MedleyStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    type = models.IntegerField()
    open_event_point = models.IntegerField()
    next_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_story_detail'


class MedleyVibrationChange(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    difficulty_type = models.IntegerField()
    tap_judge = models.IntegerField()
    change_type = models.IntegerField()
    increase_decrease = models.IntegerField()
    change_value = models.IntegerField()
    rank_s_condition_adjust = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_vibration_change'
        unique_together = (('event_id', 'difficulty_type', 'tap_judge'),)


class MedleyVibrationRank(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    difficulty_type = models.IntegerField()
    score_rank = models.IntegerField()
    encore_type = models.IntegerField()
    vibrartion_min = models.IntegerField()
    vibrartion_max = models.IntegerField()
    get_base_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medley_vibration_rank'


class MemorialStoryOpen(models.Model):
    chapter = models.IntegerField()
    open_fan_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'memorial_story_open'


class MilleFeuilleCardComment(models.Model):
    id = models.IntegerField(primary_key=True)
    comment_id = models.IntegerField()
    use_type = models.IntegerField()
    index = models.IntegerField()
    voice_flag = models.IntegerField()
    description = models.TextField()
    insert_word_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mille_feuille_card_comment'


class MilleFeuillePreset0001(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mille_feuille_preset_0001'


class MilleFeuillePreset0002(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mille_feuille_preset_0002'


class MilleFeuillePreset0003(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mille_feuille_preset_0003'


class MilleFeuilleStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    next_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mille_feuille_story_detail'


class MissionTargetLive(models.Model):
    day_id = models.IntegerField()
    live_type_1 = models.IntegerField()
    live_type_2 = models.IntegerField()
    live_type_3 = models.IntegerField()
    live_type_4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mission_target_live'


class MoPRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    month = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mo_p_rank_reward'


class MusicData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    bpm = models.IntegerField()
    composer = models.TextField()
    lyricist = models.TextField()
    sound_offset = models.IntegerField()
    sound_length = models.IntegerField()
    name_sort = models.IntegerField()
    name_kana = models.TextField()

    class Meta:
        managed = False
        db_table = 'music_data'


class MusicDataExclude(models.Model):
    id = models.IntegerField(primary_key=True)
    music_data_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'music_data_exclude'


class MusicInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    discription = models.TextField()
    android_url = models.TextField()
    ios_url = models.TextField()

    class Meta:
        managed = False
        db_table = 'music_info'


class MusicNameSort(models.Model):
    id = models.IntegerField(primary_key=True)
    sort_id = models.IntegerField()
    name_kana = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'music_name_sort'


class MusicVocalist(models.Model):
    music_data_id = models.IntegerField()
    chara_id = models.IntegerField()
    disp_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'music_vocalist'
        unique_together = (('music_data_id', 'chara_id'),)


class MvListData(models.Model):
    stage_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    stage_group_id = models.IntegerField()
    day = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'mv_list_data'


class MvListDetail(models.Model):
    set_list_id = models.IntegerField()
    stage_id = models.IntegerField()
    disp_order = models.IntegerField()
    live_data_id = models.IntegerField()
    free_open_flag = models.IntegerField()
    chara_position_1 = models.IntegerField()
    dress_position_1 = models.IntegerField()
    chara_position_2 = models.IntegerField()
    dress_position_2 = models.IntegerField()
    chara_position_3 = models.IntegerField()
    dress_position_3 = models.IntegerField()
    chara_position_4 = models.IntegerField()
    dress_position_4 = models.IntegerField()
    chara_position_5 = models.IntegerField()
    dress_position_5 = models.IntegerField()
    chara_sub = models.TextField()

    class Meta:
        managed = False
        db_table = 'mv_list_detail'


class MvListPerformer(models.Model):
    id = models.IntegerField(primary_key=True)
    stage_id = models.IntegerField()
    chara_id = models.IntegerField()
    play_start = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mv_list_performer'


class NamecardBg(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    discription = models.TextField()
    sort = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'namecard_bg'


class NormalMission(models.Model):
    id = models.IntegerField(primary_key=True)
    normal_mission_id = models.IntegerField()
    discription = models.TextField()
    discription_detail = models.TextField()
    disp_order = models.IntegerField()
    step_group_id = models.IntegerField()
    step_order = models.IntegerField()
    condition_type = models.IntegerField()
    condition_value_1 = models.IntegerField()
    condition_value_2 = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    message_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'normal_mission'


class OnetimeStory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    story_id = models.IntegerField()
    transition = models.IntegerField()
    page_index = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    play_order = models.IntegerField(unique=True)
    notice_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'onetime_story'


class PanelMissionCompReward(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    rap = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    message_id = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'panel_mission_comp_reward'


class PanelMissionDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    disp_order = models.IntegerField()
    discription = models.TextField()
    rap = models.IntegerField()
    condition_type = models.IntegerField()
    condition_value = models.IntegerField()
    total_value_flag = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    message_id = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'panel_mission_detail'


class PartyData(models.Model):
    event_id = models.IntegerField()
    cute_probability = models.IntegerField()
    cool_probability = models.IntegerField()
    passion_probability = models.IntegerField()
    all_probability = models.IntegerField()
    stamina_debut = models.IntegerField()
    stamina_regular = models.IntegerField()
    stamina_pro = models.IntegerField()
    stamina_master = models.IntegerField()
    center_boost_rate = models.IntegerField()
    singer_boost_rate = models.IntegerField()
    dancer_boost_rate = models.IntegerField()
    actor_boost_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_data'


class PartyDataRe(models.Model):
    term_id = models.IntegerField()
    type = models.IntegerField()
    name = models.TextField()
    notice_start = models.TextField()
    event_start = models.TextField()
    second_half_start = models.TextField()
    event_end = models.TextField()
    calc_start = models.TextField()
    result_start = models.TextField()
    result_end = models.TextField()
    limit_flag = models.IntegerField()
    bg_type = models.IntegerField()
    bg_id = models.TextField()
    login_bonus_type = models.IntegerField()
    login_bonus_count = models.IntegerField()
    master_plus_support = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_data_re'


class PartyDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    type = models.IntegerField()
    difficulty_type = models.IntegerField()
    score_rate = models.IntegerField()
    get_pt_rate = models.IntegerField()
    scramble_pt_rate = models.IntegerField()
    failure_penalty_rate = models.IntegerField()
    single_penalty_rate = models.IntegerField()
    ceiling_score = models.IntegerField()
    rare_drop_rate = models.IntegerField()
    rare_drop_odds = models.TextField()
    rare_drop_level = models.IntegerField()
    drop_s_type = models.IntegerField()
    drop_s_level = models.IntegerField()
    drop_a_type = models.IntegerField()
    drop_b_type = models.IntegerField()
    drop_c_type = models.IntegerField()
    over_ceiling_rate = models.IntegerField()
    ceiling_score_2 = models.IntegerField()
    score_weight_rate = models.IntegerField()
    appeal_weight_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_detail'


class PartyDetailRe(models.Model):
    id = models.IntegerField(primary_key=True)
    term_id = models.IntegerField()
    type = models.IntegerField()
    difficulty_type = models.IntegerField()
    score_rate = models.IntegerField()
    get_pt_rate = models.IntegerField()
    scramble_pt_rate = models.IntegerField()
    failure_penalty_rate = models.IntegerField()
    single_penalty_rate = models.IntegerField()
    ns_rate = models.IntegerField()
    ceiling_score = models.IntegerField()
    over_ceiling_rate = models.IntegerField()
    ceiling_score_2 = models.IntegerField()
    score_weight_rate = models.IntegerField()
    appeal_weight_rate = models.IntegerField()
    rare_drop_rate = models.IntegerField()
    rare_drop_odds = models.TextField()
    rare_drop_level = models.IntegerField()
    drop_s_type = models.IntegerField()
    drop_s_level = models.IntegerField()
    drop_a_type = models.IntegerField()
    drop_b_type = models.IntegerField()
    drop_c_type = models.IntegerField()
    tour_drop_rate = models.IntegerField()
    tour_drop_odds = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_detail_re'


class PartyExchangeData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    term_id = models.IntegerField()
    group_id = models.IntegerField()
    limit_num = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    discount_count = models.IntegerField()
    discount_cost_value = models.IntegerField()
    get_type = models.IntegerField()
    get_id = models.IntegerField()
    get_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'party_exchange_data'


class PartyFlowerData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    consume_pt = models.IntegerField()
    flower_type = models.IntegerField()
    order_num = models.IntegerField()
    party_term_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_data'


class PartyFlowerLvType(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    lv = models.IntegerField()
    flower_num = models.IntegerField()
    preset_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_lv_type'


class PartyFlowerPresetType0001(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0001'


class PartyFlowerPresetType0002(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0002'


class PartyFlowerPresetType0003(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0003'


class PartyFlowerPresetType0004(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0004'


class PartyFlowerPresetType0005(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0005'


class PartyFlowerPresetType0006(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0006'


class PartyFlowerPresetType0007(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0007'


class PartyFlowerPresetType0008(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0008'


class PartyFlowerPresetType0009(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0009'


class PartyFlowerPresetType0010(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0010'


class PartyFlowerPresetType0011(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0011'


class PartyFlowerPresetType0012(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_flower_preset_type_0012'


class PartyLoginDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    term_id = models.IntegerField()
    login_type = models.IntegerField()
    count = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'party_login_detail'


class PartyMainIdol(models.Model):
    event_id = models.IntegerField()
    main_idol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_main_idol'


class PartyPointReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    need_point = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    loop_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_point_reward'


class PartyTerm(models.Model):
    id = models.IntegerField(primary_key=True)
    cute_probability = models.IntegerField()
    cool_probability = models.IntegerField()
    passion_probability = models.IntegerField()
    all_probability = models.IntegerField()
    stamina_debut = models.IntegerField()
    stamina_regular = models.IntegerField()
    stamina_pro = models.IntegerField()
    stamina_master = models.IntegerField()
    center_boost_rate = models.IntegerField()
    singer_boost_rate = models.IntegerField()
    dancer_boost_rate = models.IntegerField()
    actor_boost_rate = models.IntegerField()
    exchange_item_id = models.IntegerField()
    party_flower_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    stamina_master_plus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_term'


class PartyTheme(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    order_num = models.IntegerField()
    reward_type = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'party_theme'


class PartyThemePreset0001(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_theme_preset_0001'


class PartyThemePreset0002(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_theme_preset_0002'


class PartyThemePreset0003(models.Model):
    id = models.IntegerField(primary_key=True)
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'party_theme_preset_0003'


class PotentialConditionFan(models.Model):
    id = models.IntegerField(primary_key=True)
    condition_fan = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_condition_fan'


class PotentialGrowthCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    potential_level = models.IntegerField()
    attribute = models.IntegerField()
    condition_type_1 = models.IntegerField()
    condition_id_1 = models.IntegerField()
    condition_value_1 = models.IntegerField()
    condition_type_2 = models.IntegerField()
    condition_id_2 = models.IntegerField()
    condition_value_2 = models.IntegerField()
    condition_type_3 = models.IntegerField()
    condition_id_3 = models.IntegerField()
    condition_value_3 = models.IntegerField()
    condition_type_4 = models.IntegerField()
    condition_id_4 = models.IntegerField()
    condition_value_4 = models.IntegerField()
    condition_type_5 = models.IntegerField()
    condition_id_5 = models.IntegerField()
    condition_value_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_growth_condition'


class PotentialValueDa(models.Model):
    potential_level = models.IntegerField()
    value_rare_1 = models.IntegerField()
    value_rare_3 = models.IntegerField()
    value_rare_5 = models.IntegerField()
    value_rare_7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_value_da'


class PotentialValueLi(models.Model):
    potential_level = models.IntegerField()
    value_rare_1 = models.IntegerField()
    value_rare_3 = models.IntegerField()
    value_rare_5 = models.IntegerField()
    value_rare_7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_value_li'


class PotentialValueSk(models.Model):
    potential_level = models.IntegerField()
    value_rare_1 = models.IntegerField()
    value_rare_3 = models.IntegerField()
    value_rare_5 = models.IntegerField()
    value_rare_7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_value_sk'


class PotentialValueVi(models.Model):
    potential_level = models.IntegerField()
    value_rare_1 = models.IntegerField()
    value_rare_3 = models.IntegerField()
    value_rare_5 = models.IntegerField()
    value_rare_7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_value_vi'


class PotentialValueVo(models.Model):
    potential_level = models.IntegerField()
    value_rare_1 = models.IntegerField()
    value_rare_3 = models.IntegerField()
    value_rare_5 = models.IntegerField()
    value_rare_7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'potential_value_vo'


class PremiumScDetail(models.Model):
    item_id = models.IntegerField()
    jewel_shop_id = models.IntegerField()
    use_period_day = models.IntegerField()
    all_user_use_end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'premium_sc_detail'


class PremiumScList(models.Model):
    id = models.IntegerField(primary_key=True)
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    sub_reward_type_1 = models.IntegerField()
    sub_reward_id_1 = models.IntegerField()
    sub_reward_value_1 = models.IntegerField()
    sub_reward_type_2 = models.IntegerField()
    sub_reward_id_2 = models.IntegerField()
    sub_reward_value_2 = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'premium_sc_list'


class ProbabilityType(models.Model):
    probability_type = models.IntegerField()
    probability_min = models.IntegerField()
    probability_max = models.IntegerField()
    explain = models.TextField()

    class Meta:
        managed = False
        db_table = 'probability_type'


class PrpReward(models.Model):
    id = models.IntegerField(primary_key=True)
    condition = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prp_reward'


class QualityAndroid(models.Model):
    raw = models.TextField()

    class Meta:
        managed = False
        db_table = 'quality_android'


class RailArea(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    name = models.TextField()
    group_id = models.IntegerField()
    rap_id = models.IntegerField()
    total_circle = models.IntegerField()
    release_area_id = models.IntegerField()
    loop_flag = models.IntegerField()
    bg_id = models.IntegerField()
    map_type_1 = models.IntegerField()
    map_value_1 = models.IntegerField()
    map_type_2 = models.IntegerField()
    map_value_2 = models.IntegerField()
    target_type_1 = models.IntegerField()
    target_value_1 = models.IntegerField()
    target_type_2 = models.IntegerField()
    target_value_2 = models.IntegerField()
    target_type_3 = models.IntegerField()
    target_value_3 = models.IntegerField()
    target_obj_id = models.IntegerField()
    step_bonus = models.IntegerField()
    chara_id = models.IntegerField()
    chara_bonus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_area'


class RailAreaBonus(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    group_id = models.IntegerField()
    rap_id = models.IntegerField()
    map_type_1 = models.IntegerField()
    map_value_1 = models.IntegerField()
    map_type_2 = models.IntegerField()
    map_value_2 = models.IntegerField()
    map_bonus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_area_bonus'


class RailAreaComment(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    group_id = models.IntegerField()
    rap_id = models.IntegerField()
    comment_id = models.IntegerField()
    use_type = models.IntegerField()
    description = models.TextField()
    insert_word_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_area_comment'


class RailCardComment(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    comment_id = models.IntegerField()
    use_type = models.IntegerField()
    index = models.IntegerField()
    description = models.TextField()
    insert_word_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_card_comment'


class RailCircleData(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    area_id = models.IntegerField()
    circle_id = models.IntegerField()
    circle_type = models.IntegerField()
    bonus_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_circle_data'


class RailCircleReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    group_id = models.IntegerField()
    rap_id = models.IntegerField()
    circle_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_circle_reward'


class RailConditionText(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    use_type = models.IntegerField()
    condition_type = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'rail_condition_text'


class RailData(models.Model):
    event_id = models.IntegerField()
    event_live_id = models.IntegerField()
    item_id = models.IntegerField()
    start_group_id = models.IntegerField()
    story_flag = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'rail_data'


class RailStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    type = models.IntegerField()
    group_id = models.IntegerField()
    open_rap_id = models.IntegerField()
    next_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_story_detail'


class RailTargetReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    group_id = models.IntegerField()
    rap_id = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rail_target_reward'


class RmAssets(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'rm_assets'


class RoomBgm(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.TextField()
    end_date = models.TextField()
    morning_bgm = models.TextField()
    evening_bgm = models.TextField()
    night_bgm = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_bgm'


class RoomEffect(models.Model):
    id = models.IntegerField(primary_key=True)
    effect_detail = models.TextField()
    effect_type = models.IntegerField()
    insert_word_type = models.IntegerField()
    value_type = models.IntegerField()
    cute_vo = models.IntegerField()
    cute_da = models.IntegerField()
    cute_vi = models.IntegerField()
    cool_vo = models.IntegerField()
    cool_da = models.IntegerField()
    cool_vi = models.IntegerField()
    passion_vo = models.IntegerField()
    passion_da = models.IntegerField()
    passion_vi = models.IntegerField()
    get_money = models.IntegerField()
    get_fan = models.IntegerField()
    get_photo = models.IntegerField()
    max_photo = models.IntegerField()
    get_parcel = models.IntegerField()
    max_parcel = models.IntegerField()
    parcel_odds_improve = models.IntegerField()
    get_money_add = models.IntegerField()
    get_live = models.IntegerField()
    sound_booth = models.IntegerField()
    get_ticket = models.IntegerField()
    max_ticket = models.IntegerField()
    ticket_odds_improve = models.IntegerField()
    get_gift = models.IntegerField()
    max_gift = models.IntegerField()
    is_draw = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_effect'


class RoomGuestCharacter(models.Model):
    id = models.IntegerField(primary_key=True)
    guest_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    anime_walk_max = models.IntegerField()
    anime_wait_max = models.IntegerField()
    is_voice_load = models.IntegerField()
    card_comment_id = models.IntegerField()
    card_comment_num = models.IntegerField()
    card_comment_load_max = models.IntegerField()
    voice_anime_common_max = models.IntegerField()
    voice_anime_ai_max = models.IntegerField()
    voice_anime_touch_max = models.IntegerField()
    incidence = models.IntegerField()
    type = models.IntegerField()
    value1 = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_guest_character'


class RoomIdolExtension(models.Model):
    card_id = models.IntegerField()
    is_spine = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_idol_extension'


class RoomIdolPresent(models.Model):
    id = models.IntegerField(primary_key=True)
    reward_date = models.TextField()
    receive_limit_date = models.TextField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_idol_present'


class RoomItem(models.Model):
    raw = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item'


class RoomItemAnime(models.Model):
    animeid = models.IntegerField(db_column='AnimeID')  # Field name made lowercase.
    charaaitype = models.IntegerField(db_column='CharaAiType')  # Field name made lowercase.
    drawparts = models.IntegerField(db_column='DrawParts')  # Field name made lowercase.
    isbase = models.IntegerField(db_column='IsBase')  # Field name made lowercase.
    isbasespine = models.IntegerField(db_column='IsBaseSpine')  # Field name made lowercase.
    isbasereverse = models.IntegerField(db_column='IsBaseReverse')  # Field name made lowercase.
    isfront = models.IntegerField(db_column='IsFront')  # Field name made lowercase.
    isfrontspine = models.IntegerField(db_column='IsFrontSpine', blank=True, null=True)  # Field name made lowercase.
    isfrontreverse = models.IntegerField(db_column='IsFrontReverse', blank=True, null=True)  # Field name made lowercase.
    minloopnum = models.IntegerField(db_column='MinLoopNum')  # Field name made lowercase.
    maxloopnum = models.IntegerField(db_column='MaxLoopNum')  # Field name made lowercase.
    isreservepos = models.IntegerField(db_column='IsReservePos')  # Field name made lowercase.
    posx1 = models.IntegerField(db_column='PosX1', blank=True, null=True)  # Field name made lowercase.
    posy1 = models.IntegerField(db_column='PosY1', blank=True, null=True)  # Field name made lowercase.
    posx2 = models.IntegerField(db_column='PosX2', blank=True, null=True)  # Field name made lowercase.
    posy2 = models.IntegerField(db_column='PosY2', blank=True, null=True)  # Field name made lowercase.
    posx3 = models.IntegerField(db_column='PosX3', blank=True, null=True)  # Field name made lowercase.
    posy3 = models.IntegerField(db_column='PosY3', blank=True, null=True)  # Field name made lowercase.
    posx4 = models.IntegerField(db_column='PosX4', blank=True, null=True)  # Field name made lowercase.
    posy4 = models.IntegerField(db_column='PosY4', blank=True, null=True)  # Field name made lowercase.
    posx5 = models.IntegerField(db_column='PosX5', blank=True, null=True)  # Field name made lowercase.
    posy5 = models.IntegerField(db_column='PosY5', blank=True, null=True)  # Field name made lowercase.
    efinid = models.IntegerField(db_column='EfInID', blank=True, null=True)  # Field name made lowercase.
    efinanimeid = models.IntegerField(db_column='EfInAnimeID', blank=True, null=True)  # Field name made lowercase.
    efmidid = models.IntegerField(db_column='EfMidID', blank=True, null=True)  # Field name made lowercase.
    efmidanimeid = models.IntegerField(db_column='EfMidAnimeID', blank=True, null=True)  # Field name made lowercase.
    efoutid = models.IntegerField(db_column='EfOutID', blank=True, null=True)  # Field name made lowercase.
    efoutanimeid = models.IntegerField(db_column='EfOutAnimeID', blank=True, null=True)  # Field name made lowercase.
    animesein = models.TextField(db_column='AnimeSeIn', blank=True, null=True)  # Field name made lowercase.
    animesemid = models.TextField(db_column='AnimeSeMid', blank=True, null=True)  # Field name made lowercase.
    animeseout = models.TextField(db_column='AnimeSeOut', blank=True, null=True)  # Field name made lowercase.
    tapanime1 = models.TextField(db_column='TapAnime1', blank=True, null=True)  # Field name made lowercase.
    tapanime2 = models.TextField(db_column='TapAnime2', blank=True, null=True)  # Field name made lowercase.
    tapanime3 = models.TextField(db_column='TapAnime3', blank=True, null=True)  # Field name made lowercase.
    tapanime4 = models.TextField(db_column='TapAnime4', blank=True, null=True)  # Field name made lowercase.
    tapanime5 = models.TextField(db_column='TapAnime5', blank=True, null=True)  # Field name made lowercase.
    randomanime1 = models.TextField(db_column='RandomAnime1', blank=True, null=True)  # Field name made lowercase.
    randomanime2 = models.TextField(db_column='RandomAnime2', blank=True, null=True)  # Field name made lowercase.
    randomanime3 = models.TextField(db_column='RandomAnime3', blank=True, null=True)  # Field name made lowercase.
    randomanime4 = models.TextField(db_column='RandomAnime4', blank=True, null=True)  # Field name made lowercase.
    randomanime5 = models.TextField(db_column='RandomAnime5', blank=True, null=True)  # Field name made lowercase.
    playanime = models.IntegerField(db_column='PlayAnime')  # Field name made lowercase.
    randomparam = models.IntegerField(db_column='RandomParam')  # Field name made lowercase.
    setype = models.IntegerField(db_column='SeType')  # Field name made lowercase.
    seloadno = models.IntegerField(db_column='SeLoadNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room_item_anime'
        unique_together = (('animeid', 'charaaitype'),)


class RoomItemAnnouncement(models.Model):
    id = models.IntegerField(primary_key=True)
    announcement_start = models.TextField()
    announcement_end = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item_announcement'


class RoomItemCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.TextField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item_category'


class RoomItemCollision(models.Model):
    raw = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item_collision'


class RoomItemDetail(models.Model):
    room_item_id = models.IntegerField()
    level = models.IntegerField()
    item_detail = models.TextField()
    effect_value_1 = models.IntegerField()
    effect_value_2 = models.IntegerField()
    effect_value_3 = models.IntegerField()
    lvup_trigger_type = models.IntegerField()
    lvup_trigger_id = models.IntegerField()
    lvup_trigger_value = models.IntegerField()
    lvup_item1_type = models.IntegerField()
    lvup_item1_id = models.IntegerField()
    lvup_item1_num = models.IntegerField()
    lvup_item2_type = models.IntegerField()
    lvup_item2_id = models.IntegerField()
    lvup_item2_num = models.IntegerField()
    lvup_time = models.IntegerField()
    animation_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item_detail'
        unique_together = (('room_item_id', 'level'),)


class RoomItemExtension(models.Model):
    raw = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item_extension'


class RoomItemGift(models.Model):
    id = models.IntegerField(primary_key=True)
    room_item_id = models.IntegerField()
    reward_date = models.TextField()
    receive_limit_date = models.TextField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    image = models.TextField()
    save_new_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item_gift'


class RoomItemGridData(models.Model):
    grid_x = models.IntegerField()
    grid_y = models.IntegerField()
    is_move = models.IntegerField()
    move_up = models.IntegerField()
    move_down = models.IntegerField()
    move_left = models.IntegerField()
    move_right = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item_grid_data'
        unique_together = (('grid_x', 'grid_y'),)


class RoomItemOffset(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    invert = models.IntegerField()
    origin_x = models.IntegerField()
    origin_y = models.IntegerField()
    origin_w = models.IntegerField()
    origin_h = models.IntegerField()
    resize_x = models.IntegerField()
    resize_y = models.IntegerField()
    resize_w = models.IntegerField()
    resize_h = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item_offset'
        unique_together = (('id', 'level', 'invert'),)


class RoomItemPreset(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_item_preset'


class RoomItemTheme(models.Model):
    id = models.IntegerField(primary_key=True)
    theme_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_item_theme'


class RoomSetData(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    value = models.IntegerField()
    shop_start = models.TextField()
    shop_end = models.TextField()
    flag_new = models.IntegerField()
    sort = models.IntegerField()
    bonus = models.TextField()

    class Meta:
        managed = False
        db_table = 'room_set_data'


class RoomSetDetail00001(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00001'


class RoomSetDetail00002(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00002'


class RoomSetDetail00003(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00003'


class RoomSetDetail00004(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00004'


class RoomSetDetail00005(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00005'


class RoomSetDetail00006(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00006'


class RoomSetDetail00007(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00007'


class RoomSetDetail00008(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00008'


class RoomSetDetail00009(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00009'


class RoomSetDetail00010(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00010'


class RoomSetDetail00011(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00011'


class RoomSetDetail00012(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00012'


class RoomSetDetail00013(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00013'


class RoomSetDetail00014(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00014'


class RoomSetDetail00015(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00015'


class RoomSetDetail00016(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00016'


class RoomSetDetail00017(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00017'


class RoomSetDetail00018(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00018'


class RoomSetDetail00019(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00019'


class RoomSetDetail00020(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00020'


class RoomSetDetail00021(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00021'


class RoomSetDetail00022(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00022'


class RoomSetDetail00023(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00023'


class RoomSetDetail00024(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00024'


class RoomSetDetail00025(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00025'


class RoomSetDetail00026(models.Model):
    id = models.IntegerField(primary_key=True)
    set_id = models.IntegerField()
    serial_id = models.IntegerField()
    item_id = models.IntegerField()
    item_type = models.IntegerField()
    level = models.IntegerField()
    dir_type = models.IntegerField()
    pos_no = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_detail00026'


class Shop(models.Model):
    id = models.IntegerField(primary_key=True)
    store_product_id = models.TextField()
    name = models.TextField()
    text = models.TextField()
    price = models.IntegerField()
    charge_jewel_num = models.IntegerField()
    free_jewel_num = models.IntegerField()
    start_time = models.TextField()
    end_time = models.TextField()
    limit_type = models.IntegerField()
    limit_num = models.IntegerField()
    disp_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop'


class SkillBoostType(models.Model):
    id = models.IntegerField(primary_key=True)
    skill_value = models.IntegerField()
    target_type = models.IntegerField()
    boost_value_1 = models.IntegerField()
    boost_value_2 = models.IntegerField()
    boost_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_boost_type'


class SkillData(models.Model):
    id = models.IntegerField(primary_key=True)
    skill_name = models.TextField()
    explain = models.TextField()
    skill_type = models.IntegerField()
    judge_type = models.IntegerField()
    skill_trigger_type = models.IntegerField()
    skill_trigger_value = models.IntegerField()
    cutin_type = models.IntegerField()
    condition = models.IntegerField()
    value = models.IntegerField()
    probability_type = models.IntegerField()
    available_time_type = models.IntegerField()
    value_2 = models.IntegerField()
    value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_data'


class SkillLevelup(models.Model):
    diff_rarity = models.IntegerField()
    skill_up_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_levelup'


class SkillLevelupItem(models.Model):
    diff_rarity = models.IntegerField()
    skill_up_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_levelup_item'


class SkillLifeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    life_value = models.IntegerField()
    type_01_value = models.IntegerField()
    type_02_value = models.IntegerField()
    type_03_value = models.IntegerField()
    type_04_value = models.IntegerField()
    type_05_value = models.IntegerField()
    type_06_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_life_value'


class SpCampaignData(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    notice_start = models.TextField()
    campaign_start = models.TextField()
    second_half_start = models.TextField()
    campaign_end = models.TextField()
    calc_start = models.TextField()
    result_start = models.TextField()
    result_end = models.TextField()

    class Meta:
        managed = False
        db_table = 'sp_campaign_data'


class SpCampaignReward(models.Model):
    id = models.IntegerField(primary_key=True)
    campaign_id = models.IntegerField()
    rank = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    lot_num = models.IntegerField()
    condition_level = models.IntegerField()
    reward_limit_day = models.IntegerField()
    remaining_lot_flag = models.IntegerField()
    message_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_campaign_reward'


class SpLoginBonusBefore(models.Model):
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    chara_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sp_login_bonus_before'


class SpLoginBonusDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    count = models.IntegerField()
    navi_id = models.IntegerField()
    navi_comment = models.TextField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    anim_name = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'sp_login_bonus_detail'


class SpLoginPosition(models.Model):
    day_count = models.IntegerField()
    chara_index = models.IntegerField()
    frame_type = models.IntegerField()
    frame_position_x = models.IntegerField()
    frame_position_y = models.IntegerField()
    text_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'sp_login_position'
        unique_together = (('day_count', 'chara_index'),)


class SpecialCardSkillData(models.Model):
    id = models.IntegerField(primary_key=True)
    explain = models.TextField()
    judge_type = models.IntegerField()
    skill_trigger_type = models.IntegerField()
    skill_trigger_value = models.IntegerField()
    condition = models.IntegerField()
    value = models.IntegerField()
    probability_type = models.IntegerField()
    available_time_type = models.IntegerField()
    value_2 = models.IntegerField()
    value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'special_card_skill_data'


class SpecialSkillData(models.Model):
    special_id = models.IntegerField()
    name = models.TextField()
    explain = models.TextField()
    type = models.IntegerField()
    need_cute = models.IntegerField()
    need_cool = models.IntegerField()
    need_passion = models.IntegerField()
    target_attribute = models.IntegerField()
    target_param = models.IntegerField()
    up_type = models.IntegerField()
    up_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'special_skill_data'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class StampData(models.Model):
    id = models.IntegerField(primary_key=True)
    discription = models.TextField()
    use_type = models.IntegerField()
    category = models.IntegerField()
    setting_type = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'stamp_data'


class StampDataRe(models.Model):
    id = models.IntegerField(primary_key=True)
    discription = models.TextField()
    use_type = models.IntegerField()
    category = models.IntegerField()
    setting_type = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'stamp_data_re'


class StarLessonType(models.Model):
    id = models.IntegerField(primary_key=True)
    min_rank = models.IntegerField()
    max_rank = models.IntegerField()
    min_money = models.IntegerField()
    max_money = models.IntegerField()
    growth_money = models.IntegerField()
    min_drop = models.IntegerField()
    max_drop = models.IntegerField()
    growth_drop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'star_lesson_type'


class StarRankEffect(models.Model):
    star_rank = models.IntegerField()
    type_1_drop_rate = models.IntegerField()
    type_1_money_rate = models.IntegerField()
    type_2_drop_rate = models.IntegerField()
    type_2_money_rate = models.IntegerField()
    type_3_drop_rate = models.IntegerField()
    type_3_money_rate = models.IntegerField()
    type_4_drop_rate = models.IntegerField()
    type_4_money_rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'star_rank_effect'


class SterntalerStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    data_1 = models.IntegerField()
    data_2 = models.IntegerField()
    data_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sterntaler_story_detail'


class SterntalerStoryUnit(models.Model):
    id = models.IntegerField(primary_key=True)
    data_1 = models.IntegerField()
    data_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sterntaler_story_unit'


class StoryCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    chara_type = models.IntegerField()
    chara_id = models.IntegerField()
    title = models.TextField()
    sub_title = models.TextField()
    disp_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'story_category'
        unique_together = (('type', 'disp_order'),)


class StoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    story_detail_type = models.IntegerField()
    chapter = models.IntegerField()
    title = models.TextField()
    sub_title = models.TextField()
    disp_order = models.IntegerField(unique=True)
    dialog_id = models.IntegerField()
    open_level = models.IntegerField()
    open_live_id = models.IntegerField()
    open_live_difficulty = models.IntegerField()
    open_card_id = models.IntegerField()
    open_chara_id = models.IntegerField()
    next_detail_id = models.IntegerField()
    is_release = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_id_1 = models.IntegerField()
    reward_value_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_id_2 = models.IntegerField()
    reward_value_2 = models.IntegerField()
    reward_type_3 = models.IntegerField()
    reward_id_3 = models.IntegerField()
    reward_value_3 = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    open_mission_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'story_detail'


class StoryExchangeData(models.Model):
    id = models.IntegerField(primary_key=True)
    story_detail_id = models.IntegerField()
    cost_type = models.IntegerField()
    cost_id = models.IntegerField()
    cost_value = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'story_exchange_data'


class TextData(models.Model):
    category = models.IntegerField()
    index = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'text_data'
        unique_together = (('category', 'index'),)


class Tips(models.Model):
    id = models.IntegerField(primary_key=True)
    tips_type = models.IntegerField()
    value = models.IntegerField()
    index = models.IntegerField()
    title = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'tips'


class TitlePattern(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    rate = models.IntegerField()
    bg = models.IntegerField()
    bgm = models.TextField()
    voice_file = models.TextField()
    voice_key = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    logo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'title_pattern'


class TotalLoginBonus(models.Model):
    id = models.IntegerField(primary_key=True)
    days = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'total_login_bonus'


class TourArea(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    name = models.TextField()
    base_id = models.IntegerField()
    max_audience = models.IntegerField()
    need_area_value_1 = models.IntegerField()
    need_area_value_2 = models.IntegerField()
    need_area_value_3 = models.IntegerField()
    need_area_value_4 = models.IntegerField()
    need_area_value_5 = models.IntegerField()
    need_area_value_6 = models.IntegerField()
    need_area_value_7 = models.IntegerField()
    is_open_area_id_1 = models.IntegerField()
    is_open_area_id_2 = models.IntegerField()
    is_open_area_id_3 = models.IntegerField()
    is_open_area_id_4 = models.IntegerField()
    is_open_area_id_5 = models.IntegerField()
    is_open_area_id_6 = models.IntegerField()
    is_open_area_id_7 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_area'


class TourAudienceReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    need_audience = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_audience_reward'


class TourData(models.Model):
    event_id = models.IntegerField()
    event_live_id = models.IntegerField()
    release_area_id_master_plus = models.IntegerField()
    story_flag = models.IntegerField()
    trend_live_get_audience = models.IntegerField()
    get_point_success = models.IntegerField()
    get_point_failure = models.IntegerField()
    get_audience_success = models.IntegerField()
    get_audience_failure = models.IntegerField()
    tour_title = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'tour_data'


class TourLiveCorrection(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    difficulty = models.IntegerField()
    score_rate = models.IntegerField()
    ceiling_score = models.IntegerField()
    need_param = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_live_correction'


class TourLiveDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    area_id = models.IntegerField()
    area_index = models.IntegerField()
    area_place_index = models.IntegerField()
    name = models.TextField()
    cost = models.IntegerField()
    live_num = models.IntegerField()
    need_live_id = models.IntegerField()
    condition_type_1 = models.IntegerField()
    condition_value_1 = models.IntegerField()
    condition_type_2 = models.IntegerField()
    condition_value_2 = models.IntegerField()
    condition_type_3 = models.IntegerField()
    condition_value_3 = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    rare_drop_rate = models.IntegerField()
    rare_drop_odds = models.TextField()
    rare_drop_level = models.IntegerField()
    drop_s_type = models.IntegerField()
    drop_s_level = models.IntegerField()
    drop_a_type = models.IntegerField()
    drop_b_type = models.IntegerField()
    drop_c_type = models.IntegerField()
    difficulty_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_live_detail'


class TourLiveExclude(models.Model):
    event_id = models.IntegerField()
    live_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_live_exclude'
        unique_together = (('event_id', 'live_id'),)


class TourLiveItem(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    need_money = models.IntegerField()
    effect_type = models.IntegerField()
    effect_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_live_item'


class TourPointReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    need_point = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_point_reward'


class TourScoreRankDisp(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_score_rank_disp'


class TourScoreRankReward(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    rank_min = models.IntegerField()
    rank_max = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_value = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_score_rank_reward'


class TourStoryDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    type = models.IntegerField()
    open_event_point = models.IntegerField()
    next_detail_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_story_detail'


class TourTrendLive(models.Model):
    id = models.IntegerField(primary_key=True)
    event_id = models.IntegerField()
    live_data_id_1 = models.IntegerField()
    live_data_id_2 = models.IntegerField()
    live_data_id_3 = models.IntegerField()
    live_data_id_4 = models.IntegerField()
    live_data_id_5 = models.IntegerField()
    live_data_id_6 = models.IntegerField()
    live_data_id_7 = models.IntegerField()
    live_data_id_8 = models.IntegerField()
    live_data_id_9 = models.IntegerField()
    live_data_id_10 = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()

    class Meta:
        managed = False
        db_table = 'tour_trend_live'


class UserLevel(models.Model):
    level = models.IntegerField()
    stamina = models.IntegerField()
    max_friend = models.IntegerField()
    total_exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_level'


class UserRank(models.Model):
    id = models.IntegerField(primary_key=True)
    rank_name = models.TextField()
    condition = models.IntegerField()
    reward_type_1 = models.IntegerField()
    reward_1 = models.IntegerField()
    reward_num_1 = models.IntegerField()
    reward_type_2 = models.IntegerField()
    reward_2 = models.IntegerField()
    reward_num_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_rank'


class WeeklyMission(models.Model):
    id = models.IntegerField(primary_key=True)
    weekly_mission_id = models.IntegerField()
    base_day = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    discription = models.TextField()
    discription_detail = models.TextField()
    disp_order = models.IntegerField()
    condition_type = models.IntegerField()
    condition_value_day = models.IntegerField()
    condition_value_interval = models.IntegerField()
    condition_total_value_week = models.IntegerField()
    reward_type = models.IntegerField()
    reward_id = models.IntegerField()
    reward_num = models.IntegerField()
    message_id = models.IntegerField()
    add_value_1 = models.IntegerField()
    add_value_2 = models.IntegerField()
    add_value_3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'weekly_mission'
