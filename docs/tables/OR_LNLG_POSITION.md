# OR_LNLG_POSITION

> This table contains the Patient Positioning information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 19  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `PAT_POSITION_C_NAME` | VARCHAR | org | The position of the patient. |
| 3 | `HEAD_POS_C_NAME` | VARCHAR | org | The head position of the patient. |
| 4 | `RT_ARM_POS_C_NAME` | VARCHAR | org | The right arm position of the patient. |
| 5 | `LEFT_ARM_POS_C_NAME` | VARCHAR |  | The left arm position of the patient. |
| 6 | `RT_LEG_POS_C_NAME` | VARCHAR | org | The right leg position of the patient. |
| 7 | `LEFT_LEG_POS_C_NAME` | VARCHAR |  | The left leg position of the patient. |
| 8 | `POS_PROC_ID` | VARCHAR |  | The procedure ID of the current position. |
| 9 | `POS_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 10 | `PROC_ORDINAL` | INTEGER |  | The ordinal of the position. |
| 11 | `POSITION_TIME` | DATETIME (Local) |  | The time at which the patient was positioned. |
| 12 | `POS_RECORD_ID_TANK_NAME` | VARCHAR |  | The name of the tank record. |
| 13 | `PANEL_NUM_POSITION` | INTEGER |  | Panel number to which positioning data applies |
| 14 | `PAT_POSITION_C_CMT` | VARCHAR |  | Comment for the patient's body position. |
| 15 | `HEAD_POS_C_CMT` | VARCHAR |  | Comment for the patient's head position. |
| 16 | `RT_ARM_POS_C_CMT` | VARCHAR |  | Comment for the patient's right arm position. |
| 17 | `LEFT_ARM_POS_C_CMT` | VARCHAR |  | Comment for the patient's left arm position. |
| 18 | `RT_LEG_POS_C_CMT` | VARCHAR |  | Comment for the patient's right leg position. |
| 19 | `LEFT_LEG_POS_C_CMT` | VARCHAR |  | Comment for the patient's left leg position. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

