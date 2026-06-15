# PAT_CALL_DISP

> The PAT_CALL_DISP table contains the information regarding the disposition given to a patient during a phone encounter. Each row corresponds to one disposition.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE_COUNT`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE_COUNT` | INTEGER | PK | The line number of the disposition within the encounter. |
| 2 | `CONTACT_DATE` | DATETIME |  | The contact date of the encounter. Note: There may be multiple encounters on the same calendar date. |
| 3 | `PHONE_DISP_C_NAME` | VARCHAR | org | The disposition given to the patient on the phone. |
| 4 | `PHONE_DISP_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `PHONE_DISP_TIME` | DATETIME |  | The time the disposition was given. |
| 6 | `PHONE_DISP_CMT` | VARCHAR |  | The comment entered by the user when the disposition was given. |
| 7 | `PHONE_DISP_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `CM_CT_OWNER_ID` | VARCHAR |  | ID of the deployment owner for this contact. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 10 | `ORIGINAL_DISP_C_NAME` | VARCHAR |  | The original disposition if the disposition was overridden, or nothing if the disposition was not overridden. |
| 11 | `SUGGEST_PROTOCOL_ID` | NUMERIC |  | The most recently used protocol that suggested the original disposition. |
| 12 | `SUGGEST_PROTOCOL_ID_PROTOCOL_NAME` | VARCHAR |  | The display name of the protocol. |
| 13 | `PHONE_DISP_SUGGST_C_NAME` | VARCHAR |  | If disposition filtering is turned on, this column stores if a disposition was suggested by a protocol, manually entered, or both suggested and manually entered/edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

