# EMBRYOLOGY_RESULT

> Information about the results in an andrology or embryology lab.

**Primary key:** `RESULT_ID`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `EMB_RESULT_INST_UTC_DTTM` | DATETIME (UTC) |  | Stores the UTC result instant for the embryology evaluation or procedure. |
| 3 | `RESP_REQ_OVERRIDE_YN` | VARCHAR |  | Whether any responsibility requirements for this embryology result was overridden. |
| 4 | `RESP_REQ_OVERRIDE_USER_ID` | VARCHAR |  | The user that overrode responsibility requirements for this embryology result. |
| 5 | `RESP_REQ_OVERRIDE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RESP_REQ_OVERRIDE_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant that the responsibility requirements for this embryology result was overridden. |
| 7 | `RESP_REQ_OVRIDE_REASON_C_NAME` | VARCHAR | org | The reason that the responsibility requirement for this embryology result was overridden. |
| 8 | `RESP_REQ_OVERRIDE_COMMENT` | VARCHAR |  | Comment for the responsibility requirement override for this embryology result. |
| 9 | `EMB_RESULT_INST_LOCAL_DTTM` | DATETIME (Attached) |  | Stores the result instant for the embryology evaluation or procedure in the time zone of the lab performing the procedure. |
| 10 | `EMB_RES_RECEIVE_CULTURE_DAY` | INTEGER |  | This item stores the number of culture days that have occurred for the specimen when it was received in the lab. |
| 11 | `EMB_RES_EXTERNAL_FREEZE_DATE` | DATETIME |  | This item stores the date on which the embryology specimen was frozen. |
| 12 | `EMB_RES_EXTERNAL_COMMENTS` | VARCHAR |  | This item stores relevant comments associated with the embryology specimen that came from an external lab. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

