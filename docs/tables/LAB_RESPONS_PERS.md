# LAB_RESPONS_PERS

> Lab Anatomic Pathology case responsible person.

**Primary key:** `REQUISITION_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUISITION_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESPONSIBLE_PERS_ID` | VARCHAR |  | The unique identifiers of the users that have responsibility for the current Anatomic Pathology case. In conjunction with Responsible Role, it identifies the various types of responsibility. |
| 4 | `RESPONSIBLE_PERS_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RESPONSIBLE_ROLE_C_NAME` | VARCHAR | org | This item defines the role of the related person responsible for this case. |
| 6 | `RESPONSIBLE_DTTM` | DATETIME (Attached) |  | The instant when the corresponding user has taken the responsibility of the case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

