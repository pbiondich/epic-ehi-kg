# PAT_SVC_PROV_SEARCH_ACT

> Contains actions performed on or with lists of service providers provided to a patient. Actions can include things like printing the list, and scanning a list back in after the patient has indicated their preference.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SEARCH_LIST_IDENT` | INTEGER |  | An ID for the list of service providers that the result is a part of. This column is frequently used to link to the PAT_SVC_PROV_SEARCH_LIST table. |
| 6 | `SERV_PROV_LIST_ACT_TYP_C_NAME` | VARCHAR |  | The category ID for the type of action that was performed on the list of service providers |
| 7 | `USER_ID` | VARCHAR | FK→ | The user who performed the action on the service provider list. |
| 8 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | The time the action was performed on the service provider list. |
| 10 | `DOCUMENT_ID` | VARCHAR | shared | A document that was printed or scanned for the patient preference list generated in the Patient Choice navigator section. |
| 11 | `LIST_PRINT_STATUS_C_NAME` | VARCHAR |  | The status of the print job if the action type is Printed. |
| 12 | `ACTION_LOCAL_DTTM` | DATETIME (Local) |  | The time the action was performed on the service provider list, in the patient's local time zone. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

