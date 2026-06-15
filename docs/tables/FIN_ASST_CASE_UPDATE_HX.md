# FIN_ASST_CASE_UPDATE_HX

> This table contains the updates made to financial assistance case record. Whenever any of the following details of a case record are changed, a row is added to this table. 1. Case status 2. Case flags 3. Assigned user 4. Follow up date 5. Application provided date 6. Application signed date 7. Primary Contact (Guarantor) 8. Patients on the case.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (in UTC time zone) when an update was made. |
| 4 | `UPDATE_USER_ID` | VARCHAR |  | The unique ID of the user who made the update. |
| 5 | `UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `UPDATE_STATUS_C_NAME` | VARCHAR |  | The category ID of the financial assistance case status after an update was made. |
| 7 | `UPDATE_APPL_PROVD_DATE` | DATETIME |  | The application provided date on the financial assistance case after an update was made. |
| 8 | `UPDATE_APPL_SIGNED_DATE` | DATETIME |  | The application signed date on the financial assistance case after an update was made. |
| 9 | `UPDATE_CONTACT_ACCOUNT_ID` | NUMERIC |  | The unique ID of the primary contact (guarantor) of the financial assistance case after an update was made. |
| 10 | `UPDATE_NOTE_ID` | VARCHAR |  | Stores the unique ID of the note record that contains the comment entered as part of this row. This will only be populated if the user manually entered a comment for the financial assistance case. |
| 11 | `UPDATE_NOTE_SUMMARY` | VARCHAR |  | Stores a brief description of the changes made between this row and the last row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

