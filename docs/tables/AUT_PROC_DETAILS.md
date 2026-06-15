# AUT_PROC_DETAILS

> This table contains procedure-level details about authorizations. The associated authorization information for the procedure can be found in the AUTHORIZATIONS table by joining the tables on the AUTH_ID columns. Child table AUT_PROC_MODS contains multiple rows of additional information related to each row in this table. You may join to this table on the AUTH_ID columns and AUT_PROC_DETAILS.LINE = GROUP_LINE from that table.

**Primary key:** `AUTH_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK FK→ | The authorization ID for the authorization record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROC_TYPE_C_NAME` | VARCHAR |  | Type of procedure information being authorized. A procedure authorization may be collected for a specific code, a code range, or a procedure component. |
| 4 | `PROC_FREE_TEXT` | VARCHAR |  | Procedure (free text) being authorized. |
| 5 | `PROC_RNG_START` | VARCHAR |  | Starting code of the code range |
| 6 | `PROC_RNG_END` | VARCHAR |  | Ending code of the code range |
| 7 | `PROC_COMP_ID` | VARCHAR |  | Procedure component being authorized. This column is frequently used to link to the CL_CMP table. |
| 8 | `PROC_COMP_ID_COMPONENT_NAME` | VARCHAR |  | The name of the component |
| 9 | `REV_CODE_ID` | NUMERIC |  | Procedure revenue code. This column is frequently used to link to the CL_UB_REV_CODE table. |
| 10 | `REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 11 | `PROC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `PROC_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 13 | `PROC_DISCIPLINE_C_NAME` | VARCHAR | org | The Home Health and Hospice discipline category ID for the authorization. |
| 14 | `PROC_LEVELOFCARE_C_NAME` | VARCHAR |  | This column stores the hospice level of care that is authorized by this authorization period. This level of care is sourced from the hospice place of service table and is derived from the Medicare-defined list of hospice levels of care. |
| 15 | `SRC_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 16 | `PROC_MED_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 17 | `PROC_SVC_TYPE_CODE_C_NAME` | VARCHAR |  | Procedure level service type override. |
| 18 | `MED_DIRECTOR_REV_REQ_YN` | VARCHAR |  | Does the procedure require a medical director review? |
| 19 | `PROC_CODE_DESC` | VARCHAR |  | Item to track the procedure code description. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_ID` | [AUTHORIZATIONS](AUTHORIZATIONS.md) | overflow_master | medium |

