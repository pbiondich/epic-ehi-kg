# COVERAGE_COPAY_ECD

> Contains the copay category table (ECD) related group of coverages.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID of the coverage record for this row. This column is frequently used to link to the COVERAGE table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ECD_TBL_COPAYCAT_ID` | VARCHAR |  | Indicate the copay category specialty for which you want to establish a different copay/coinsurance amount. For details on the logic that POS or the Benefits Engine uses to determine the copay/coinsurance amount, please consult the help text of the "Default Copay Amount" or "Default Coinsurance Amount" items. |
| 4 | `ECD_TBL_COPAYCAT_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 5 | `ECD_TABLE_DEPT_C_NAME` | VARCHAR | org | Indicate the department specialty for which you want to establish a different copay/coinsurance amount. For details on the logic that POS or the Benefits Engine uses to determine the copay/coinsurance amount, please consult the help text of the "Default Copay Amount" or "Default Coinsurance Amount" items. |
| 6 | `ECD_TABLE_AMOUNT` | NUMERIC |  | Indicate the copay amount for the corresponding department specialty and/or copay category. For details on the logic that POS or the Benefits Engine uses to determine the copay/coinsurance amount, please consult the help text of the "Default Copay Amount" or "Default Coinsurance Amount" items. |
| 7 | `ECD_TABLE_COINS` | NUMERIC |  | Indicate the coinsurance amount for the corresponding department specialty or copay category. For details on the logic that POS or the Benefits Engine uses to determine the copay/coinsurance amount, please consult the help text of the "Default Copay Amount" or "Default Coinsurance Amount" items. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

