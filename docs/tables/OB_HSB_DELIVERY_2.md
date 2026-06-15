# OB_HSB_DELIVERY_2

> This table contains information about the delivery for this pregnancy, as entered in Stork's Delivery Summary activity.

**Overflow of:** [OB_HSB_DELIVERY](OB_HSB_DELIVERY.md)  
**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 15  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. |
| 2 | `AUGMENTATION_DTTM` | DATETIME (Local) |  | Stores the date that augmentation of labor began. |
| 3 | `DEL_LIVING_CMT` | VARCHAR |  | This provides users an opportunity to provide additional information about the living status in OB History. |
| 4 | `DEL_ADDL_CMT` | VARCHAR |  | This provides users an opportunity to document information related to a delivery that is not captured elsewhere. |
| 5 | `OB_HX_LIVING_STAT_C_NAME` | VARCHAR | org | Stores the living status in OB History, which reflects the current living status of the child. This status may be different than the living status set in the Delivery Summary. |
| 6 | `OB_DEL_PLCENTA_LOC_DTTM` | DATETIME (Local) |  | Stores the date and time the placenta was delivered. This is the same value as in OB_HSB_DELIVERY.OB_DEL_PLCENTA_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| 7 | `PUSHING_START_LOC_DTTM` | DATETIME (Local) |  | Stores the instant when the mother starts to push for the first time during a delivery. This is the same value as in OB_HSB_DELIVERY.PUSHING_START_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| 8 | `CORD_CLAMP_LOC_DTTM` | DATETIME (Local) |  | Stores the instant the umbilical cord was clamped. This is the same value as in OB_HSB_DELIVERY.CORD_CLAMP_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| 9 | `DECISION_LOC_DTTM` | DATETIME (Local) |  | Stores the instant the decision was made for an emergent c-section. This is the same value as in OB_HSB_DELIVERY.DECISION_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| 10 | `BREAST_FEED_ST_LOC_DTTM` | DATETIME (Local) |  | Stores the instant that breastfeeding was initiated. This is the same value as in OB_HSB_DELIVERY.BREAST_FEED_ST_DTTM but converted to the local time of the delivery encounter. This column will be blank for deliveries documented directly in OB History. |
| 11 | `DEL_PLACENTAL_WT` | NUMERIC |  | This item stores the placental weight in ounces. This information is stored in the delivery records. |
| 12 | `ESTAB_RESPIR_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant respiration was established for the newborn. |
| 13 | `OB_DEL_LABOR_TYPE_C_NAME` | VARCHAR |  | Stores the labor type category ID for the delivery record. |
| 14 | `PRIMARY_INDUCTION_REASON_C_NAME` | VARCHAR | org | Records a singular, primary reason for induction. |
| 15 | `ETHNIC_GROUP_C_NAME` | VARCHAR | org | The baby's ethnic group category ID for the historical delivery record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

