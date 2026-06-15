# ATB_AUTH_OBJECTIVES

> This table contains data for authorization objectives. A row in this table represents one objective.

**Primary key:** `AUTH_BUNDLE_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OBJECTIVE_ID_REF` | VARCHAR |  | The reference ID to use to distinguish this objective from other objective lines in the objective related group. |
| 4 | `OBJECTIVE_TYPE_C_NAME` | VARCHAR |  | This item store the type of objective that the data ona given line in the objective related group represents. |
| 5 | `OBJECTIVE_STATUS_C_NAME` | VARCHAR |  | This item holds the status of the objective on a given line of the objective related group. |
| 6 | `OBJ_AUTH_BUNDLE_ID` | NUMERIC |  | This item contains the ID of the ATB record that the objective will be completed on. This item is populated only on ATBs of type Authorization in order to get to the correct ATB of type Authorization Event to be edited. |
| 7 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | Contains the instant that a given objective was created. Stored as instant in UTC. |
| 8 | `CREATION_USER_ID` | VARCHAR |  | Stores the user responsible for creating or starting an objective, if the objective was manually created. Blank if the objective was automatically created. |
| 9 | `CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `RESOLUTION_UTC_DTTM` | DATETIME (UTC) |  | Contains the instant that an objective was completed or discarded. The instant is stored as the value in UTC. |
| 11 | `RESOLUTION_USER_ID` | VARCHAR |  | Stores the user responsible for completing or discarding the authorization objective on the given line of the objective related group. |
| 12 | `RESOLUTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

