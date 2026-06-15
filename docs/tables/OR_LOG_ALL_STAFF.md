# OR_LOG_ALL_STAFF

> The OR_LOG_ALL_STAFF table contains information about all staff members associated with a procedural case that has been performed. This includes physicians, procedural staff, anesthesia staff, pre-op nurses, and recovery nurses.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID associated with the procedural log record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STAFF_TYPE_MAP_C_NAME` | VARCHAR |  | The staff type mapping category ID for the staff member. |
| 4 | `STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `ROLE_C_NAME` | VARCHAR | org | The role category ID for the staff member. This will only have a value for physicians. |
| 6 | `SERVICE_C_NAME` | VARCHAR | org | The service category ID for the staff member. This will only have a value for physicians. |
| 7 | `PANEL` | INTEGER |  | The panel number for the staff member. This will only have a value for physicians. |
| 8 | `STAFF_TYPE_C_NAME` | VARCHAR | org | The staff type category ID for the staff member. This will only have a value for procedural staff. |
| 9 | `ANES_STAFF_TYPE_C_NAME` | VARCHAR | org | The anesthesia staff type category ID for the staff member. This will only have a value for anesthesia staff. |
| 10 | `ACCOUNTBLE_STAFF_YN` | VARCHAR |  | Indicates whether the staff member is considered primary or responsible for the log record represented by this row. Y indicates that the staff member is considered primary for procedural staff or responsible for anesthesia providers. N indicates that the staff member is not considered primary or responsible. For physicians, it is only the primary physician on the first panel. |
| 11 | `TIME_DURATION_MINS` | INTEGER |  | The length of time the staff member is documented as either in room or responsible in minutes for the log represented by this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

