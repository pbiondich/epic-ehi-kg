# HSP_ACCT_MPI

> This table contains Enterprise Master Patient Index (EMPI) ID information for records in the Hospital Accounts Receivable (HAR) master file. This table is useful only if your system is configured to use the EMPI to manage external hospital account IDs. Typically, only sites interfacing with an external hospital billing system would be configured in this manner. Based on your EMPI system settings, each hospital account might have one or more external IDs assigned. A hospital account can have only one effective ID per EMPI ID type at any given time.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID of the hospital account with which this Master Patient Index (MPI) ID is associated. |
| 2 | `LINE` | INTEGER | PK | The line number from the hospital account ID related group for this Master Patient Index (MPI) ID. |
| 3 | `MPI_ID_TYPE_ID` | NUMERIC |  | The ID type for this Master Patient Index (MPI) ID. |
| 4 | `MPI_ID_TYPE_ID_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 5 | `MPI_ID` | VARCHAR |  | This column contains an external, Master Patient Index (MPI) ID for this hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

