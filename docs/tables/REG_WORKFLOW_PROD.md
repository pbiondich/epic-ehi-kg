# REG_WORKFLOW_PROD

> The REG_WORKFLOW_PROD table contains productivity data about particular workflows on a patient contact such as Admit, Sign-In, Check-In, and Check-Out. This table stores the number of Admit, Sign-In, Check-In and Check-Out workflows completed. The table only tracks a workflow the first time it is successfully completed for that encounter. For example, when a user first checks in a patient to see the doctor, that will be tracked, but if the user subsequently reenters the Check-In workflow and changes some data, that will not be tracked. Similarly, if a user enters the Check-In workflow to try and check in a patient, but then exits the workflow without checking the patient in, that will not be tracked.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `WKFL_TYPE_C_NAME` | VARCHAR |  | Which type of workflow this line is tracking (e.g. Admit, Sign-In, etcetera). |
| 6 | `WKFL_END_INST_DTTM` | DATETIME (Attached) |  | Stores the instant when the user completed a workflow. |
| 7 | `WKFL_DURATION` | INTEGER |  | Stores the duration of the workflow in seconds. |
| 8 | `WKFL_USER_ID` | VARCHAR |  | Stores the user who completed the workflow. |
| 9 | `WKFL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `WKFL_PAT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `WKFL_LOGIN_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

