# DISCRETE_PAT_INSTR_EDIT

> This table contains contact specific discrete patient instructions information such as the entering user, entry date, and linked medication.

**Primary key:** `DISCRETE_PAT_INSTR_ID`, `CONTACT_DATE_REAL`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DISCRETE_PAT_INSTR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the instructions name record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique contact serial number (CSN) of the discrete patient instructions (DPI) contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `CONTACT_NUM` | INTEGER |  | Stores the contact number |
| 6 | `DISPLAY_NAME` | VARCHAR |  | Display name of the DPI record. |
| 7 | `PAT_CSN` | NUMERIC | FK→ | The contact serial number (CSN) of the patient contact on which these instructions were last edited. |
| 8 | `ENTERING_USER_ID` | VARCHAR |  | Stores the user who last edited this record |
| 9 | `ENTERING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LAST_EDIT_UTC_DTTM` | DATETIME (UTC) |  | Stores the last instant the instructions were edited. |
| 11 | `INSTRUCTIONS_END_UTC_DTTM` | DATETIME (UTC) |  | Stores the date the instructions are no longer valid |
| 12 | `DISCRETE_PAT_INSTR_SRC_C_NAME` | VARCHAR |  | The source of these instructions |
| 13 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 14 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Attached) |  | Stores the instant of entry when a record is edited |
| 15 | `SHOW_CARB_RANGES_YN` | VARCHAR |  | Indicates if carbs should be printed with a range (ex "10-19") or not (ex "10") on the AVS. |
| 16 | `DOSE_ROUNDING_C_NAME` | VARCHAR |  | Indicates if the AVS insulin injection tables should round Down (first row is 0 units) or round Up (first row is one unit increment). |
| 17 | `DOSING_METHOD_C_NAME` | VARCHAR |  | Indicates the dosing method used on the insulin injection tables. |
| 18 | `MAX_BLOOD_GLUCOSE` | NUMERIC |  | Maximum blood glucose, in mg/dL, to display on the AVS insulin injection tables. |
| 19 | `MAX_CARBOHYDRATES` | NUMERIC |  | Maximum carbohydrates to display on the AVS insulin injection tables. |
| 20 | `GLUC_UNIT_INCREMENT` | NUMERIC |  | Indicates the number of units to increment each row of the AVS insulin injection tables by. Enter a value of 0.5 to get half unit increment behavior. |
| 21 | `HYPO_THRESHOLD` | NUMERIC |  | Hypoglycemia threshold, in mg/dL, to display as the lower bound for the first row on the AVS insulin injection tables. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DISCRETE_PAT_INSTR_ID` | [DISCRETE_PAT_INSTRUCTIONS](DISCRETE_PAT_INSTRUCTIONS.md) | sole_pk | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

