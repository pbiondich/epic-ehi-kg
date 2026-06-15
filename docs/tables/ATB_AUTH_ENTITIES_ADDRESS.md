# ATB_AUTH_ENTITIES_ADDRESS

> The Auth Entities Address table contains multiple address line data as it pertains to a single entity outlined in the Auth Entities table.

**Primary key:** `AUTH_BUNDLE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the auth bundle record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated entity in the auth bundle. Together with AUTH_BUNDLE_ID, this forms the foreign key to the ATB_AUTH_ENTITIES table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple entity address values associated with the auth bundle and the auth entitty from the ATB_AUTH_ENTITIES table. |
| 4 | `ENTITY_ST_ADDR` | VARCHAR |  | The street address associated with the entity's address information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

