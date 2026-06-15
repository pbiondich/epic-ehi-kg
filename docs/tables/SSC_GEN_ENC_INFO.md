# SSC_GEN_ENC_INFO

> The SSC_GEN_ENC_INFO table contains one row for each patient-level SmartSet Information contact in the system. These rows contain fields that may be updated for each contact such as contact date, contact owner, and contact type. This table also stores details on care plan goals and interventions and task templates associated with SmartSet Information records.

**Primary key:** `CONTACT_SERIAL_NUM`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | shared | The unique ID of the patient-level SmartSet Information record. |
| 2 | `CONTACT_SERIAL_NUM` | NUMERIC | PK shared | The unique contact serial number for this contact. This number is unique across all patient-level SmartSet Information encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 3 | `GOAL_ID` | VARCHAR | FK→ | The unique ID of the care plan goal that is linked to this SmartSet Information record. |
| 4 | `INTERVENTION_ID` | VARCHAR | FK→ | The unique ID of the care plan intervention that is linked to this SmartSet Information record. |
| 5 | `TASK_TEMPLATE_ID` | VARCHAR |  | The unique ID of the task template that is linked to this SmartSet Information record. |
| 6 | `TASK_TEMPLATE_ID_RECORD_NAME` | VARCHAR |  | This column displays the name of the task template record. |
| 7 | `TASK_TEMPLATE_DAT` | VARCHAR |  | The unique, internal contact date in decimal format of the task template that is linked to this SmartSet Information record. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

