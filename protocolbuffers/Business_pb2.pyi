from protocolbuffers._ProtobufTypes import Message
from protocolbuffers._ProtobufTypes import RepeatedCompositeFieldContainer
from enum import IntEnum

from protocolbuffers.UI_pb2 import *
from protocolbuffers.ResourceKey_pb2 import *
from protocolbuffers.Localization_pb2 import *
from protocolbuffers.SimObjectAttributes_pb2 import *
from protocolbuffers.Clubs_pb2 import *
from protocolbuffers.S4Common_pb2 import *


class ReviewIconData(Message):
    # __init__
    title: 'LocalizedString'
    desc: 'LocalizedString'
    icon: 'ResourceKey'


class ReviewDataUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    score: 'float'  # float32
    review_count: 'int'  # int32
    icons: 'RepeatedCompositeFieldContainer[ReviewIconData]'


class BusinessSummaryEntry(Message):
    class EntryType(IntEnum):
        NORMAL: 'BusinessSummaryEntry.EntryType' = 0
        TOTAL: 'BusinessSummaryEntry.EntryType' = 1
        SUB_TOTAL: 'BusinessSummaryEntry.EntryType' = 2
        NORMAL_WITH_BEVEL: 'BusinessSummaryEntry.EntryType' = 3
        NORMAL_WITH_SUBTITLE: 'BusinessSummaryEntry.EntryType' = 4
        TOTAL_WITH_BUCKS: 'BusinessSummaryEntry.EntryType' = 5
        CUSTOM_BACKGROUND_ITEM: 'BusinessSummaryEntry.EntryType' = 6

    NORMAL = EntryType.NORMAL
    TOTAL = EntryType.TOTAL
    SUB_TOTAL = EntryType.SUB_TOTAL
    NORMAL_WITH_BEVEL = EntryType.NORMAL_WITH_BEVEL
    NORMAL_WITH_SUBTITLE = EntryType.NORMAL_WITH_SUBTITLE
    TOTAL_WITH_BUCKS = EntryType.TOTAL_WITH_BUCKS
    CUSTOM_BACKGROUND_ITEM = EntryType.CUSTOM_BACKGROUND_ITEM

    # __init__
    entry_name: 'LocalizedString'
    entry_value: 'LocalizedString'
    entry_type: 'BusinessSummaryEntry.EntryType'
    entry_subtitle: 'LocalizedString'
    entry_bucks: 'LocalizedString'
    tooltip: 'LocalizedString'
    is_locked: 'bool'


class BusinessRule(Message):
    class BusinessRuleState(IntEnum):
        DISABLED: 'BusinessRule.BusinessRuleState' = 0
        ENABLED: 'BusinessRule.BusinessRuleState' = 1
        BROKEN: 'BusinessRule.BusinessRuleState' = 2

    DISABLED = BusinessRuleState.DISABLED
    ENABLED = BusinessRuleState.ENABLED
    BROKEN = BusinessRuleState.BROKEN

    # __init__
    rule_id: 'int'  # fixed uint64
    state: 'BusinessRule.BusinessRuleState'
    state_change_cooldown_time: 'int'  # uint32


class RestaurantBusinessDataUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    ingredient_chosen: 'int'  # uint32
    is_ingredient_unlocked: 'bool'
    advertising_chosen: 'int'  # uint32


class RetailBusinessDataUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64


class VetClinicBusinessDataUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    advertising_chosen: 'int'  # uint32
    is_quality_unlocked: 'bool'
    quality_chosen: 'int'  # uint32


class RentalUnitBusinessDataUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    overdue_rent: 'int'  # uint32
    max_rent: 'int'  # uint32
    tenant_alert_visible: 'bool'
    is_grace_period: 'bool'
    unit_rating_alert_state: 'int'  # int32
    house_description_id: 'int'  # fixed uint64


class SmallBusinessDataUpdate(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    description: 'str'
    customer_rules: 'RepeatedCompositeFieldContainer[ClubConductRule]'
    attendance_criteria: 'RepeatedCompositeFieldContainer[ClubCriteria]'
    attendance_sale_mode: 'int'  # uint32
    allowed_zone_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class TemplateHouseholdSelectedStatus(Message):
    # __init__
    template_guid: 'int'  # uint32
    household_selected: 'bool'


class TenantApplicationServicePersistence(Message):
    # __init__
    template_selected_map: 'RepeatedCompositeFieldContainer[TemplateHouseholdSelectedStatus]'


class TenantApplicationDesiredRent(Message):
    # __init__
    star_rating: 'int'  # int32
    rent_multiplier: 'float'  # float32


class TenantApplicationNumHouseholds(Message):
    # __init__
    star_rating: 'int'  # int32
    num_households: 'int'  # int32


class TenantApplicationHouseholdOccupant(Message):
    # __init__
    occupant_age: 'int'  # uint32
    occupant_species: 'int'  # uint32


class TenantApplicationHousehold(Message):
    # __init__
    household_name: 'str'
    household_occupants: 'RepeatedCompositeFieldContainer[TenantApplicationHouseholdOccupant]'
    desired_beds: 'int'  # int32
    desired_rent: 'RepeatedCompositeFieldContainer[TenantApplicationDesiredRent]'
    household_id: 'int'  # fixed uint64
    zone_id: 'int'  # fixed uint64
    household_name_key: 'int'  # uint32


class PotentialTenantApplicationHouseholds(Message):
    # __init__
    potential_households: 'RepeatedCompositeFieldContainer[TenantApplicationHousehold]'
    num_households: 'RepeatedCompositeFieldContainer[TenantApplicationNumHouseholds]'


class CustomerBusinessData(Message):
    # __init__
    customer_id: 'int'  # fixed uint64
    customer_buffs: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    buff_bucket_totals: 'RepeatedCompositeFieldContainer[BusinessBuffBucketTotal]'
    last_buff_id: 'int'  # fixed uint64


class EmployeeBusinessData(Message):
    class EmployeeData():
        # __init__
        employee_type: 'int'  # fixed uint64
        employee_id: 'int'  # fixed uint64

    class BusinessUniformData():
        # __init__
        employee_type: 'int'  # fixed uint64
        employee_uniform_data: 'MannequinSimData'

    class BusinessDataPayroll():
        # __init__
        sim_id: 'int'  # fixed uint64
        clock_in_time: 'int'  # uint64
        payroll_data: 'RepeatedCompositeFieldContainer[EmployeeBusinessData.BusinessDataPayroll.BusinessDataPayrollEntry]'
        career_level_guid: 'int'  # fixed uint64
        hours_worked: 'float'  # float32

    # __init__
    employee_data: 'RepeatedCompositeFieldContainer[EmployeeBusinessData.EmployeeData]'
    daily_employee_wages: 'int'  # int32
    employee_uniforms_male: 'RepeatedCompositeFieldContainer[EmployeeBusinessData.BusinessUniformData]'
    employee_uniforms_female: 'RepeatedCompositeFieldContainer[EmployeeBusinessData.BusinessUniformData]'
    employee_payroll: 'RepeatedCompositeFieldContainer[EmployeeBusinessData.BusinessDataPayroll]'
    daily_household_employee_wages: 'int'  # int32
    employee_type: 'int'  # fixed uint64
    employee_id: 'int'  # fixed uint64
    employee_type: 'int'  # fixed uint64
    employee_uniform_data: 'MannequinSimData'
    sim_id: 'int'  # fixed uint64
    clock_in_time: 'int'  # uint64
    payroll_data: 'RepeatedCompositeFieldContainer[EmployeeBusinessData.BusinessDataPayroll.BusinessDataPayrollEntry]'
    career_level_guid: 'int'  # fixed uint64
    hours_worked: 'float'  # float32


class SetBusinessData(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    name: 'str'
    is_open: 'bool'
    funds: 'int'  # int32
    review_data: 'ReviewDataUpdate'
    net_profit: 'int'  # int32
    icon: 'ResourceKey'
    markup_chosen: 'float'  # float32
    time_opened: 'int'  # uint64
    daily_revenue: 'int'  # int32
    daily_items_sold: 'int'  # int32
    daily_outgoing_costs: 'int'  # int32
    open_time: 'int'  # uint64
    daily_customers_served: 'int'  # uint32
    minimum_employee_requirements_met: 'bool'
    sim_id: 'int'  # fixed uint64
    default_dynamic_area_type: 'int'  # int32
    total_open_hours: 'int'  # uint32
    total_customers_served: 'int'  # uint32
    dynamic_area_types: 'RepeatedCompositeFieldContainer[int]'  # int32
    restaurant_data: 'RestaurantBusinessDataUpdate'
    retail_data: 'RetailBusinessDataUpdate'
    vet_clinic_data: 'VetClinicBusinessDataUpdate'
    rental_unit_data: 'RentalUnitBusinessDataUpdate'
    small_business_data: 'SmallBusinessDataUpdate'
    allowed_zone_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class BusinessMarkupUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    markup_chosen: 'float'  # float32
    sim_id: 'int'  # fixed uint64


class BusinessAdvertisementUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    advertisement_chosen: 'int'  # uint32


class BusinessDailyCustomersServedUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    daily_customers_served: 'int'  # uint32


class BusinessIsOpenUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    is_open: 'bool'
    time_opened: 'int'  # uint64
    sim_id: 'int'  # fixed uint64


class BusinessFundsUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    available_funds: 'int'  # int32
    vfx_amount: 'int'  # int32


class BusinessProfitUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    net_profit: 'int'  # int32
    sim_id: 'int'  # fixed uint64


class BusinessDailyItemsSoldUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    daily_items_sold: 'int'  # uint32


class BusinessDailyCostsUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    daily_outgoing_costs: 'int'  # uint32


class BusinessSummaryDialog(Message):
    # __init__
    business_data: 'SetBusinessData'
    lines_entries: 'RepeatedCompositeFieldContainer[BusinessSummaryEntry]'
    employees: 'RepeatedCompositeFieldContainer[ManageEmployeeRowData]'
    is_global_overview: 'bool'
    hide_review_stars: 'bool'
    show_sim_bubble: 'bool'
    show_staff_report: 'bool'
    show_custom_stats_container: 'bool'
    stats_custom_background: 'str'
    stats_custom_tooltip: 'LocalizedString'
    default_highlight_finances_help: 'bool'


class BusinessCustomerUpdate(Message):
    # __init__
    sim_id: 'int'  # fixed uint64


class BusinessCustomerReviewEvent(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    event_name: 'LocalizedString'
    event_icon: 'ResourceKey'
    is_event_positive: 'bool'


class ManageEmployeesDialog(Message):
    # __init__
    hiring_sim_id: 'int'  # fixed uint64
    jobs: 'RepeatedCompositeFieldContainer[ManageEmployeeJobData]'


class ManageEmployeeJobData(Message):
    # __init__
    employees: 'RepeatedCompositeFieldContainer[ManageEmployeeRowData]'
    available_sims: 'RepeatedCompositeFieldContainer[ManageEmployeeRowData]'
    open_slots: 'int'  # uint32
    locked_slots: 'int'  # uint32
    job_type: 'int'  # uint32
    job_name: 'LocalizedString'
    job_icon: 'IconInfo'


class ManageEmployeeRowData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    satisfaction_string: 'LocalizedString'
    pay: 'int'  # uint32
    skill_data: 'RepeatedCompositeFieldContainer[ManageEmployeeSkillData]'
    current_career_level: 'int'  # uint32
    max_career_level: 'int'  # uint32


class BusinessBuffBucketTotal(Message):
    # __init__
    buff_bucket: 'int'  # uint32
    buff_bucket_total: 'float'  # float32


class RestaurantSaveData(Message):
    # __init__
    ingredient_quality_enum: 'int'  # uint32
    profit_per_meal_queue: 'RepeatedCompositeFieldContainer[int]'  # uint32
    dining_spot_count: 'int'  # uint32
    advertising_type: 'int'  # uint32


class VetClinicSaveData(Message):
    # __init__
    advertising_type: 'int'  # uint32
    quality_type: 'int'  # uint32
    profit_per_treatment_queue: 'RepeatedCompositeFieldContainer[int]'  # uint32
    exam_table_count: 'int'  # uint32


class RentalUnitSaveData(Message):
    # __init__
    overdue_rent: 'int'  # uint32
    max_rent: 'int'  # uint32
    tenant_alert_visible: 'bool'
    rent_overdue_time: 'int'  # uint64
    due_rent: 'int'  # uint32
    paid_rent_awaiting_transfer: 'int'  # uint32
    has_tenant_ever_paid_rent: 'bool'
    has_tenant_ever_received_rent_bill: 'bool'


class SmallBusinessSaveData(Message):
    # __init__
    small_business_income_data: 'SmallBusinessIncomeData'
    bucks_data: 'RepeatedCompositeFieldContainer[BucksData]'
    customer_rules: 'RepeatedCompositeFieldContainer[ClubConductRule]'
    attendance_criteria: 'RepeatedCompositeFieldContainer[ClubCriteria]'
    name: 'str'
    description: 'str'
    icon: 'ResourceKey'
    employee_data: 'RepeatedCompositeFieldContainer[SmallBusinessEmployeeData]'
    business_xp_on_open: 'int'  # uint32
    had_ticket_machine_once: 'bool'
    had_employee_once: 'bool'
    had_light_retail_surface_once: 'bool'
    business_has_been_autocreated: 'bool'
    allowed_zone_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64
    name_key: 'LocalizedString'
    description_key: 'LocalizedString'
    transferred_sim_id: 'int'  # fixed uint64
    business_visitors_ids: 'RepeatedCompositeFieldContainer[int]'  # fixed uint64


class BusinessSaveData(Message):
    class BusinessFundsCategoryEntry():
        # __init__
        funds_category: 'int'  # uint32
        amount: 'int'  # int32

    # __init__
    is_open: 'bool'
    funds: 'int'  # int32
    markup: 'float'  # float32
    employee_payroll: 'EmployeeBusinessData'
    open_time: 'int'  # uint64
    grand_opening: 'bool'
    funds_category_tracker_data: 'RepeatedCompositeFieldContainer[BusinessSaveData.BusinessFundsCategoryEntry]'
    daily_revenue: 'int'  # int32
    daily_items_sold: 'int'  # uint32
    lifetime_customers_served: 'int'  # uint32
    restaurant_save_data: 'RestaurantSaveData'
    star_rating_value: 'float'  # float32
    buff_bucket_totals: 'RepeatedCompositeFieldContainer[BusinessBuffBucketTotal]'
    customer_data: 'RepeatedCompositeFieldContainer[CustomerBusinessData]'
    session_customers_served: 'int'  # uint32
    last_off_lot_update: 'int'  # uint64
    buff_bucket_size: 'int'  # uint32
    total_open_hours: 'int'  # uint32
    vet_clinic_save_data: 'VetClinicSaveData'
    rental_unit_save_data: 'RentalUnitSaveData'
    small_business_save_data: 'SmallBusinessSaveData'
    funds_category: 'int'  # uint32
    amount: 'int'  # int32


class BusinessServiceData(Message):
    # __init__
    business_tracker_data: 'RepeatedCompositeFieldContainer[BusinessTrackerData]'
    unowned_business_tracker_data: 'RepeatedCompositeFieldContainer[BusinessTrackerData]'
    first_time_messages: 'RepeatedCompositeFieldContainer[FirstTimeMessages]'
    rental_unit_payout_timer: 'int'  # uint64
    rule_presets_data: 'RepeatedCompositeFieldContainer[BusinessRulePreset]'


class SmallBusinessIncomeData(Message):
    # __init__
    current_day_business_income_record: 'SmallBusinessIncomeRecord'
    total_business_income_record: 'SmallBusinessIncomeRecord'
    attendance_sale_mode_enum: 'int'  # uint32
    is_light_retail_enabled: 'bool'


class SmallBusinessIncomeRecord(Message):
    # __init__
    customers_visited: 'int'  # uint32
    aggregate_customers_hours: 'int'  # uint32
    records_by_revenue: 'RepeatedCompositeFieldContainer[SingleRevenueRecord]'


class SmallBusinessEmployeeData(Message):
    # __init__
    employee_id: 'int'  # fixed uint64
    employee_rules: 'RepeatedCompositeFieldContainer[ClubConductRule]'


class ManageSmallBusinessEmployeeRowData(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
    pay: 'int'  # uint32
    skill_data: 'RepeatedCompositeFieldContainer[ManageEmployeeSkillData]'
    rules: 'RepeatedCompositeFieldContainer[ClubConductRule]'
    is_fake_payment_enabled: 'bool'
    salary_icon: 'ResourceKey'


class ManageSmallBusinessEmployeesData(Message):
    # __init__
    hiring_sim_id: 'int'  # fixed uint64
    employees: 'RepeatedCompositeFieldContainer[ManageSmallBusinessEmployeeRowData]'
    has_no_potential_employees: 'bool'


class BusinessRulePreset(Message):
    # __init__
    name: 'str'
    rules: 'RepeatedCompositeFieldContainer[ClubConductRule]'


class UpdateBusinessRulePresets(Message):
    # __init__
    presets: 'RepeatedCompositeFieldContainer[BusinessRulePreset]'


class SingleRevenueRecord(Message):
    # __init__
    revenue_type: 'int'  # uint32
    count: 'int'  # uint32
    profit: 'int'  # int32


class FirstTimeMessages(Message):
    # __init__
    business_type: 'int'  # fixed uint64
    messages: 'RepeatedCompositeFieldContainer[int]'  # uint32


class AdditionalEmployeeSlotData(Message):
    # __init__
    employee_type: 'int'  # fixed uint64
    additional_slot_count: 'int'  # uint32


class BusinessTrackerData(Message):
    # __init__
    household_id: 'int'  # fixed uint64
    business_type: 'int'  # fixed uint64
    business_manager_data: 'RepeatedCompositeFieldContainer[BusinessManagerData]'
    additional_markup_multiplier: 'float'  # float32
    additional_customer_count: 'float'  # float32
    additional_employee_slot_data: 'RepeatedCompositeFieldContainer[AdditionalEmployeeSlotData]'
    rental_unit_payout_cache: 'int'  # uint32
    zoneless_business_manager_data: 'RepeatedCompositeFieldContainer[BusinessManagerData]'
    sim_id_open_business_on_load: 'int'  # fixed uint64


class BusinessManagerData(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    business_data: 'BusinessSaveData'
    make_unowned_on_load: 'bool'
    sim_id: 'int'  # fixed uint64


class ManageEmployeeSkillData(Message):
    # __init__
    skill_id: 'int'  # fixed uint64
    curr_points: 'int'  # uint32
    skill_tooltip: 'LocalizedString'
    is_training: 'bool'
    has_skilled_up: 'bool'


class MinEmployeeReqMetUpdate(Message):
    # __init__
    zone_id: 'int'  # fixed uint64
    minimum_employee_requirements_met: 'bool'


class DeleteSimBusiness(Message):
    # __init__
    sim_id: 'int'  # fixed uint64
