# DOC_PROVIDER

> This table contains information entered in the documentation provider table during charge entry. Since one transaction may have multiple rows of documentation provider data, each row in this table represents one line of documentation provider data and is identified by the transaction ID and line number. The data for this table is extracted using a KB_SQL query.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID of the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number to identify each row of documentation provider data associated with an individual transaction. |
| 3 | `POST_DATE` | DATETIME |  | The post date of the transaction identified by TX_ID. |
| 4 | `DOC_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `DOC_PROV_FUNC_C_NAME` | VARCHAR | org | The category value associated with the function performed by the documentation provider as recorded in billing system charge entry such as Supervised, Performed, or Assisted. |
| 6 | `DOC_START_DATE` | DATETIME |  | The date on which this provider’s participation began. |
| 7 | `DOC_END_DATE` | DATETIME |  | The date on which this provider’s participation ended. |
| 8 | `DOC_START_TIME` | DATETIME (Local) |  | The time of day at which this provider’s participation began. |
| 9 | `DOC_END_TIME` | DATETIME (Local) |  | The time of day at which this provider’s participation ended. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

