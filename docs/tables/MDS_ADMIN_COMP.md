# MDS_ADMIN_COMP

> The MDS_ADMIN_COMP table contains information relevant to the Z0400 signatures found on a Minimum Data Set (MDS) assessment under Section Z.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MDS_ADMIN_SIG_USER_ID` | VARCHAR |  | This column contains the User IDs of persons completing sections of the MDS assessment. |
| 4 | `MDS_ADMIN_SIG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `MDS_ADMIN_SIG_DTTM` | DATETIME (UTC) |  | This column contains the instant a user signed for section completion for the MDS assessment. |
| 6 | `MDS_ADMIN_SIG_FOR_USER_ID` | VARCHAR |  | This column contains the signatures of persons signing in Z0400 for another user. |
| 7 | `MDS_ADMIN_SIG_FOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

