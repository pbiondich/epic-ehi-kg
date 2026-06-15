# ALTERNATIVE_PROCS

> This table contains information about alternative procedures selected for patients.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 24  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line count for alternative procedure items. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 6 | `ALT_PROC_LMA_ID` | NUMERIC |  | The identifier for the alternative procedure (LMA) record. |
| 7 | `ALT_PROC_LMA_ID_ALTERNATIVE_NAME` | VARCHAR |  | This column contains the name of the alternative medication and procedure records. |
| 8 | `ALT_PROC_ORIG_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `ALT_PROC_OPTION_C_NAME` | VARCHAR |  | Alternative procedure option taken. |
| 10 | `ALT_PROC_USER_ID` | VARCHAR |  | ID of user who ordered the alternative procedure. |
| 11 | `ALT_PROC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `ALT_PROC_TIME` | DATETIME (Attached) |  | Instant the alternative was taken. |
| 13 | `ALT_PROC_ORDER_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 14 | `ALT_PROC_CLS_C_NAME` | VARCHAR | org | Order class for alternative procedure. |
| 15 | `ALT_PROC_QUANTITY` | VARCHAR |  | Quantity for alternative procedure. |
| 16 | `ALT_PROC_PRIO_C_NAME` | VARCHAR | org | Priority of alternative procedure. |
| 17 | `ALT_PROC_REL_COST` | VARCHAR |  | Relative cost of alternative procedure. |
| 18 | `ALT_PROC_WHEN_C_NAME` | VARCHAR | org | When value for alternative procedure. |
| 19 | `ALT_PROC_FREQ_ID` | VARCHAR |  | Frequency of alternative procedure. |
| 20 | `ALT_PROC_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 21 | `ALT_PROC_COUNT` | INTEGER |  | Count value for alternative procedure. |
| 22 | `ALT_PROC_CONTINUE_C_NAME` | VARCHAR | org | The continue reason category number for the alternative procedure alert. |
| 23 | `ALT_PROC_FB_DISC_C_NAME` | VARCHAR |  | Captures the discrete positive/negative procedure alternatives feedback value. |
| 24 | `ALT_PROC_FB_COMMENT` | VARCHAR |  | Captures freetext feedback comments on the procedure alternative. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

