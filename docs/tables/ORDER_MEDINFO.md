# ORDER_MEDINFO

> The ORDER_MEDINFO table is an addendum table for ORDER_MED and enables you to report on detail medication information for each order in clinical system (prescriptions). We have also included patient and contact identification information for each record.

**Primary key:** `ORDER_MED_ID`  
**Columns:** 74  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. |
| 2 | `MED_LINKED_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 3 | `MED_CNCT_DAT_REAL` | FLOAT |  | The real medication contact date (DAT) used in this order. |
| 4 | `LAST_ADMIN_INST` | DATETIME (Local) |  | The last instant that the medication order is administrated in the Medication Administration Record (MAR). |
| 5 | `NUMBER_OF_DOSES` | INTEGER |  | The total number of doses of the medication order that should be given to the patient. |
| 6 | `DOSES_REMAINING` | INTEGER |  | The total number of the medication order which has not been given to patient. |
| 7 | `RESUME_STATUS_C_NAME` | VARCHAR |  | The resume status. |
| 8 | `MIN_RATE` | NUMERIC |  | The minimum rate number. |
| 9 | `MAX_RATE` | NUMERIC |  | The maximum rate number. |
| 10 | `RATE_UNIT_C_NAME` | VARCHAR | org | The rate unit. |
| 11 | `MIN_DURATION` | NUMERIC |  | The minimum duration. |
| 12 | `MAX_DURATION` | NUMERIC |  | The maximum duration. |
| 13 | `MIN_VOLUME` | NUMERIC |  | The minimum volume. |
| 14 | `MAX_VOLUME` | NUMERIC |  | The maximum volume. |
| 15 | `VOLUME_UNIT_C_NAME` | VARCHAR |  | The volume unit of measure associated with the order. |
| 16 | `CALC_VOLUME_YN` | VARCHAR |  | Indicate if the volume is calculated. "Y" means the volume is calculated. "N" means the volume is not calculated. Default is "Y". |
| 17 | `STABILITY` | NUMERIC |  | The stability value. |
| 18 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 19 | `PAT_SUPP_MED_YN` | VARCHAR |  | Indicates if the medication is patient-supplied. 'N' indicates the med is not supplied by the patient. 'Y' indicates the medication is supplied by the patient. |
| 20 | `PAT_SUPP_DOSES` | INTEGER |  | Specifies the number of doses the patient supplies if the medication is patient supplied. |
| 21 | `CALC_MIN_DOSE` | NUMERIC |  | The minimum calculated administer dose. |
| 22 | `CALC_MAX_DOSE` | NUMERIC |  | The maximum calculated administer dose. |
| 23 | `CALC_DOSE_UNIT_C_NAME` | VARCHAR |  | The dose unit for calculated administer dose. |
| 24 | `CALC_DOSE_INFO` | VARCHAR |  | The calculation steps to get calculated administer dose from the ordered dose. |
| 25 | `ADMIN_MIN_DOSE` | NUMERIC |  | The minimum administer dose. |
| 26 | `ADMIN_MAX_DOSE` | NUMERIC |  | The maximum administer dose. |
| 27 | `ADMIN_DOSE_UNIT_C_NAME` | VARCHAR |  | The dose unit for administer dose. |
| 28 | `DONOT_DISP_YN` | VARCHAR |  | Indicate if the medication is not dispensed. 'N' indicates the medication is dispensed. 'Y' indicates the medication is not dispensed. |
| 29 | `DONOT_DISP_DOSE` | INTEGER |  | It is to specify the number of doses which will not be dispensed if the DONOT_DISP_YN column is 'Y' for Yes. |
| 30 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 31 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 32 | `ORDERING_DATE` | DATETIME |  | The date the order was placed in calendar format. |
| 33 | `ORDER_CLASS_C_NAME` | VARCHAR | org | The order class category ID for the prescription, used to determine how the clinical system processes the order. |
| 34 | `CONC_NAME_C_NAME` | VARCHAR | org | The concentration of this order (used only for fixed ratio mixture orders). |
| 35 | `LET_EXPIRE_USER_ID` | VARCHAR |  | The ID of the user who marked order as Let Expire. |
| 36 | `LET_EXPIRE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 37 | `TIME_LET_EXPIRE` | DATETIME (Local) |  | The time when the physician marked the order as Let Expire. |
| 38 | `EXP_AFT_START_TIME` | DATETIME (Local) |  | The date and time the order will expire, based on the amount of time a physician entered for the order to expire after the start time. |
| 39 | `EXP_BEF_END_TIME` | DATETIME (Local) |  | The date and time the order will expire, based on the amount of time a physician entered for the order to expire before the end time. |
| 40 | `ORD_COPIED_C_NAME` | VARCHAR |  | The order copy status: If the order has been copied to another encounter or not. |
| 41 | `ORDER_SOURCE_C_NAME` | VARCHAR |  | Where in the system the order was placed from. |
| 42 | `DFLT_DISCRETE_FREQ_NAME` | VARCHAR |  | A flag to indicate if this order should default discrete ambulatory medication frequency information. |
| 43 | `DFLT_DISCRETE_DOSE_NAME` | VARCHAR |  | A flag to indicate if this order should default discrete ambulatory medication dose information. |
| 44 | `REV_ORD_GRANU_YN` | VARCHAR | org | Determines if an order is reviewed by day or by instant |
| 45 | `EXP_DAYS_YN` | VARCHAR |  | Determines if an expiring order is by days or by instant |
| 46 | `MED_CONTACT_DT` | DATETIME |  | This is the order contact date in human readable form. |
| 47 | `DOSE_CALC_WARNING` | VARCHAR |  | Contains the dose warning generated when the order was entered or verified. |
| 48 | `MIXTURE_TYPE_C_NAME` | VARCHAR |  | Specifies the mixture type if the medication order is a mixture. This column will be empty if the medication is not a mixture. |
| 49 | `MED_DURATION_UNIT_C_NAME` | VARCHAR |  | The duration unit. |
| 50 | `TPN_SITE_C_NAME` | VARCHAR | org | The total parenteral nutrition (TPN) infusion site. |
| 51 | `STABILITY_UNIT_C_NAME` | VARCHAR |  | The stability unit. |
| 52 | `DISP_INDIV_YN` | VARCHAR |  | Indicate if the ingredients are dispensed individually. 'N' indicates the ingredients are dispensed together. 'Y' indicates the ingredients are dispensed individually. |
| 53 | `MR_IS_PERSISTENT_YN` | VARCHAR |  | Indicates whether this order is set to persist after the encounter is closed. Yes indicates the order will not be discontinued; No or blank indicates it will be discontinued. |
| 54 | `MAR_ADMIN_TYPE_C_NAME` | VARCHAR |  | Used for performance to determine the administration type of the order. This gets set once the order has been administered. |
| 55 | `ORD_COMP_YN` | VARCHAR |  | This item determines whether an order is completed or not. |
| 56 | `RATE_CALC_INFO` | VARCHAR |  | Stores the rate calculation info. |
| 57 | `RATE_CALC_WARNING` | VARCHAR |  | Contains the rate warning generated when the order was entered or verified. |
| 58 | `DFLT_DISCRETE_C_NAME` | VARCHAR |  | A flag to indicate if this order should default discrete ambulatory medication information. |
| 59 | `PT_SIG_SMARTTEXT_ID` | VARCHAR |  | The unique identifier of the SmartText record used to generate medication instructions for the patient based on order details. A SmartText record is a text template that can contain text and dynamic data. |
| 60 | `PT_SIG_SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 61 | `DISPENSABLE_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 62 | `TIMELY_THRESHOLD` | INTEGER |  | Number of minutes between the scheduled time for an administration and the actual time given before the administration is considered Late/Early. This is a calculated value specific to each order, derived from settings in the ordered medication, ordered frequency, and System Definitions. |
| 63 | `IS_FAM_YN` | VARCHAR |  | Indicates whether this order is ordered as a Facility-Administered Medication (FAM). 1 indicates the order is a FAM and will not be discontinued on closing the encounter; 0 or blank indicates it will be discontinued. |
| 64 | `ONE_STEP_MED_YN` | VARCHAR |  | Indicates whether the order is a one-step medication, a medication whose administration is documented in one step. |
| 65 | `PRIOR_AUTH_STATUS_C_NAME` | VARCHAR |  | Contains the authorization status of the order when it is released from a treatment plan. |
| 66 | `REFERRAL_AUTH_STATUS_C_NAME` | VARCHAR | org | The referral status category ID of the order record when it is activated. |
| 67 | `RECIPE_AMOUNT` | NUMERIC |  | The recipe quantity amount for a ratio-based mixture medication (a medication which consists of a drug diluted in a base at a fixed concentration). |
| 68 | `RECIPE_UNIT_C_NAME` | VARCHAR |  | The med & dose unit category ID for the recipe quantity for a ratio-based mixture medication. |
| 69 | `ADMIN_INSTRUCTIONS_CHANGE_DTTM` | DATETIME (Local) |  | Tracks the instant when the administration instructions were changed from their system default. |
| 70 | `ADDL_DUES_REMAINING` | INTEGER |  | The count of due times that need to be accounted for before the order can be considered complete, in addition to those that represent ordered due times. |
| 71 | `HAS_COMPONENT_DATA_C_NAME` | VARCHAR |  | The category ID for whether this order has any nutritional component data. |
| 72 | `ORDERED_VOLUME_MED_UNIT_C_NAME` | VARCHAR |  | The volume unit as ordered. This volume unit can be in mL or in weight-based units. |
| 73 | `ORDERED_VOLUME` | NUMERIC |  | The volume as ordered. This volume can be in mL or in weight-based units. |
| 74 | `RX_ENERGY_BASED_YN` | VARCHAR |  | Yes if the mixture is energy-based, No otherwise. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

