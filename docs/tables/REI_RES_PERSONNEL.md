# REI_RES_PERSONNEL

> The REI_RES_PERSONNEL table contains information about an embryology result's personnel and each person's responsibilities.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REI_EMB_RESPONSIBILITY_C_NAME` | VARCHAR | org | The responsibility of this embryology result that the associated person was responsible for. |
| 4 | `RESPONSIBLE_USER_ID` | VARCHAR |  | The responsible user for the associated responsibility of this embryology result. |
| 5 | `RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RESPONSIBLE_PERSON_TEXT` | VARCHAR |  | The non-user responsible person for the associated responsibility of this embryology result. |
| 7 | `RESPONSIBLE_PERSON_AUTH_YN` | VARCHAR |  | Whether the responsible person for this embryology procedure responsibility has authenticated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

