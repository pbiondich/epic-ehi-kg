# MEM_LIST_DETAIL_REPL

> The MEM_LIST_DETAIL_REPL table contains a list of members in a transaction like capitation computation or capitation receipt and reconciliation.

**Primary key:** `MEM_LIST_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MEM_LIST_ID` | NUMERIC | PK shared | The ID of the transaction member list record computed as part of the specialty capitation payment process. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEMBER_LIST` | VARCHAR |  | The ID of the member eligible for inclusion in specialty capitation payment computations. |
| 4 | `COVERAGE_LIST` | NUMERIC |  | The ID of the coverage record for the member under which the member is eligible for inclusion in specialty capitation payment computations. |
| 5 | `MEMBER_DOB` | DATETIME |  | The date of birth for the member eligible for inclusion in specialty capitation payment computations. |
| 6 | `MEMBER_SEX_C_NAME` | VARCHAR | org | The sex of the member eligible for inclusion in specialty capitation payment computations. |
| 7 | `MEMBER_CVG_ATTRS_EXTERNAL` | VARCHAR |  | Stores members' coverage attributes formatted by category list CVG 2001. |
| 8 | `MEM_MCARE_CONTRACT_NUM` | VARCHAR |  | Stores the member's medicare advantage contract number. |
| 9 | `WITHHOLD_REASON_C_NAME` | VARCHAR |  | The specialty capitation payment withhold reason category ID for a member in the transaction. |
| 10 | `MEMBER_REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 11 | `MEMBER_MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

