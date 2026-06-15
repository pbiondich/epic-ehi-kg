# PAT_ENC_COPAY_COLL

> Information relating to copays collected using the POS or Registration copay forms (not the AR copay form).

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | Used to indicate which copay the data applies to on the appointment: the 1st copay, 2nd, nth. |
| 3 | `E_PMT_BANK_ACCT_TYPE_C_NAME` | VARCHAR |  | The bank account type for bank account transactions. |
| 4 | `SCANNED_CHECK_YN` | VARCHAR |  | Indicates if a transaction was made using a scanned check. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

