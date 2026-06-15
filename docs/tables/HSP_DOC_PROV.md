# HSP_DOC_PROV

> This table contains hospital account transaction documentation provider information from the Hospital Permanent Transactions (HTR) master file.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the charge transaction. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. As multiple documentation providers can be associated with one charge, each charge will have a unique line number. |
| 3 | `POST_DATE` | DATETIME |  | The post date of the charge. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `DOC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `DOC_PRV_FUNC_HA_C_NAME` | VARCHAR | org | The function of the documentation provider that is stored in the charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

